import logging

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.core.database import engine
from app.core.query import QueryData


class BaseController(object):
    """Base View to create helpers common to all Webservices.
    """

    def __init__(self, db: Session = None):
        """Constructor
        """
        self.close_session = None
        self.model_class = None

        if db:
            self.db = db
        else:
            self.db = Session(engine)
            self.close_session = True

    def read(
            self,
            offset: int = 0,
            limit: int = 100,
            sort_by: str = 'id',
            order_by: str = 'desc',
            qtype: str = 'first',
            params: dict = {},
            **kwargs):
        """Get a record from the database.
        """
        limit = limit if limit <= 100 else 100
        query_data = QueryData(
            model_class=self.model_class,
            params=params
        )

        try:
            query_model = self.db.query(self.model_class)
            for data in query_data:
                query_model = query_model.filter(
                    data.field == data.value
                )

            sort_by = getattr(self.model_class, sort_by)

            return getattr(query_model.order_by(
                getattr(sort_by, order_by)()).offset(offset).limit(limit), qtype)()

        except Exception as error:
            logging.error(error)
            raise Exception(error)

        finally:
            if self.close_session:
                self.db.close()

    def create(self, data: dict):
        """Create a record in the database.
        """
        db_data = self.model_class(**data)

        try:
            self.db.add(db_data)
            self.db.commit()
            self.db.refresh(db_data)
            return db_data

        except IntegrityError as error:
            logging.error(error)
            return None

        except Exception as error:
            logging.error(error)
            raise Exception(error)

        finally:
            if self.close_session:
                self.db.close()

    def update(
            self,
            data: dict,
            id: int = None,
            params: dict = list()):
        """Edit a record in the database.
        """
        try:
            query_model = self.db.query(self.model_class)
            if id:
                query_model = query_model.filter(
                    self.model_class.id == id
                )

            if params:
                for item in params:
                    if params.get(item) is not None:
                        query_model = query_model.filter(
                            getattr(self.model_class, item) == params.get(item)
                        )

            query_model = query_model.one_or_none()

            if query_model:
                for item in data:
                    if data.get(item) is not None:
                        setattr(query_model, item, data[item])

                self.db.merge(query_model)
                self.db.commit()
                self.db.refresh(query_model)

                return query_model

        except Exception as error:
            logging.error(error)
            raise Exception(error)

        finally:
            if self.close_session:
                self.db.close()

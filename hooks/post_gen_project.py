from os import remove, rename
from pathlib import Path
from shutil import rmtree


CONTEXT = Path.cwd()


def rename_endpoint(file: str, for_file: str) -> None:
    context_path = CONTEXT.joinpath(
        'app', 'api', 'v1', 'endpoints', file
    )
    context_path_new = CONTEXT.joinpath(
        'app', 'api', 'v1', 'endpoints', for_file
    )

    rename(context_path, context_path_new)


def remove_endpoint(file: str) -> None:
    context_path = CONTEXT.joinpath('app', 'api', 'v1', 'endpoints', file)
    remove(context_path)


def remove_mkdocs() -> None:
    context_path = CONTEXT.joinpath('docs')
    remove('mkdocs.yml')
    rmtree(context_path)


def remove_templates() -> None:
    context_path = CONTEXT.joinpath('app', 'static')
    rmtree(context_path)


def main():
    if "{{ cookiecutter.use_mkdocs }}" != "y":
        remove_mkdocs()

    if "{{ cookiecutter.use_templates }}" != "y":
        remove_templates()

    if "{{ cookiecutter.use_auth }}" == "y":
        remove_endpoint(file='item.py')
        rename_endpoint(file='item_auth.py', for_file='item.py')
    else:
        remove_endpoint(file='item_auth.py')


if __name__ == "__main__":
    main()

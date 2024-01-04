from os import remove
from pathlib import Path
from shutil import rmtree


CONTEXT = Path.cwd()


def remove_mkdocs():
    context_path = CONTEXT.joinpath('docs')
    remove('mkdocs.yml')
    rmtree(context_path)


def remove_templates():
    context_path = CONTEXT.joinpath('app', 'static')
    rmtree(context_path)


def main():
  if "{{ cookiecutter.use_mkdocs }}" != "y":
        remove_mkdocs()

  if "{{ cookiecutter.use_templates }}" != "y":
        remove_templates()


if __name__ == "__main__":
    main()

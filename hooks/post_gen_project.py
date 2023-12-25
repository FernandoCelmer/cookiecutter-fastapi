from os import remove
from pathlib import Path
from shutil import rmtree

def remove_mkdocs():
    remove(Path.home().joinpath('docs'))
    rmtree('mkdocs.yml')


def main():
  if "{{ cookiecutter.use_mkdocs }}" != "y":
        remove_mkdocs()


if __name__ == "__main__":
    main()

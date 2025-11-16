"""
This module contains the post-generation project hooks.
"""

from os import remove
from pathlib import Path
from shutil import rmtree
from subprocess import run


CONTEXT = Path.cwd()


def remove_mkdocs() -> None:
    """Remove the mkdocs files and directories."""
    mkdocs_file = CONTEXT.joinpath('mkdocs.yml')
    if mkdocs_file.exists():
        remove(mkdocs_file)

    docs_dir = CONTEXT.joinpath('docs')
    if docs_dir.exists():
        rmtree(docs_dir)


def remove_templates() -> None:
    """Remove all template-related files and directories."""
    static_path = CONTEXT.joinpath('app', 'static')
    if static_path.exists():
        rmtree(static_path)

    templates_config_path = CONTEXT.joinpath('app', 'core', 'templates.py')
    if templates_config_path.exists():
        remove(templates_config_path)

    templates_endpoint_path = CONTEXT.joinpath('app', 'api', 'v1', 'endpoints', 'templates.py')
    if templates_endpoint_path.exists():
        remove(templates_endpoint_path)

    templates_test_path = CONTEXT.joinpath('tests', 'test_templates.py')
    if templates_test_path.exists():
        remove(templates_test_path)


def remove_github_workflow() -> None:
    """Remove the GitHub workflow directory."""
    github_dir = CONTEXT.joinpath('.github')
    if github_dir.exists():
        rmtree(github_dir)


def remove_test_auth() -> None:
    """Remove the test authentication file."""
    test_auth_path = CONTEXT.joinpath('tests', 'test_auth.py')
    if test_auth_path.exists():
        remove(test_auth_path)


def fix_imports() -> None:
    """Fix import sorting with Ruff."""
    try:
        run(
            ["ruff", "check", "--fix", "app/", "tests/"],
            cwd=CONTEXT,
            check=False
        )
    except FileNotFoundError:
        try:
            run(
                ["poetry", "run", "ruff", "check", "--fix", "app/", "tests/"],
                cwd=CONTEXT,
                check=False
            )
        except FileNotFoundError:
            pass


def main():
    """Main function to remove the unwanted files and directories."""
    if "{{ cookiecutter.use_mkdocs }}" != "y":
        remove_mkdocs()

    if "{{ cookiecutter.use_templates }}" != "y":
        remove_templates()

    if "{{ cookiecutter.use_github_workflow }}" != "y":
        remove_github_workflow()

    if "{{ cookiecutter.use_auth }}" == "n":
        remove_test_auth()

    fix_imports()


if __name__ == "__main__":
    main()

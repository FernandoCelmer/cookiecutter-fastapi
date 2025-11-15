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


def remove_github_workflow() -> None:
    workflow_path = CONTEXT.joinpath('.github', 'workflows', 'python-app-code.yml')
    if workflow_path.exists():
        remove(workflow_path)

    github_dir = CONTEXT.joinpath('.github', 'workflows')
    if github_dir.exists() and not any(github_dir.iterdir()):
        rmtree(CONTEXT.joinpath('.github'))


def remove_test_auth() -> None:
    test_auth_path = CONTEXT.joinpath('tests', 'test_auth.py')
    if test_auth_path.exists():
        remove(test_auth_path)


def main():
    if "{{ cookiecutter.use_mkdocs }}" != "y":
        remove_mkdocs()

    if "{{ cookiecutter.use_templates }}" != "y":
        remove_templates()

    if "{{ cookiecutter.github_action_code_scan }}" != "y":
        remove_github_workflow()

    if "{{ cookiecutter.use_auth }}" == "n":
        remove_test_auth()


if __name__ == "__main__":
    main()

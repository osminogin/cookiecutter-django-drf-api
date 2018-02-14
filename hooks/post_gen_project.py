#!/usr/bin/env python3
import subprocess
from pathlib import Path


def run(command, log=True):
    try:
        subprocess.run(command, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as error:
        print('{}: {}\n{}'.format(error.returncode, error.cmd, error.output))
        raise error

    if log:
        print('{}\n'.format(' '.join(command)))
    else:
        print(' '.join(command))


def which(command):
    try:
        import shutil
        assert hasattr(shutil, 'which')
        full_path = shutil.which(command)
        assert full_path
        return full_path
    except AssertionError:
        raise RuntimeError('Command {} not installed'.format(command))


def setup_git_repo():
    git = which('git')
    print(git)
    run([git, 'init'])
    run([git, 'add', '.'])
    run([git, 'status'])
    run([git, 'commit', '-m', 'Initial commit'])


def setup_virtualenv(python):
    python = which(python)
    try:
        # First try bundled venv module
        import venv     # noqa
        run([python, '-m', 'venv', './env'])
    except ImportError:
        # Second try use virtualenv
        try:
            virtualenv = which('virtualenv')
            run([virtualenv, '-p', python, './venv'])
        except AssertionError:
            raise RuntimeError('Python venv module or virtualenv required')


def install_dependencies():
    """
    Install project dependencies inside venv.
    """
    cwd = Path(__file__).parent.cwd()
    python = cwd / '..' / 'env' / 'bin' / 'python'
    requirements = cwd / '..' / 'requirements.txt'
    run([python, 'install', '-U', '-r', requirements])
    python = cwd / '..' / 'env' / 'bin' / 'python'
    requirements = cwd / '..' / 'requirements.txt'
    run([python, 'install', '-U', '-r', requirements])


def cleanup():
    """
    Removing unnecessary files from project directory.
    """
    if '{{ cookiecutter.use_registration }}' == 'n':
        run(['rm', '-rf', 'templates/registration'])
    if '{{ cookiecutter.use_heroku }}' == 'n':
        run(['rm', 'Procfile'])
    if '{{ cookiecutter.use_vscode }}' == 'n':
        run(['rm', '-rf', '.vscode'])


if __name__ == '__main__':
    setup_git_repo()
    if 'python' in '{{ cookiecutter.use_virtualenv }}':
        setup_virtualenv('{{ cookiecutter.use_virtualenv }}')
        install_dependencies()
    print('\n{{cookiecutter.project_slug}} setup successfully!\n\n')
    cleanup()

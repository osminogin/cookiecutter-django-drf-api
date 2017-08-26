import os
import codecs
import subprocess


def run(command, log=True):
    try:
        output = codecs.decode(subprocess.check_output(command), 'utf-8')
    except subprocess.CalledProcessError as error:
        print('{}: {}\n{}'.format(error.returncode, error.cmd, error.output))
        raise error
    else:
        if output and log:
            print('{}\n{}'.format(' '.join(command), output))
        else:
            print(' '.join(command))
    return output


def which(command):
    # For python 3.3 and later
    try:
        import shutil
        assert hasattr(shutil, 'which')
        return shutil.which(command)
    # For python 3.2 and earlier
    except (ImportError, AssertionError):
        for path in os.environ['PATH'].split(os.pathsep):
            full_path = os.path.join(path, command)
            if os.access(full_path, os.X_OK):
                return full_path


def setup_git_repo():
    assert which('git')
    run(['git', 'init'])
    run(['git', 'add', '.'])
    run(['git', 'status'])
    run(['git', 'commit', '-m', 'Initial commit'])


def setup_virtualenv(python):
    python_command = which(python)
    assert python_command
    # First try included venv module
    try:
        import venv     # noqa
        run([python_command, '-m', 'venv', './venv'])
    except ImportError:
        # Second try use virtualenv
        try:
            virtualenv_command = which('virtualenv')
            assert virtualenv_command
            run([virtualenv_command, '-p', python_command, './venv'])
        except AssertionError:
            raise RuntimeError('Python venv module or virtualenv required')


def cleanup():
    """
    Removing unnecessary files from project directory.
    """
    if '{{ cookiecutter.use_heroku }}' == 'n':
        run(['rm', 'Procfile'])
    if '{{ cookiecutter.use_vscode }}' == 'n':
        run(['rm', '-rf', '.vscode'])


def main():
    setup_git_repo()
    if 'python' in '{{ cookiecutter.use_virtualenv }}':
        setup_virtualenv('{{ cookiecutter.use_virtualenv }}')
    cleanup()
    print('\n{{cookiecutter.project_slug}} setup successfully!\n\n')


if __name__ == '__main__':
    main()

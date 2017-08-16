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


def setup_git_repo():
    run(['git', 'init'])
    run(['git', 'add', '.'])
    run(['git', 'status'])
    run(['git', 'commit', '-m', 'Initial commit'])


def main():
    setup_git_repo()
    print('\n{{cookiecutter.project_slug}} setup successfully!\n\n')


if __name__ == '__main__':
    main()

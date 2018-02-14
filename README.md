# Cookiecutter Django Ultimate

[![](https://img.shields.io/github/release/osminogin/cookiecutter-django-ultimate.svg?style=flat)](https://github.com/osminogin/cookiecutter-django-ultimate/releases/latest) ![python 3.5, 3.6](https://img.shields.io/badge/python-3.5.4%2C%203.6.2-green.svg?style=flat) ![license](https://img.shields.io/badge/license-MIT-green.svg) [![Requirements Status](https://requires.io/github/osminogin/cookiecutter-django-ultimate/requirements.svg?branch=master)](https://requires.io/github/osminogin/cookiecutter-django-ultimate/requirements/?branch=master)


Ultimate Django project template via [cookiecutter](https://github.com/audreyr/cookiecutter) include most of Django features and apps.

## Features

* Latest Django 2.0, Python 3.6 stable releases.
* PostgreSQL, MariaDB databases (or SQLite for developing).
* Celery, Redis Server for cache and async queue (if enabled).
* Docker support.
* Django REST Framework for public and private APIs.
* Ready for instant deploying to Heroku.
* User authentication (login/logout) and registration (with email confirmation).
* Assets storage via S3 (or any object storage with plugins).


## Requirements

Install `cookiecutter` command line util:

```bash
sudo pip3 install cookiecutter
# or more secure (but add ~/.local/bin to $PATH env)
pip3 install --user cookiecutter
```

## Usage

Generate a new Cookiecutter template layout:

```bash
cookiecutter gh:osminogin/cookiecutter-django-ultimate
```

## License

This project is licensed under the terms of the [MIT License](/LICENSE).

# -*- coding: utf-8 -*-
import os
import re
import shutil


def fix_template_expansion(content, replacements):
    """
    fix template expansion after hook copy
    :param content: the duplicated hook content
    :param replacements: array of dictionaries
                         cookiecutter_key => template key expanded
    """
    for replacement in replacements:
        for key, to_be_replaced in replacement.items():
            replacement = chr(123) + chr(123) + \
                'cookiecutter.' + key + chr(125) + chr(125)
            content = content.replace(to_be_replaced, replacement)
    return content


def get_file_content(file):
    """
    get the content of a given file
    :param file: the file to get the content of
    """
    return open(file, 'r').read()


def set_file_content(file, content):
    """
    write content to file
    :param file: the file to rewrite its content
    :param content: content to write to the given file
    """
    return open(file, 'w').write(content)

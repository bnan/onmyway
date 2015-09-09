import hashlib
import os
import json


def md5(string):
    return hashlib.md5(str(string)).hexdigest()


def list_to_csv(a):
    return ','.join(map(str, list(a)))


def remove_string_whitespace(string):
    return string.replace(' ', '')


def json_from_file(filename):
    return json.load(open(filename, 'r'))

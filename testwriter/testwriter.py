# -*- coding: utf-8 -*-

def tests_generator(slug, names):
    """
    Returns a string containing repetitive tests.

    :param str slug: Slug containing protoype test.
    :param list names: Names to be substituted into the slug.
    """
    tests = ""
    slug = slug.strip()

    for name in names:
        tests += slug.replace("%s", name)
        tests += "\n\n"

    return tests

def read_names(filename):
    """
    Returns names listed in specified file as list, stripped of whitespace.
    """
    with open(filename,"r") as f:
        names = [line.strip() for line in f]

    return names

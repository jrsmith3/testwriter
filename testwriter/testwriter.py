#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

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
    with open(filename, "r") as f:
        names = [line.strip() for line in f]

    return names

def read_slug(filename):
    """
    Returns the test slug found in specified filename.
    """
    with open(filename, "r") as f:
        slug = f.read()

    return slug

class main():
    """
    Class that always gets instantiated when program is run
    """

    def __init__(self):

        parser = argparse.ArgumentParser(description = "Easily generate similar unit test methods.")

        parser.add_argument("slug",
            help = "Path to file containing test slug.")
        parser.add_argument("names",
            help = "Path to file containing names to be substituted into test slug.")

        args = parser.parse_args()

        names = read_names(args.names)
        slug = read_slug(args.slug)

        print tests_generator(slug, names)

if __name__ == "__main__":
    main()

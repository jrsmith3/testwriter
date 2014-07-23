testwriter - A package to automate writing test methods

Unit tests can be repetitive. For example, say an object is instantiated with a dictionary with several keys. A comprehensive set of tests would include testing each case where the dictionary passed to `__init__` is missing one of its keys. These tests should be separate, but the code implementing each test will be nearly identical.

The `testwriter` module generates a set of tests from a single prototype test written in a file. This prototype test includes a special substring ("%s") which is replaced by each item in a user-provided list. In this way, the user only needs to provide a list and a prototype and the `testwriter` module generates all of the repetitive tests without the user haivng to copy-and-paste or search-and-replace.

This module features a command-line application that takes two arguments. The first is a text file containing the properly formatted slug. The second is a text file containing the list of names to be substituted into the slug, where each name is on a new line.

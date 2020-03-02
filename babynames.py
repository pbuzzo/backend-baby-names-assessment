#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse
import os


"""
Author: Patrick Buzzo
Assistance: Derek Barnes
"""


def extract_names(filename):
    """
    Given a single file name for babyXXXX.html, returns a single list starting
    with the year string followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    names = []
    names_dict = {}
    new_lst = []
    year = ''
    if filename == 'baby*.html':
        filename = '*'
    else:
        year = filename[4:8]
        filename = 'babies/' + filename
    if filename == '*':
        for i in os.listdir('babies/'):
            file_path = 'babies/' + i
            year = i[4:8]
            print(year)
            with open(file_path, "r") as f:
                for i in f.readlines():
                    if re.search(r'<td*?>(\d*)', i):
                        adding_str = ''
                        finder = re.search(r'<td*?>(\d*)', i)
                        baby_names = re.findall(r'<td*?>[A-Z]{1}\w*', i)
                        for i in baby_names:
                            adding_str = finder.group(1) + ' ' + i[4:]
                            names.append(adding_str)
                            adding_str = ''
            for i in names:
                k = i.split(' ')
                names_dict[k[1]] = k[0]
            for i in sorted(names_dict):
                new_lst.append((i + ' ' + names_dict[i]))
            for i in new_lst:
                print(i)
    else:
        with open(filename, "r") as f:
            for i in f.readlines():
                if re.search(r'<td*?>(\d*)', i):
                    adding_str = ''
                    finder = re.search(r'<td*?>(\d*)', i)
                    baby_names = re.findall(r'<td*?>[A-Z]{1}\w*', i)
                    for i in baby_names:
                        adding_str = finder.group(1) + ' ' + i[4:]
                        names.append(adding_str)
                        adding_str = ''
        for i in names:
            k = i.split(' ')
            names_dict[k[1]] = k[0]
        for i in sorted(names_dict):
            new_lst.append((i + ' ' + names_dict[i]))
        ret_str = year + '\n'
        for i in new_lst:
            ret_str += i + '\n'
        return ret_str

# extract_names('baby*.html')


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser(
        description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main(args):
    # Create a command-line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command-line arguments into a NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    file_list = ns.files

    # option flag
    create_summary = ns.summaryfile

    if create_summary:
        if file_list[0] == 'baby*.html':
            for i in os.listdir('babies/'):
                timing = extract_names(i)
                with open(i + '.summary', "w") as f:
                    f.write(timing)


if __name__ == '__main__':
    main(sys.argv[1:])

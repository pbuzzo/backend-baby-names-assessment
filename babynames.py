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
Assistance: Derek Barnes, Bryan Fernandez, Jake Hershey
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
    baby_list = []
    if filename == 'baby*.html':
        filename = '*'
    else:
        year = filename[4:8]
        filename = 'babies/' + filename
    if filename == '*':
        for i in os.listdir('babies/'):
            file_path = 'babies/' + i
            year = i[4:8]
            with open(file_path, "r") as f:
                year = re.findall(r'\d{4}', filename)
                new_lst.append(year[0])
                for i in f.readlines():
                    if re.search(r'<td*?>(\d*)', i):
                        adding_str = ''
                        finder = re.search(r'<td*?>(\d*)', i)
                        baby_names = re.findall(r'<td*?>[A-Z]{1}\w*', i)
                        for i in baby_names:
                            if i not in baby_list:
                                baby_list.append(i)
                                adding_str = finder.group(1) + ' ' + i[4:]
                                names.append(adding_str)
                                adding_str = ''
                            else:
                                continue
            for i in names:
                k = i.split(' ')
                names_dict[k[1]] = k[0]
            result = {}
            for key, value in sorted(names_dict.items()):
                if value not in result.values():
                    result[key] = value
            for k, v in sorted(result.items()):
                new_lst.append((k + ' ' + v))
        return new_lst
    else:
        with open(filename, "r") as f:
            year = re.findall(r'\d{4}', filename)
            new_lst.append(year[0])
            for i in f.readlines():
                if re.search(r'<td*?>(\d*)', i):
                    adding_str = ''
                    finder = re.search(r'<td*?>(\d*)', i)
                    baby_names = re.findall(r'<td*?>[A-Z]{1}\w*', i)
                    for i in baby_names:
                        if i not in baby_list:
                            baby_list.append(i)
                            adding_str = finder.group(1) + ' ' + i[4:]
                            names.append(adding_str)
                            adding_str = ''
                        else:
                            continue
        for i in names:
            k = i.split(' ')
            names_dict[k[1]] = k[0]
        result = {}
        for key, value in names_dict.items():
            # print(key)
            if key not in sorted(result.keys()):
                result[key] = value
        # print(sorted(result.keys()))
        for k, v in sorted(result.items()):
            new_lst.append((k + ' ' + v))
        return new_lst


extract_names('baby1990.html')


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
                extraction = extract_names(i)
                with open(i + '.summary', "w") as f:
                    for k in extraction:
                        f.write(k + '\n')
        else:
            for item in file_list:
                timing = extract_names(item)
                with open(item + '.summary', "w") as f:
                    for k in timing:
                        f.write(k + '\n')
    else:
        for item in file_list:
            answer = extract_names(item)
            text = '\n'.join(answer) + '\n'
            print(text[:-1])


if __name__ == '__main__':
    main(sys.argv[1:])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is used to run a CLI for interactively tagging metadata to the
specified source file
"""
from __future__ import print_function, with_statement
import os
import argparse
import subprocess

from tempfile import NamedTemporaryFile

__author__ = 'Jon Nappi'


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='The source file to be tagged')
    return parser.parse_args()


def pad_to_size(field, size):
    """Pad a field to the specified size. Once the field has been padded to the
    specified size, wrap it in square brackets and return it.
    """
    i = 0
    padded_field = field
    while len(padded_field) < size:
        if i % 2 == 0:
            padded_field = ' ' + padded_field
        else:
            padded_field += ' '
        i += 1
    return '[' + padded_field + ']:'


def build_tmp_file_content(fields, existing_data):
    """Build and return the data that will be initially written to the tempfile
    and presented to the user in the text editor of their choice
    """
    content = ''
    max_size = len(max(fields, key=len))
    for field in fields:
        padded_field = pad_to_size(field, max_size)
        if field in existing_data:
            padded_field = ' '.join([padded_field, existing_data[field]])
        content = '\n'.join([content, padded_field])
    return content


def parse_user_input(user_input):
    """Parse user input from temporary file into an
    :class:`~subler.tools.AtomCollection` for tagging
    """
    from subler.tools import AtomCollection

    metadata = AtomCollection()
    lines = user_input.split('\n')
    for line in lines:
        colon = line.find(':')
        key, val = line[:colon], line[colon+1:]
        if val.strip() != '':
            metadata[key[1:-1].strip()] = val.strip()
    return metadata


def main():
    """Main function for the pysubler cli"""
    from subler import Atom, Subler

    source = parse_args().source
    tagger = Subler(source)
    fields = list(Atom._valid_tags) + ['dest', 'chapters', 'delay',
                                       'chapters_preview', 'height', 'language',
                                       'remove', 'optimize', 'downmix',
                                       'rating', 'media_kind', 'explicit']
    existing = tagger.existing_metadata_collection
    content = build_tmp_file_content(fields, existing).strip()

    editor = os.environ.get('EDITOR', 'vim')  # default to vim

    temp = NamedTemporaryFile('w', suffix='.tmp')
    temp.write(content + '\n')
    temp.flush()
    subprocess.call([editor, temp.name])

    # Wait until changes are saved
    user_input = open(temp.name, 'r').read()
    metadata = parse_user_input(user_input)
    temp.close()

    tagger.metadata = metadata.atoms
    tagger.tag()


if __name__ == '__main__':
    main()

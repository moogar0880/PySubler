# -*- coding: utf-8 -*-
"""Tests for the :class:`subler.Atom` class"""
import unittest

import subler


class AtomTests(unittest.TestCase):
    """Basic unit level tests for the :class:`subler.Atom` class"""

    def setUp(self):
        self.valid_tags = subler.Atom._valid_tags

    def test_is_valid(self):
        """Assert that all valid tag names pass an Atom's validity check"""
        results = []
        for tag_name in self.valid_tags:
            atom = subler.Atom(tag=tag_name, value='Some Value')
            results.append(atom.is_valid())
        self.assertTrue(all(results))

    def test_invalid(self):
        """Assert that an invalid tag name fails an Atom's validity check"""
        atom = subler.Atom(tag='Fake Tag', value='Some Value')
        self.assertFalse(atom.is_valid())

    def test_data(self):
        """Validate the data output of a specific Atom"""
        fmt_str = '{%s:%s}'
        for tag_name in self.valid_tags:
            atom = subler.Atom(tag=tag_name, value='Some Value')
            self.assertEqual(atom.data, fmt_str % (tag_name, 'Some Value'))

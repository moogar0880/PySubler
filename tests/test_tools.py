# -*- coding: utf-8 -*-
"""Tests for the utilities found in the `subler.tools` module"""
import unittest

from copy import copy
from mock import patch

from subler import Atom
from subler.tools import AtomCollection, tag_dict

from .mocks import mock_tag


class AtomCollectionTests(unittest.TestCase):
    """Unit tests for :class:`subler.tools.AtomCollection`"""

    def setUp(self):
        """Create an AtomCollection instance and initialize some known data to
        work with
        """
        self.collection = AtomCollection()
        self.tags = ['TV Show', 'TV Episode $', 'Genre']
        self.values = ['Firefly', 1, 'Drama']
        self.data = tuple(zip(self.tags, self.values))

    def test_get(self):
        """Test AtomCollection's get method"""
        key, val = self.data[0]
        self.collection[key] = val
        self.assertEqual(self.collection.get(key), val)

    def test_get_default(self):
        """Test AtomCollection's get method with a provided default value"""
        key, expected = 'TV Show', 'Not Firefly'
        out = self.collection.get(key, expected)
        self.assertEqual(out, expected)

    def test_atoms(self):
        """Test AtomCollection's atoms property"""
        for key, val in self.data:
            self.collection[key] = val

        for atom in self.collection.atoms:
            self.assertIsInstance(atom, Atom)
            self.assertIn(atom.tag, self.tags)

    def test_items(self):
        """Test AtomCollection's items method"""
        for key, val in self.data:
            self.collection[key] = val

        for key, atom in self.collection.items():
            self.assertIn((key, atom), self.data)

    def test_getitem(self):
        """Test AtomCollection's __getitem__ method"""
        key, val = self.data[0]
        self.collection[key] = val
        self.assertEqual(self.collection.__getitem__(key), val)

    def test_setitem(self):
        """Test AtomCollection's __setitem__ method"""
        key, val = self.data[0]

        self.collection.__setitem__(key, val)
        self.assertEqual(self.collection[key], val)


class TagDictTests(unittest.TestCase):
    """Unit tests for the tag_dict function"""

    def setUp(self):
        """Initialize some known data to work with"""
        self.tags = ['TV Show', 'TV Episode #', 'Genre']
        self.values = ['Firefly', 1, 'Drama']
        self.metadata = dict(zip(self.tags, self.values))

        self.mock_path = 'subler.subler.Subler.tag'

    def test_tag_dict(self):
        """Test the tag_dict function creates the expected Subler instance"""
        source = '/Some/File/Path'
        media_kind = 'TV Show'
        with patch('subler.subler.Subler.tag', mock_tag):
            ret = tag_dict(self.metadata, source, media_kind=media_kind)

        for tag in [m.tag for m in ret.metadata]:
            self.assertIn(tag, self.tags)
        for val in [m.value for m in ret.metadata]:
            self.assertIn(val, self.values)
        self.assertEqual(ret.source, source)
        self.assertEqual(ret.media_kind, media_kind)

    def test_tag_dict_with_metadata(self):
        """Test that the tag_dict function properly curries a provided
        metadata list
        """
        source = '/Some/File/Path'
        media_kind = 'TV Show'
        tags, vals = copy(self.tags), copy(self.values)
        tags.append('Artist')
        vals.append('Firefly')

        atoms = Atom(tag='Artist', value='Firefly')

        with patch('subler.subler.Subler.tag', mock_tag):
            ret = tag_dict(self.metadata, source, media_kind=media_kind,
                           metadata=[atoms])

        for tag in [m.tag for m in ret.metadata]:
            self.assertIn(tag, tags)
        for val in [m.value for m in ret.metadata]:
            self.assertIn(val, vals)
        self.assertEqual(ret.source, source)
        self.assertEqual(ret.media_kind, media_kind)

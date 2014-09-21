# -*- coding: utf-8 -*-
"""A collection of tools to help ease the pain of tagging metadata"""
from .subler import Atom, Subler

__author__ = 'Jon Nappi'
__all__ = ['AtomCollection', 'tag_dict']


class AtomCollection(dict):
    """A dictionary collection of :class:`~subler.subler.Atom` instances. When a
    tag is added, the tag for it is used as the key to the dictionary, the value
    for which is an :class:`~subler.subler.Atom` instance. When you key back on
    an item already in the dictionary the value of that
    :class:`~subler.subler.Atom` is returned. Thus, if you know a key 'Artist'
    exists, you can get the value of that tag by doing
    ``my_collection['Artist']``
    """
    def get(self, k, d=None):
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        if k in self:
            return self[k]
        return d

    @property
    def atoms(self):
        """The list of :class:`~subler.subler.Atom`'s contained in this
        collection
        """
        return [super(AtomCollection, self).__getitem__(key) for key in self]

    def items(self):
        """ D.items() -> list of D's (key, value) pairs, as 2-tuples """
        items = []
        for tag in self:
            items.append((tag, self[tag]))
        return items

    def __getitem__(self, key):
        """Return the value of the :class:`~subler.subler.Atom` at *key*"""
        return super(AtomCollection, self).__getitem__(key).value

    def __setitem__(self, key, val):
        """Custom __setitem__ for entering :class:`~subler.subler.Atom`s based
        on *key*, *val*
        """
        super(AtomCollection, self).__setitem__(key, Atom(key, val))


def tag_dict(d, source, **kwargs):
    """Normally, you are only allowed to tag using a list of
    :class:`~subler.subler.Atom` objects. This function will allow you to
    provide a dict of metadata to be tagged via a :class:`~subler.subler.Subler`
    instance. Note: the same :class:`~subler.subler.Atom` limitations of valid
    tags will still apply

    :param d: A dict of Atom data
    :param source: The source file you wish to write the metadata to
    :param **kwargs: Any other keyword args you would like passed to
        :class:`~subler.subler.Subler`. Note: if you provide a 'metadata' field
        it will be merged with the data stored in *d*
    """
    atoms = []
    for key, val in d.items():
        atoms.append(Atom(key, val))

    # Edge case, but better safe than sorry
    if 'metadata' in kwargs:
        md = kwargs.pop('metadata', [])
        for atom in md:
            if isinstance(atom, Atom):
                atoms.append(atom)

    s = Subler(source, metadata=atoms, **kwargs)
    return s.tag()

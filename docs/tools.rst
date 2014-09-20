subler.tools module
===================

.. automodule:: subler.tools
    :members:
    :undoc-members:
    :show-inheritance:


Tools Examples
--------------
Below are some examples of how one might make use of the functions provided
within the tools module.

AtomCollection Examples
+++++++++++++++++++++++
:class:`~subler.tools.AtomCollection`'s can be used to store Atom data in a dict
representation.
::

    >>> from subler import Subler
    >>> from subler.tools import AtomCollection
    >>> metadata = AtomCollection()
    >>> metadata['TV Show'] = 'Firefly'
    >>> metadata['TV Episode #'] = 1
    >>> metadata['Genre'] = 'Drama'
    >>> s = Subler('/Users/Me/Movies/Firefly/S1/S1E1.m4v', media_kind='TV Show',
    ...            metadata=metadata.atoms)
    >>> s.tag()


tag_dict Examples
+++++++++++++++++
If you'd prefer to not deal with :class:`~subler.subler.Atom` instances or an
:class:`~subler.tools.AtomCollection` for managing your metadata, you can
optionally store your data in a stock Python *dict* instance and still easily
tag your metadata
::

    >>> from subler.tools import tag_dict
    >>> metadata = {'TV Show': 'Firefly', 'TV Episode #': 1, 'Genre': 'Drama'}
    >>> tag_dict(metadata, '/Users/Me/Movies/Firefly/S1/S1E1.m4v',
    ...          media_kind='TV Show')


.. PySubler documentation master file, created by
   sphinx-quickstart on Sun Sep 14 20:08:17 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

subler: The Unofficial Python-Subler Interface
==============================================

Release v\ |version|. (:ref:`Installation <install>`)

With the use of this module, it's now even easier to script the writing of iTunes
style metadata to your media files using the `SublerCLI <https://code.google.com/p/subler/wiki/SublerCLIHelp>`_.

Atoms
-----

To construct metadata you simply create a collection of Metadata Atoms like so,
::

    >>> artist = Atom('Artist', 'Linkin Park')
    >>> album = Atom('Album', 'Hybrid Theory')
    >>> metadata = [artist, album]

Tagging
-------
Then, you simply pass that through to a Subler instance and use the Subler tag
method, like so,
::

    >>> subler = Subler(path_to_source_file, dest=path_to_dest_file,
                        metadata=metadata)
    >>> subler.tag()

Contents:

.. toctree::
   :maxdepth: 4

   install
   subler
   tools
   cli
   utils


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


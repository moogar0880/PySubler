PySubler
========

Simple Python interface to the SublerCLI utility to make scripting metadata
tagging with `SublerCLI <https://code.google.com/p/subler/wiki/SublerCLIHelp>`_. even easier.

Atoms
-----

To construct metadata you simply create a collection of Metadata Atoms like
so,::

    >>> artist = Atom('Artist', 'Linkin Park')
    >>> album = Atom('Album', 'Hybrid Theory')
    >>> metadata = [artist, album]

Tagging
-------
Then, you simply pass that through to a Subler instance and use the Subler tag
method, like so,::

    >>> subler = Subler(path_to_source_file, dest=path_to_dest_file,
                        metadata=metadata)
    >>> subler.tag()


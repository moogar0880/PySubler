PySubler
========

.. image:: https://travis-ci.org/moogar0880/PySubler.svg
    :target: https://travis-ci.org/moogar0880/PySubler
    :alt: Travis CI Status

.. image:: https://coveralls.io/repos/moogar0880/PySubler/badge.svg
    :target: https://coveralls.io/r/moogar0880/PySubler
    :alt: Coverage

Simple Python interface to the SublerCLI utility to make scripting metadata
tagging with `SublerCLI <https://bitbucket.org/galad87/sublercli>`_. even easier.
Full documentation can be found on `Read The Docs <http://pysubler.readthedocs.org/en/latest/>`_.

Install
-------
Installing is as easy as
::

    $ pip install subler


Atoms
-----

To construct metadata you simply create a collection of Metadata Atoms like
so,
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


Interactive Tagging
-------------------
As of PySubler version 0.4.0 you can optionally use the `pysubler` command line
utility to interactively write metadata to your files. More information is provided
in the `Docs <http://pysubler.readthedocs.org/en/latest/>`_, but the gist of
interactive tagging is to run the `pysubler` cli like so
::

    $ pysubler /path/to/your/file.m4v

You will then be prompted with a template that you can fill in with all sorts of
provided metadata that will then be written to your file.


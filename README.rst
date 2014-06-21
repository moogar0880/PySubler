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


Valid Tag Table
^^^^^^^^^^^^^^^
Also probably worth noting is the list of valid Tag attributes and their types:

- Name
- Artist
- Album Artist
- Album
- Grouping
- Composer
- Comments
- Genre
- Release Date
- Track
- Disk
- Tempo
- TV Show
- TV Episode
- TV Network
- TV Episode ID
- TV Season
- Description
- Long Description
- Series Description
- Rating
- Studio
- Cast
- Director
- Codirector
- Producers
- Screenwriters
- Lyrics
- Copyright
- Encoding Tool
- Encoded By                      
- Keywords
- Category
- contentID
- artistID
- playlistID
- genreID
- composerID
- XID
- iTunes Account
- iTunes Account Type
- iTunes Country
- Track Sub- Title
- Song Description
- Art Director
- Arranger
- Lyricist
- Acknowledgement
- Conductor
- Linear Notes
- Record Company
- Original Artist
- Phonogram Rights
- Producer
- Performer
- Publisher
- Sound Engineer
- Soloist
- Credits
- Thanks
- Online Extras
- Executive Producer
- Sort Name
- Sort Artist
- Sort Album Artist
- Sort Album
- Sort Composer
- Sort TV Show
- Media Kind
- HD Video
- Gapless
- Artwork


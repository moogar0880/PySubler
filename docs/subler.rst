subler module
=============

.. automodule:: subler
    :members:
    :undoc-members:
    :show-inheritance:

subler
------

.. automodule:: subler.subler
    :members:
    :undoc-members:
    :show-inheritance:

Subler Examples
---------------
There are many permutations of ways that a user may arrange their metadata, so all
of those variations will not be covered here. However, several smaller examples
and examples highlighting the additional functionality of this module will be shown below

Basic Information Gathering
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The subler module can be used to access a variety of information about the specified
source file::

    >>> from subler import Subler
    >>> sub = Subler('/Users/Jon/Movies/Iron Man.m4v')
    >>> sub.tracks
    ['Track: 1, Video Track, 2:06:23:60, 208 kbit/s, H.264, 1280 x 720', 'Track: 2, Stereo, 2:06:23:60, 128 kbit/s, AAC, 2 ch']
    >>> sub.existing_metadata
    [Atom(tag='Rating', value='PG-13'), Atom(tag='Name', value='Iron Man'),...]
    >>> sub.version
    'version 0.19'

Although it's documented above, I'd like to specify that there is a distinct difference
between subler.version_info/__version__ and subler.Subler.version.
::

    >>> import subler
    >>> subler.version_info
    (0, 3, 0)
    >>> subler.__version__
    '0.3.0'

As shown above, subler.version_info and __version__ depict the version of this Python
package, while the subler instances version attribute (seen in the first example) is
actually the version information about your systems SublerCLI executable


Tagging an Audio File
^^^^^^^^^^^^^^^^^^^^^
This example will show how to tag an Audio file with a variety of different types
of metadata
::

    >>> from subler import Atom, Subler
    >>> atoms = []
    >>> artist = Atom('Artist', 'Linkin Park')
    >>> album = Atom('Album', 'Hybrid Theory')
    >>> track = Atom('Name', 'Papercut')
    >>> artwork = Atom('Artwork', '/path/to/artwork.jpg')
    >>> metadata = [artist, album, track, artwork]
    >>> tagger = Subler('/path/to/papercut.mp3', media_kind='Music',
                        explicit='Explicit', metadata=metadata)
    >>> tagger.tag

Tagging other Media Types
^^^^^^^^^^^^^^^^^^^^^^^^^
Tagging a Audiobook, Music Video, Movie, TV Show, Booklet, or Ringtone is
fundamentally no different than an audio file, you just need to remember to
explicity set the media_kind attribute for anything that isn't a Movie.

subler.utils module
-------------------
Although the functions contained in this util module will likely be less than
helpful to someone trying to use this module, their behavior is documented below

.. automodule:: subler.utils
    :members:
    :undoc-members:
    :show-inheritance:

Valid Tags
^^^^^^^^^^
Also probably worth noting is the list of valid Tag names as the official
documentation appears to be out of date:

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

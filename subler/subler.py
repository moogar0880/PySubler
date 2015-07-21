# -*- coding: utf-8 -*-
"""This module provides an easily scriptable interface to tagging an assortment
of media types including x264 video, AAC audio, and many others with iTunes
formatted metadata via the SublerCLI. By simply creating new metadata
:class:`Atom`'s and specifying any additionally desired variables in an
instance of :class:`Subler` you can quickly execute the tagging of metadata to
a specified file.
"""
import os
import logging
from collections import namedtuple

from .utils import subler_executable, get_output

__author__ = 'Jon Nappi'
__all__ = ['Atom', 'Subler']

_Atom = namedtuple('_Atom', ['tag', 'value'])


class Atom(_Atom):
    """A class representing a single metadata atom. It's important to note that
    if you attempt to use an invalid tag for this Atom it will not be used when
    actually tagging the media file via a :class:`Subler` instance.
    """
    _valid_tags = ('Artist', 'Album Artist', 'Album', 'Grouping', 'Composer',
                   'Comments', 'Genre', 'Release Date', 'Track #', 'Disk #',
                   'Tempo', 'TV Show', 'TV Episode #', 'TV Network',
                   'TV Episode ID', 'TV Season', 'Description',
                   'Long Description', 'Series Description', 'HD Video',
                   'Rating Annotation', 'Studio', 'Cast', 'Director',
                   'Gapless', 'Codirector', 'Producers', 'Screenwriters',
                   'Lyrics', 'Copyright', 'Encoding Tool', 'Encoded By',
                   'Keywords', 'Category', 'contentID', 'artistID',
                   'playlistID', 'genreID', 'composerID', 'XID',
                   'iTunes Account', 'iTunes Account Type', 'iTunes Country',
                   'Track Sub-Title', 'Song Description', 'Art Director',
                   'Arranger', 'Lyricist', 'Acknowledgement', 'Conductor',
                   'Linear Notes', 'Record Company', 'Original Artist',
                   'Phonogram Rights', 'Producer', 'Performer', 'Publisher',
                   'Sound Engineer', 'Soloist', 'Credits', 'Thanks',
                   'Online Extras', 'Executive Producer', 'Sort Name',
                   'Sort Artist', 'Sort Album Artist', 'Sort Album',
                   'Sort Composer', 'Sort TV Show', 'Artwork', 'Name',
                   'Rating', 'Media Kind')

    def is_valid(self):
        """Check that the data in this :class:`Atom` is valid"""
        return self.tag in self._valid_tags

    @property
    def data(self):
        """The Subler argument formatted version of this :class:`Atom`"""
        return '{%s:%s}' % (self.tag, self.value)


class Subler(object):
    """A Python interface to the SublerCLI that can be used to easily read
    from and write to a specified source file.
    """
    __executable = subler_executable()

    def __init__(self, source, dest=None, chapters=None, delay=None,
                 chapters_preview=False, height=None, language='English',
                 remove=False, optimize=True, downmix=False, rating=None,
                 media_kind='Movie', explicit=None, metadata=None):
        """Create a Subler tagging instance

        :param source: The source file to feed to Subler
        :param dest: The destination file to save any changes to
        :param chapters: A .txt file with chapter information
        :param chapters_preview: Boolean option to create an additional video
            track with the preview of the chapters. Used by iTunes and some
            other media clients.
        :param delay: The delay of the subtitle track in ms
        :param height: The pixel height of the subtitle track
        :param language: The language of the subtitle track (i.e. English)
        :param remove: Boolean flag for remove all existing subtitles tracks
        :param optimize: Boolean flag for optimizing the file by moving the
            moov atom at the begining and interleaving the samples
        :param downmix: downmix audio (mono, stereo, dolby, pl2) from the
            source file
        :param rating: A valid US, UK, or German content rating
        :param media_kind: The type of media represented by the source file.
            Valid values are Music, Audiobook, Music Video, Movie, TV Show,
            Booklet, or Ringtone
        :param explicit: The explicit-ness warning of the content in the source
            file. Valid values are: None, "Clean", and "Explicit"
        :param metadata: A list of :class:`Atom`'s to be applied to the source
            file as metadata
        """
        self.source = source
        if dest is None:
            dest = self._generate_dest()
        self.dest = dest
        self.chapters = chapters
        self.chapters_preview = chapters_preview
        self.delay = delay
        self.height = height
        self.language = language
        self.remove = remove
        self.optimize = optimize
        self.downmix = downmix
        self._rating = None
        self._explicit = None
        self._media_kind = None
        self.rating = rating
        self.media_kind = media_kind
        self.explicit = explicit
        self.metadata = metadata
        self._logger = logging.getLogger('subler.Subler')

    def _generate_dest(self):
        """Generate a destination file name for the provided source file. This
        function will increment a number to append to the file name in order to
        distinguish it from other copies of the same file name

        :return: The absolute path for the destination file
        """
        name, ext = os.path.splitext(self.source)
        counter = 1
        dest = name + ' ({})'.format(counter) + ext

        while os.path.exists(dest):
            counter += 1
            dest = name + ' ({})'.format(counter) + ext
        return dest

    @property
    def version(self):
        """The current version of your systems SublerCLI package"""
        cmd = [self.__executable, '-version']
        return get_output(cmd)

    @property
    def tracks(self):
        """A list of tracks found the source file"""
        cmd = [self.__executable, '-source', self.source, '-listtracks']
        return get_output(cmd).split('\n')

    @property
    def existing_metadata_raw(self):
        """The metadata currently contained in the source file"""
        cmd = [self.__executable, '-source', self.source, '-listmetadata']
        return get_output(cmd).split('\n')

    @property
    def existing_metadata(self):
        """Atom representations of the metadata currently contained in the
        source file
        """
        raw = self.existing_metadata_raw
        atoms = []
        for s in raw:
            key, val = s[:s.find(':')].strip(), s[s.find(':') + 1:].strip()
            atoms.append(Atom(key, val))
        return atoms

    @property
    def existing_metadata_collection(self):
        """AtomCollection representation of the metadata currently contained in
        the source file
        """
        from .tools import AtomCollection
        raw = self.existing_metadata_raw
        atoms = AtomCollection()
        for s in raw:
            key, val = s[:s.find(':')].strip(), s[s.find(':') + 1:].strip()
            atoms[key] = val
        return atoms

    @property
    def rating(self):
        """The content rating of the source file. Valid US content ratings are:
        Not Rated, G, PG, PG-13, R, NC-17, TV-Y, TV-Y7, TV-G, TV-PG, TV-14,
        TV-MA, and Unrated. Valid UK content ratings are: Not Rated, U, Uc, PG,
        12, 12A, 15, 18, R18, Exempt, Unrated, and Caution. Valid German
        content ratings are FSK 0, FSK 6, FSK 12, FSK 16, and FSK 18.
        """
        return self._rating
    @rating.setter
    def rating(self, new_rating):
        """We will only update the rating provided if *new_rating* is a valid,
        Subler-supported rating.
        """
        valid = ('Not Rated', 'G', 'PG', 'PG-13', 'R', 'NC-17', 'Unrated',
                 'TV-Y', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA', 'U', 'Uc',
                 '12', '12A', '15', '18', 'R18', 'Exempt', 'Caution', 'FSK 0',
                 'FSK 6', 'FSK 12', 'FSK 16', 'FSK 18')
        if new_rating in valid:
            self._rating = new_rating

    @property
    def media_kind(self):
        """The type of media encapsulated in the source file. Valid values are:
        Music, Audiobook, Music Video, Movie, TV Show, Booklet, or Ringtone
        """
        return self._media_kind
    @media_kind.setter
    def media_kind(self, new_media_kind):
        valid = ('Music', 'Audiobook', 'Music Video', 'Movie', 'TV Show',
                 'Booklet', 'Ringtone')
        if new_media_kind in valid:
            self._media_kind = new_media_kind

    @property
    def explicitness(self):
        """The explicit rating of the content in the source file. Valid explicit
        ratings are: None, "Clean", and "Explicit"
        """
        return self._explicit
    @explicitness.setter
    def explicitness(self, explicit_rating):
        """If we don't receive a valid Explicitness rating, we'll ignore it"""
        valid = (None, 'Clean', 'Explicit')
        if explicit_rating in valid:
            self._explicit = explicit_rating

    def tag(self):
        """Apply the specified metadata to the source file and output it to
        the specified destination file
        """
        cmd = [self.__executable, '-source', self.source]

        if self.dest:
            cmd += ['-dest', self.dest]
        self.metadata.append(Atom('Media Kind', self.media_kind))
        if self._rating is not None:
            self.metadata.append(Atom('Rating', self.rating))
        if self.explicitness:
            self.metadata.append(Atom('Content Rating', self.explicitness))
        tags = [atom.data for atom in self.metadata if atom.is_valid()]
        cmd += ['-metadata', ''.join(tags)]
        if self.optimize:
            cmd += ['-optimize']
        self._logger.debug(cmd)
        return get_output(cmd)

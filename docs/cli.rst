pysubler CLI
============
As of PySubler 0.4.0, PySubler ships with the `pysubler` commandline utility,
which provides an interactive manner through which you can easily edit the metadata
found within your media file, using nothing more than your favorite text editor!

From the commandline, simply run:
::

    $ pysubler /path/to/your/file.m4v

From there you will be provided a template file you can fill with whatever metadata
you want written to your media file. This template will also automatically populate
with any metadata currently in your media file. The template will look similar
to the following
::

    [       Artist      ]:
    [    Album Artist   ]:
    [       Album       ]:
    [      Grouping     ]:
    [      Composer     ]:
    [      Comments     ]:
    [       Genre       ]:
    [    Release Date   ]:
    [      Track #      ]:
    [       Disk #      ]:
    [       Tempo       ]:
    [      TV Show      ]:
    [    TV Episode #   ]:
    [     TV Network    ]:
    [   TV Episode ID   ]:
    [     TV Season     ]:
    [    Description    ]:
    [  Long Description ]:
    [ Series Description]:
    [      HD Video     ]:
    [ Rating Annotation ]:
    [       Studio      ]:
    [        Cast       ]:
    [      Director     ]:
    [      Gapless      ]:
    [     Codirector    ]:
    [     Producers     ]:
    [   Screenwriters   ]:
    [       Lyrics      ]:
    [     Copyright     ]:
    [   Encoding Tool   ]: HandBrake 0.9.9 2013051800
    ...

And by simply writing information similar to this
::

    [       Artist      ]: Firefly
    [    Album Artist   ]: Firefly
    [       Album       ]: Firefly, Season 1
    ...

The metadata you provided will be passed through to Subler and written to your
media file as soon as you save the file in your text editor.

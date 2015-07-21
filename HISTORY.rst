Release History
---------------
0.4.1 (2015-07-21)
++++++++++++++++++

* Fixed an issue with improperly escaping metadata for use with `subprocess.check_output`
* Added improved DEBUG logging for generated commands and their results
* Improved the default `Subler.dest` attibute to create a unique destination filename
* Added a collection of automated tests for Travis CI
* Added Travis CI support

0.4.0 (2014-09-20)
++++++++++++++++++

* Added subler.tools module
* Added subler.cli module which provides the interactive pysubler commandline tool
* Added subler.subler.Subler.existing_metadata_collection property
* Fixed bug with default Subler dest attribute

0.3.1 (2014-09-14)
++++++++++++++++++

* Bug fix to keep RTD happy

0.3.0 (2014-09-14)
++++++++++++++++++

* Addition of subler.utils module for utility functions
* More intuitive SublerCLI executable path discovery
* Added better shell escaping for SublerCLI arguments
* Fixed SublerCLI version property
* Fixed tracks property for outputting the track listings of the source file
* Subler existing_metadata property is now returned as a list of Atoms

0.2.0 (2014-06-21)
++++++++++++++++++

* Initial release

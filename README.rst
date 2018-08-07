#############
conlog
#############

|build-status| |license| |pypi-version|

Boilerplate-free Console Logging Module for Python


About
=====

*conlog* is a configurable console logging mechanism featuring:

- One-line setup per Logger
- Optional export to rotating log file
- Show additional information when debugging
- YAML or argument based configuration


Installation
============

Install via pip: **(Recommended)**
::

  pip install conlog

Or with setup_tools:
::

  python setup.py install


Documentation
=============

Quick start
-----------

Getting a Logger started with *conlog* is easy:
::

  import conlog
  log = conlog.start(level='INFO')
  log.info('Hello World!')


Functions
---------


start(...)
""""""""""

::

    start(
        yaml_file=None,
        log_file=None,
        log_format='%(asctime)22s - %(levelname)8s - %(name)20s - %(message)s',
        debug_format='%(asctime)22s - %(levelname)8s - %(name)20s - %(funcName)20s - %(message)s',
        level='INFO',
        max_file_size='5000000',
        max_retention=5
    )

Configure and return the root Logger instance. All arguments
are optional. If any argument is not supplied, its default
value is used. This means it is possible to run with no
arguments if default values are desired across all options.

Parameters
''''''''''

:``yaml_file``:
  Pull configurations from a YAML file. All arguments from
  ``start()`` are available as YAML options. Option entries
  should be nested under ``conlog`` at the root of the YAML
  file. The file should be structured:
  ::

      conlog:
        log_file: log/app.log
        log_format: '%(asctime)22s - %(levelname)8s - %(name)20s - %(message)s'
        debug_format: '%(asctime)22s - %(levelname)8s - %(name)20s - %(funcName)20s - %(message)s'
        level: INFO
        max_file_size: 5 MB
        max_retention: 5

  Like ``start()`` arguments, all YAML settings are optional.
  If any setting is not supplied in the configuration, its
  default value is used.

  **NOTE:** If ``yaml_file`` is supplied, its values are processed
  first, and will be overridden by any additional arguments
  supplied in ``start()``.

  Default: ``None``


:``log_file``:
  Path to log file. By default, file logging is disabled. If
  ``log_file`` is set to a file path, for example, ``log/app.log``,
  it will enable rotating file logging.

  **NOTE:** In the example ``log/app.log``, the log file itself,
  ``app.log``, does not need to exist; however, the base directory
  ``log`` MUST exist.

  By default, the log file will rotate when it reaches *5 MB*, with up
  to *5* rotations being kept before overwriting the oldest file.
  These values can be adjusted using the ``max_file_size`` and
  ``max_retention`` options.

  Default: ``None``


:``log_format``:
  Logging format for all levels **EXCEPT** ``DEBUG``.

  Default: ``%(asctime)22s - %(levelname)8s - %(name)20s - %(message)s``


:``debug_format``:
  Logging format for only the ``DEBUG`` level. By default, this
  displays the same formatting as ``log_format``, but with an
  additional column for the name of the function writing to the
  Logger.

  Default: ``%(asctime)22s - %(levelname)8s - %(name)20s - %(funcName)20s - %(message)s``


:``level``:
  Logging level. Only messages sent to this level or higher will
  appear in log.

  Default: ``INFO``


:``max_file_size``:
  Maximum log file size before rollover. This value can either
  be an integer byte size or a proper string like: ``5 MB``,
  ``50 kB``, etc. Setting to ``0`` will cause the log file to
  grow infinitely with no rollover.
  
  This option has no impact if ``log_file`` is set to ``None``.

  Default: ``5000000`` (5 MB)


:``max_retention``:
  Maximum number of rollover logs to keep. Rotated logs will be
  saved in the format ``log_name.1``, ``log_name.2``, etc.,
  until ``max_retention`` is reached. At that point the oldest
  of the rollover logs will be purged.
  
  This option has no impact if ``log_file`` is set to ``None``,
  or if ``max_file_size`` is set to ``0``.

  Default: ``5``

----

new(inst)
"""""""""

Get a new Logger instance. Recommended usage is
``self.log = conlog.new(self)`` from the ``__init__`` method of
the calling class.

Parameters
''''''''''

:``inst``:
  **Required** - Instance of the class which new Logger is for,
  (Typically use ``self``)


Examples
========

This is the easiest way to add a root Logger using conlog with ``INFO`` level
logging to the console.
::

  log = conlog.start(level='INFO')

----

Start logging based on configuration in the YAML file, ``conf/conlog.yml``.
::

  log = conlog.start(yaml_file='conf/conlog.yml')

----

Start ``DEBUG`` level Logger with console logging and rotating file logging to
``logs/app.log``.
::

  log = conlog.start(
          log_file='logs/app.log',
          level='DEBUG'
  )
  
----

Similar to above but with specific values set for rotation of log files. This
will rotate the log file when it reaches ``1 MB`` and retain up to ``10``
archived log files before overwriting the oldest.
::

    log = conlog.start(
            log_file='log/app.log',
            level='INFO',
            max_file_size='1 MB',
            max_retention=10,
    )

----

Start console logging with a different log format.
::

    log = conlog.start(log_format='%(levelname)s:%(name)s:%(message)s')

----

Get a Logger instance for a class. In this example, a root Logger
has already been set up by *start()* in the main function of the
program.
::

    class Example(object):
        def __init__(self):
            self.log = conlog.new(self)


Author
======
* Ryan Miller - ryan@devopsmachine.com

.. |build-status| image:: https://img.shields.io/travis/RyanMillerC/conlog.svg?branch=master
    :alt: Build Status
    :scale: 100%
    :target: https://travis-ci.org/RyanMillerC/conlog

.. |license| image:: https://img.shields.io/github/license/ryanmillerc/conlog.svg
    :alt: License
    :scale: 100%
    :target: https://github.com/RyanMillerC/conlog/blob/master/LICENSE.txt

.. |pypi-version| image:: https://img.shields.io/pypi/v/conlog.svg
    :alt: PyPi Version
    :scale: 100%
    :target: https://pypi.org/project/conlog

#############
clogging
#############

clogging - Configurable Logging Boilerplate for the Autologging Module. 

About
************

Autologging (https://github.com/mzipay/Autologging) is an awesome module for
automatic logging in Python; however, it's not completely boilerplate free.

This module, clogging, addresses tasks that I would otherwise need to address
per application I build.

It features:

* Complete setup of a complex root Logger instance with a single call
* Configurable logging through YAML configuration or through keyword args
* Detailed output columns for lower logging levels
* Surpressed output columns for higher logging levels
* Optional rotating file handler

A demo "Hello World" application using clogging/autologging is available here,
    https://github.com/RyanMillerC/DemoCloggingApp

*Technically clogging could be used to configure the standard Python
logging module, since this doesn't directly interact with autologging,
but it was specifically created to fill in gaps and save me time
building applications that use autologging.*

Installation
************
 
::

  pip install clogging


Documentation
*************

Import this module with:
::

  import clogging

These are the two functions which will start logging.

start_from_yaml
~~~~~~~~~~~~~~~

Usage:
::

  log = clogging.start_from_yaml('path/to/file.yaml')

Start logging based on entries in a YAML configuration file. This is
designed to work with an existing application settings.yaml file, but
does not have to have anything additional for your application inside
it. All clogging entries should be nested under 'clogging' at the root
of the YAML file. If this is unclear, look at the example in the demo
application mentioned previous in this document.

This function returns a root Logger instance.

Your YAML file, at it's root level, should be structured like,
::


    clogging:
      file: log/app.log
      format: '%(asctime)22s - %(levelname)8s - %(name)20s - %(message)s'
      format_ext: '%(asctime)22s - %(levelname)8s - %(name)20s - ' \
              '%(funcName)20s - %(message)s'
      level: INFO
      max_file_size: 5 MB
      max_retention: 5
      verbose_levels: ['TRACE', 'DEBUG']
    app:  // Application or other configurations not nessesary, shown
      ... // as example only
    ...

All settings are optional. If you fail to supply one or more of the
settings in the YAML file, default settings will be used.

For a list of available options and defaults, see the Options section below.

start_from_yaml does require that you have at least a "clogging" section
in your YAML file. To use clogging without a YAML file, use start_from_args.

start_from_args
~~~~~~~~~~~~~~~

Usage:
::

    log = clogging.start_from_args(
            file="log/app.log",
            format="%(asctime)22s - %(levelname)8s - %(name)20s - %(message)s",
            format_ext: "%(asctime)22s - %(levelname)8s - %(name)20s - " \
                        "%(funcName)20s - %(message)s",
            level=INFO,
            max_file_size="5 MB",
            max_retention=5,
            verbose_levels=['TRACE', 'DEBUG']
    )


Start logging based on keyword arguments. This function will accept the
same options as start_from_yaml, but passed in to the function as
keyword arguments.

This function returns a root Logger instance.

All settings are optional. If you fail to supply one or more of the
options in the YAML file, default settings for those options will be
used. It is even possible to run with no options set. In that case the
default settings would be used for every option.

For a list of available options and defaults, see the Options
section below.

This example is the easiest way to add clogging into a project and start
INFO level logging to the console,
::

  log = clogging.start_from_args(level='INFO')

Or, another example to start DEBUG level logging with a rotating file handler,
::

  log = clogging.start_from_args(
          file='logs/app.log',
          level='DEBUG'
  )


Options
~~~~~~~

The following are available options and their descriptions. If any of
these options are not supplied, the default value will be used. These
option names can be set in either YAML format or as arguments to
start_from_args.

:file:
  Path to log file. By default, file logging is disabled. If 'file' is set to a
  file path, for example, 'log/app.log', it will enable rotating file logging. 

  Note: In the example 'log/app.log', the log file itself, 'app.log', does not
  need to exist; however, the base directory 'log' MUST exist. 
  
  By default the log file will rotate when it reaches 5 MB, with up to 5
  rotations being kept before overwriting the oldest. These values can be
  configured using 'max_file_size' and 'max_retention'.

  Default: None

:format:
  Logging format for all non-verbose levels. By default non-verbose is
  considered to be INFO and higher.

  Default: '%(asctime)22s - %(levelname)8s - %(name)20s - %(message)s'

:format_ext:
  Logging format for all verbose levels. By default this is considered
  to be DEBUG and TRACE levels. Additional levels can be added to use this
  format in 'verbose_levels'.
  
  Default: '%(asctime)22s - %(levelname)8s - %(name)20s - %(funcName)20s - %(message)s'

:level:
  Logging level.

  Default: 'INFO'

:max_file_size:
  Maximum log file size before rollover. This value can either be an integer
  bytes size or a proper string like: "5 MB", "50 kB", etc. Setting to 0
  will cause the log file to grow infinitely with no rollover. This option has
  no impact if 'file' is set to None.

  Default: '5 MB'

:max_retention:
  Maximum number of rolled over logs to keep. Logs will be saved as log.1,
  log.2, ...etc., until max_retention is reached. At that point the oldest of
  the rollover logs will be cleared. This option has no impact if 'file' is set
  to None, or if 'max_file_size' is set to 0.

  Default: 5

:verbose_levels:
  Logging levels in this list are considered verbose levels and will use
  format_ext for formatting. This is typically done to follow low
  level logs which show funcName alongside name.
  
  Default: ['TRACE', 'DEBUG']

Author
************
* Ryan Miller - ryan@devopsmachine.com

python3-pam
===========

An interface to the Pluggable Authentication Modules (PAM) library on linux,
written in pure python (using ctypes)

Overview
--------

This module provides an ``authenticate`` function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

Usage
-----

Import the ``authenticate`` function, and use it as follows:

    authenticate(username, password, service)

The ``service`` argument specifies the PAM service to authenticate against.
Defaults to ``login``.

License
-------

The [original module](http://atlee.ca/software/pam/) was written by Chris AtLee,
see the original copyright notice:

    Copyright (C) 2007-2009 Chris AtLee <chris@atlee.ca>.
    Licensed under the MIT license. 

Modifications 2013 by Leon Weber <leon@leonweber.de>:
* Ported to Python3

This module is licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php).

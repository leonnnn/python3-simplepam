python3-simplepam
=================

An interface to the Pluggable Authentication Modules (PAM) library on linux,
written in pure python (using ctypes)

Overview
--------

This module provides an ``authenticate`` function that allows the caller to
authenticate a given username / password against the PAM system on Linux.

Usage
-----

Run ``python3 setup.py install`` as root to install the module, then import the
``authenticate`` function, and use it as follows:

```python
    from simplepam import authenticate
    authenticate(username, password, service)
```

The full function signature is as follows:

```python
    authenticate(username, password, service='login', encoding='utf-8',
                 resetcred=True)
```

The ``service`` argument specifies the PAM service to authenticate against.
Defaults to ``login``.

``username``, ``password`` and ``service`` can be given as strings or bytes. If
they are strings, they will be encoded using the encoding given by the
``encoding`` parameter, or, if omitted, as UTF-8.

The function returns ``True`` if the authentication succeeds and returns
``False`` if authentication fails (or if PAM returns an error (FIXME)).

Python version
--------------
Despite its name, this module works with both Python 2 and Python 3.

License
-------

The [original python-pam module](http://atlee.ca/software/pam/) was written by
Chris AtLee, see the original copyright notice:

    Copyright (C) 2007-2009 Chris AtLee <chris@atlee.ca>.
    Licensed under the MIT license. 

Modifications 2013-2014 by Leon Weber <leon@leonweber.de>:
* Ported to Python3
* Add call to ``pam_end()``
* Use ``ctypes.byref()`` instead of ``ctypes.pointer()`` to pass arguments by reference
* Properly handle encoding of password, username and service (Patch by Sebastian
  Riese)
* Add call to ``pam_reset()`` (Patch by Lertsenem)
* Re-add Python2 support (Patch by Victor Stinner of eNovance)

This module is licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php).

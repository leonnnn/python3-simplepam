from distutils.core import setup

desc = (
    'An interface to the Pluggable Authentication Modules (PAM) library '
    'on linux, written in pure python (using ctypes)'
)

setup(name='simplepam', version='0.1.5',
      description=desc,
      py_modules=['simplepam'],
      author='Leon Weber <leon@leonweber.de>, Chris AtLee <chris@atlee.ca>',
      author_email='leon@leonweber.de',
      url='https://github.com/leonnnn/python3-simplepam',
      license='MIT'
      )

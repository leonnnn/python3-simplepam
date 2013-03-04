from distutils.core import setup

desc = (
    'An interface to the Pluggable Authentication Modules (PAM) library'
    'on linux, written in pure python (using ctypes)'
)

setup(name='python3-pam', version='0.1.4alpha',
      description=desc,
      py_modules=['pam'],
      author='Leon Weber <leon@leonweber.de>, Chris AtLee <chris@atlee.ca>',
      author_email='leon@leonweber.de',
      url='https://github.com/leonnnn/python3-pam',
      license='MIT'
      )

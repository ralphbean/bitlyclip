from setuptools import setup, find_packages
import sys, os

version = '0.2.2'

setup(name='bitlyclip',
      version=version,
      description="bit.ly-fy a url in the X clipboard",
      long_description="""
      `bitlyclip` is just a script that:

        - takes a url in your clipboard
        - bitly-ifies it
        - puts the new url back in your clipboard

      It makes a nice 'hotkey' in whatever window manager you're using.

      If you have notify-python installed, it will
      pop up nice messages for you.

        - http://www.galago-project.org/downloads.php

      You'll need to have ``xsel`` on your system::

        $ sudo yum -y install xsel

      To install bitlyclip itself:  ``$ pip install bitlyclip``

      To use: ``$ bitlyclip``
      """,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Text Processing :: General',
      ],
      keywords='',
      author='Ralph Bean',
      author_email='rbean@redhat.com',
      url='http://github.com/ralphbean/bitlyclip',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'bitlyapi',
      ],
      entry_points="""
      [console_scripts]
      bitlyclip = bitlyclip:cmd
      """,
     )

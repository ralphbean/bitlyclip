from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='bitlyclip',
      version=version,
      description="bitly-fy a url in the linux clipboard",
      long_description="",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Text Processing :: General',
      ],
      keywords='',
      author='Ralph Bean',
      author_email='ralph.bean@gmail.com',
      url='http://github.com/ralphbean/bitlyclip',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=['scripts/bitlyclip',],
      install_requires=[
          'bitlyapi',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
     )

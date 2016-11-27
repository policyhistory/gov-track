import os
from setuptools import setup

# Arguments to setup function.
pkgname = 'govtrack'
authors = [
'Jeffrey Bouas',
          ]
author_emails = [
'jd.bouas@gmail.com',
               ]
url = 'https://github.com/policyhistory/govtrack'
readme = 'README.md'

# Dependencies
dependencies = [
'requests',
'beautifulsoup4',
]

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
  VERSIONFILE = os.path.join(pkgname, '__init__.py')
  initfile_lines = open(VERSIONFILE, 'rt').readlines()
  VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
  for line in initfile_lines:
    mo = re.search(VSRE, line, re.M)
    if mo:
      return mo.group(1)
  raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))

def get_str_list(strlist):
  return ', '.join(strlist)

def get_authors():
  return get_str_list(authors)

def get_author_emails():
  return get_str_list(author_emails)

setup(
  name = pkgname,
  version = get_version(),
  author = get_authors(),
  author_email = get_author_emails(),
  description = ("A government website parsing toolbox."),
  license = "GPLv3",
  url = url,
  packages = ['govtrack'],
  install_requires = dependencies,
  long_description = read(readme),
)

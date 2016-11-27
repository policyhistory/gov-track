from bs4 import BeautifulSoup
from Resource import Resource

class PageParser(object):
  def __init__(self, html, domain=None):
    self.html = BeautifulSoup(html, "html.parser")
    self.domain = domain

  def local_resource_links(self):
    hardlinks = dict()
    for link in self.html.find_all('a'):
      tar = link.get('href')
      # Skip <a> tags that aren't links.
      if tar is None: continue
      include = True
      # Skip javascript code.
      if 'javascript' in tar:
        include = False
      # Skip external links.
      if 'http://' in tar or 'https://' in tar:
        include = False
      # Skip links to other parts of the same page
      if tar[0] == '#':
        include = False
      # Go to the next link if we don't include it.
      if not include:
        continue
      # Split off parameters.
      params = None
      if '?' in tar:
        parts = tar.split('?')
        tar = parts[0]
        params = parts[1].split('&') if len(parts) > 1 else None
      # Go to the next link if stripping parameters left us with nothing.
      if len(tar) < 1 or tar == '/':
        continue
      hardlinks[tar] = True if params is None else params
    links = list()
    for link in list(hardlinks.keys()):
      links.append(
        Resource(domain=self.domain, path=link,
                 parameters = (hardlinks[link] if hardlinks[link] is not True \
                                               else None))
      )
    return links

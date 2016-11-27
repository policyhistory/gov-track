class Resource(object):
  def __init__(self, path=None, domain=None, parameters=None, protocol=None):
    self.domain = domain
    self.parameters = parameters
    self.path = path
    self.protocol = protocol

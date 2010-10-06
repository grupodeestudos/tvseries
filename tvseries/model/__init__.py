


__all__ = ['Serie', 'Episode']

class Serie(object):
  name = None
  episodes = None

  def __init__(self, name=None, episodes=[]):
    self.name = name
    self.episodes = episodes


class Episode(object):
  name = None
  number = 0

  def __init__(self, name, number):
    self.name = name
    self.number = number

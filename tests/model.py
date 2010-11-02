


import unittest
from tvseries.model import Serie, Episode

class SerieTest(unittest.TestCase):


  def test_get_last_episode_empty_serie(self):
    s = Serie(name="dexter", episodes=[Episode(name="s01e02"), Episode(name="s01e05")])

    self.assertEquals("s01e05", s.last_episode().name)

  def test_get_last_episode(self):
    s = Serie(name="dexter")
    self.assertEquals("s01e00", s.last_episode().name)


class EpisodeTest(unittest.TestCase):


  def test_next_episode(self):
    e = Episode(serie=Serie(name="dexter"), name="s01e08")
    self.assertEquals("s01e09", e.next().name)
    self.assertEquals("dexter", e.next().serie.name)

  def test_next_episode_invalid_episode_name(self):
    e = Episode(serie=Serie(name="dexter"), name="s01eab")
    self.assertEquals(None, e.next())

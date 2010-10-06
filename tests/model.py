


import unittest

from tvseries.model import Serie, Episode


class ModelTest(unittest.TestCase):
  

  def test_model_serie_init_with_name(self):
    serie = Serie(name="dexter")
    self.assertEquals("dexter", serie.name)
    self.assertEquals([], serie.episodes)

  def test_model_serie_init(self):
    serie = Serie()
    self.assertEquals(None, serie.name)
    self.assertEquals([], serie.episodes)

  def test_model_episode(self):
   ep = Episode("Pilot", 1)
   self.assertEquals("Pilot", ep.name)
   self.assertEquals(1, ep.number)
    

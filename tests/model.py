
# encoding: utf-8

import unittest

from tvseries.model import Serie, Episode
import tvseries.db

import mock

class ModelTest(unittest.TestCase):
  

  def test_model_serie_init_with_name(self):
    serie = Serie(name="dexter")
    self.assertEquals("dexter", serie.name)
    self.assertEquals([], serie.episodes)

  def test_model_serie_init(self):
    serie = Serie()
    self.assertEquals(None, serie.name)
    self.assertEquals([], serie.episodes)

  def test_model_serie_return_values(self):
    s = Serie("house")
    self.assertEquals(["house"], s.return_values())

  def test_model_serie_column_names(self):
    s = Serie("dex")
    self.assertEquals(["name"], s.columns())

  def test_model_episode(self):
   ep = Episode("Pilot", 1)
   self.assertEquals("Pilot", ep.name)
   self.assertEquals(1, ep.number)

  @mock.patch.object(tvseries.db, "get_connection")
  def test_save_serie(self, get_conn_mock):
    connectionMock = mock.Mock()
    get_conn_mock.return_value = connectionMock
    s = Serie("dexter")
    s.save()

    self.assertTrue(connectionMock.execute.called, "Não chamou o método execute()")
    self.assertTrue(connectionMock.commit.called)
    self.assertTrue(connectionMock.close.called)
    connectionMock.execute.assert_called_with("insert into series (name) values (?)", "dexter")

  def test_model_episode_return_values(self):
    e = Episode("Pilot", 3)
    self.assertEquals(["Pilot", 3], e.return_values())

  def test_model_episode_columns(self):
    e = Episode("Ep04", 4)
    self.assertEquals(["name", "number"], e.columns())

  @mock.patch.object(tvseries.db, "get_connection")
  def test_save_episode(self, get_conn_mock):
    connectionMock = mock.Mock()
    get_conn_mock.return_value = connectionMock
    e = Episode("Pilot", 4)
    e.save()

    self.assertTrue(connectionMock.execute.called, "Não chamou o método execute()")
    self.assertTrue(connectionMock.commit.called)
    self.assertTrue(connectionMock.close.called)
    connectionMock.execute.assert_called_with("insert into episodes (name, number) values (?, ?)", "Pilot", 4)



    

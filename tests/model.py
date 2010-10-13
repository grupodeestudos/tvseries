
# encoding: utf-8

import unittest

from tvseries.model import Serie, Episode
from ludibrio import Mock

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

  def test_save_serie(self):
    with Mock() as get_connection:
      from tvseries.db import get_connection
      conn = get_connection()
      cursor= conn.cursor()
      cursor.execute("insert into series (name) values (?)", ("dexter",))
      cursor.commit()
      conn.close()

    s = Serie("dexter")
    s.save()
    get_connection.validate()

  def test_model_episode_return_values(self):
    e = Episode("Pilot", 3)
    self.assertEquals(["Pilot", 3], e.return_values())

  def test_model_episode_columns(self):
    e = Episode("Ep04", 4)
    self.assertEquals(["name", "number"], e.columns())

  def test_save_episode(self):
    with Mock() as get_connection:
      from tvseries.db import get_connection
      c = get_connection()
      cursor = c.cursor().execute('insert into episodes (name, number) values (?, ?)', ('Pilot', 4))
      cursor.commit()
      c.close()

    e = Episode("Pilot", 4)
    e.save()
    get_connection.validate()


  def test_model_list_all_com_filtro(self):
    with Mock() as get_connection:
      from tvseries.db import get_connection
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("select * from series where name = '?'", "dexter")
      cursor.fetchall()
      conn.close()
    
    s = Serie("dexter")
    s.all()
    get_connection.validate()

  def test_model_list_all_sem_filtro(self):
    with Mock() as get_connection:
      from tvseries.db import get_connection
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("select * from series")
      cursor.fetchall()
      conn.close()
 
    s = Serie()
    s.all()
    get_connection.validate()


    

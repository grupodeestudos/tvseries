
import tvseries.db


__all__ = ['Serie', 'Episode']


class Entity(object):


  def save(self):
    table = self.__class__.__name__.lower() + "s"
    column_values = self.return_values()
    values = ['?' for v in column_values]

    sql = "insert into %s (%s) values (%s)" %\
                                            (table,\
                                             ", ".join(self.columns()),\
                                             ", ".join(values))
    
    conn = tvseries.db.get_connection()

    conn.execute(sql, *column_values)
    conn.commit()
    conn.close()


  def all(self):
    table = self.__class__.__name__.lower() + "s"
    sql = "select * from %s" % table
    params = []

    if (self.name):
      sql += " where name = '?'"
      params += [self.name]

    conn = tvseries.db.get_connection()
    r = conn.execute(sql, *params)
    
    r = r.fetchall()
    conn.close()
    return r


  def return_values(self):
    pass
  
  def columns(self):
    pass


class Serie(Entity):
  name = None
  episodes = None

  def __init__(self, name=None, episodes=[]):
    self.name = name
    self.episodes = episodes
  
  def return_values(self):
    return [self.name]
  
  def columns(self):
    return ["name"]


class Episode(Entity):
  name = None
  number = 0

  def __init__(self, name, number):
    self.name = name
    self.number = number


  def return_values(self):
    return [self.name, self.number]

  def columns(self):
    return ["name", "number"]

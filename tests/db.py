

import unittest

from ludibrio import Mock
import tvseries.db

class DbTest(unittest.TestCase):

  def test_db_get_conection(self, *args):
    tvseries.db.PATH = "/tmp/db.sqlite3"
    with Mock() as connect:
      from sqlite import connect
      c = connect("/tmp/db.sqlite3")

    tvseries.db.get_connection()
    connect.validate()

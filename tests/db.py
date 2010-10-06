

import unittest
from mock import Mock
import sqlite3

import tvseries.db



class DbTest(unittest.TestCase):

  def test_db_get_conection(self):
    sqlite3.connect = Mock()
    c = tvseries.db.get_connection()
    self.assertTrue(sqlite3.connect.called)
    self.assertEquals(sqlite3.connect.call_args, ((tvseries.db.PATH,), {}))

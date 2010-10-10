

import unittest
from mock import Mock, sentinel
import mock
import sqlite3

import tvseries.db



class DbTest(unittest.TestCase):

  @mock.patch.object(sqlite3, "connect")
  def test_db_get_conection(self, *args):
    tvseries.db.get_connection()
    self.assertTrue(sqlite3.connect.called)
    self.assertEquals(sqlite3.connect.call_args, ((tvseries.db.PATH,), {}))

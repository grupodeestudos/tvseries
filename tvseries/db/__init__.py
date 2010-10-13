
import os

try:
  import sqlite3 as sqlite
except Exception, e:
  import sqlite



PATH = os.path.expanduser("~dalton/tvseries.db.sqlite3")

def get_connection():
  return sqlite.connect(PATH)

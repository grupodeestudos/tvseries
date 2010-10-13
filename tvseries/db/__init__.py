
import os
import sqlite



PATH = os.path.expanduser("~dalton/tvseries.db.sqlite")

def get_connection():
  return sqlite.connect(PATH)

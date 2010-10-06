

import os
import sqlite3

PATH = "/tmp/db.sqlite3"

def get_connection():
  return sqlite3.connect(PATH)

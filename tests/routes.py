
import unittest

import tvseries.routes
from pyroutes.http.request import Request

from ludibrio import Mock

class RoutesTest(unittest.TestCase):
  
  def setUp(self):
    tvseries.db.PATH = "/tmp/db.sqlite3"

  def test_index_route(self):
    with Mock() as Redirect:
      from pyroutes.http.response import Redirect
      Redirect("/series")

    tvseries.routes.index(Request({}))
    Redirect.validate()

  def test_list_series(self):
    with Mock() as get_connection:
      from tvseries.db import get_connection
      c = get_connection()
      crs = c.cursor()
      crs.execute("select name from series") 
      crs.fetchall() >> [("dexter",), ("house",)]
      crs.execute("select name from episodes where serie = 'dexter' order by name")
      crs.fetchall() >> [("s05e01",), ("s05e02",)]
      crs.execute("select name from episodes where serie = 'house' order by name")
      crs.fetchall() >> []


    with Mock() as render_to_response:
      from tvseries.templates import render_to_response
      render_to_response('series.html', data={'series': ['dexter', 'house'], 
                                                 'episodes': {
                                                     'house': [], 
                                                     'dexter': ['s05e01', 's05e02']
                                                    }
                                             })

    tvseries.routes.series(Request({}))
    get_connection.validate()
    render_to_response.validate()


#  def test_new_serie(self):
#    with Mock() as Serie:
#      from tvseries.model import Serie
#      a = Serie("dexter")
#      a.save()
#
#    tvseries.routes.new_serie(Request({'PATH_INFO': "/dexter"}))
#    Serie.validate()


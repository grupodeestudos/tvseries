
import unittest

import tvseries.routes
from pyroutes.http.request import Request

from ludibrio import Mock

class RoutesTest(unittest.TestCase):
  

  def test_index_route(self):
    with Mock() as Redirect:
      from pyroutes.http.response import Redirect
      Redirect("/series")

    tvseries.routes.index(Request({}))
    Redirect.validate()

  def test_list_series(self):
    with Mock() as Serie:
      from tvseries.model import Serie
      Serie().all() >> [1, 2, 3]

    with Mock() as render_to_response:
      from tvseries.templates import render_to_response
      render_to_response('series.html', data=[1,2,3])

    tvseries.routes.series(Request({}))
    Serie.validate()
    render_to_response.validate()

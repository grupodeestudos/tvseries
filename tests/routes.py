
import unittest

import tvseries.routes
from pyroutes.http.request import Request

from ludibrio import Mock

class RoutesTest(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_index_route(self):
    with Mock() as full_path_redirect:
      from tvseries import full_path_redirect
      full_path_redirect({}, "/series") >> "/series"
    with Mock() as Redirect:
      from pyroutes.http.response import Redirect
      Redirect("/series")

    tvseries.routes.index(Request({}))
    Redirect.validate()
    full_path_redirect.validate()

  def test_list_series(self):

    with Mock() as Serie:
      from tvseries.model import Serie
      s = Serie.query.order_by(Serie.name).all() >> ["dexter", "house"]


    with Mock() as render_to_response:
      from tvseries.templates import render_to_response
      render_to_response('series.html', data={'series':["dexter", "house"]})

    tvseries.routes.series(Request({}))
    Serie.validate()
    render_to_response.validate()


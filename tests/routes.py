
import unittest
import mock
import pyroutes.http.response


class RoutesTest(unittest.TestCase):
  

  @mock.patch.object(pyroutes.http.response, "Redirect")
  def test_index_route(self, mock):
    import tvseries.routes
    from pyroutes.http.request import Request

    tvseries.routes.index(Request({}))
    mock.assert_called_with("/series")

  @mock.patch.object(pyroutes.http.response, "Response")
  def test_list_series(self, response_mock):
    self.fail()

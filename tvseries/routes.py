



from pyroutes import route
from pyroutes.http.response import Redirect, Response

from tvseries.model import Serie
from tvseries.templates import render_to_response

@route("/")
def index(req):
  return Redirect("/series")


@route("/series")
def series(req):
  return render_to_response('series.html', data=Serie().all())
  


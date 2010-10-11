



from pyroutes import route
from pyroutes.http.response import Redirect, Response


@route("/")
def index(req):
  return Redirect("/series")


@route("/series")
def series(req):
  return Response("List Series")

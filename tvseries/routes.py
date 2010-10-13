



from pyroutes import route
from pyroutes.http.response import Redirect, Response

from tvseries.model import Serie
from tvseries.templates import render_to_response
from tvseries.db import get_connection


@route("/")
def index(req):
  return Redirect("series")


@route("/series")
def series(req):
  return render_to_response('series.html', data=Serie().all())
  

@route("/serie/new")
def new_serie(req):
  if req.POST:
    serie = req.POST.get('serie', None)
    if serie:
      s = Serie(str(serie))
      s.save()
    return Redirect("series")
  
  return render_to_response('serie_new.html')


@route("/serie/delete")
def delete_serie(req, serie):
  c = get_connection()
  c.cursor().execute("delete from series where name = ?", (serie,))
  c.commit()
  c.close()
  return Redirect("series")


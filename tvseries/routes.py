



from pyroutes import route
from pyroutes.http.response import Redirect, Response

from tvseries.model import Serie
from tvseries.templates import render_to_response
from tvseries.db import get_connection


@route("/")
def index(req):
  return Redirect("/series")


@route("/series")
def series(req):
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute("select name from series")
  series = []
  for row in cursor.fetchall():
    series.append(row[0])

  episodes = {}
  for serie in series:
    cursor.execute("select name from episodes where serie = '%s' order by name" % serie)
    ep = cursor.fetchall()
    episodes[serie] = [e[0] for e in ep]


  return render_to_response('series.html', data={'series': series, 'episodes': episodes})
  

@route("/serie/new")
def new_serie(req):
  if req.POST:
    serie = req.POST.get('serie', None)
    if serie:
      s = Serie(str(serie))
      s.save()
    return Redirect("/series")
  
  return render_to_response('serie_new.html')


@route("/serie/delete")
def delete_serie(req, serie):
  c = get_connection()
  c.cursor().execute("delete from series where name = ?", (serie,))
  c.commit()
  c.close()
  return Redirect("/series")


@route("/serie/edit")
def edit_serie(req, serie):
  if req.POST:
    episode = req.POST.get('episode', None)
    if episode and serie:
      conn = get_connection()
      cursor = conn.cursor()
      cursor.execute("insert into episodes (name, serie) values (%s, %s)", (episode, serie))
      conn.commit()
    return Redirect("/series")
  return render_to_response('episode_new.html')



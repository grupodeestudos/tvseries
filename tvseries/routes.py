



from pyroutes import route
from pyroutes.http.response import Redirect, Response

from tvseries.model import Serie, Episode
from tvseries.templates import render_to_response
from tvseries import full_path_redirect
from elixir import *


@route("/")
def index(req):
  return Redirect(full_path_redirect(req.ENV, "/series"))


@route("/series")
def series(req):
  return render_to_response('series.html', data={'series': Serie.query.order_by(Serie.name).all()})
  

@route("/serie/new")
def new_serie(req):
  if req.POST:
    serie = req.POST.get('serie', None)
    if serie:
      s = Serie(name=serie)
      session.commit()
    return Redirect(full_path_redirect(req.ENV, "/series"))
  
  return render_to_response('serie_new.html')


@route("/serie/delete")
def delete_serie(req, serie):
  s = Serie.get_by(name=serie)
  if s:
    s.delete()
    session.commit()
  return Redirect(full_path_redirect(req.ENV, "/series"))

@route("/episode/delete")
def delete_episode(req, serie, episode):
  if serie and episode:
    s = Serie.get_by(name=serie)
    e = Episode.get_by(serie=s)
    s.episodes.remove(e)
    session.commit()
  return Redirect(full_path_redirect(req.ENV, "/series"))




@route("/serie/edit")
def edit_serie(req, serie):
  if req.POST:
    episode = req.POST.get('episode', None)
    if episode and serie:
      s = Serie.get_by(name=serie)
      e = Episode(name=episode)
      s.episodes.append(e)
      session.commit()
    return Redirect(full_path_redirect(req.ENV, "/series"))
  return render_to_response('episode_new.html')



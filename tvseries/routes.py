


import os
from pyroutes import route
from pyroutes.http.response import Redirect, Response

from tvseries.model import Serie, Episode
from tvseries.templates import render_to_response
from tvseries import full_path_redirect
from elixir import *


def _serve_file(path, content_type):
    location = os.path.join(os.path.dirname(__file__), path)
    content = file(location).read()
    return Response(content=content, headers=[('Content-type', content_type)])

@route("/static/css")
def static(req, file_name):
  if file_name:
    return _serve_file(req.ENV['PATH_INFO'].strip('/'), 'text/css')


@route("/")
def index(req):
  return Redirect(full_path_redirect(req.ENV, "/series"))


@route("/series")
def series(req):
  return render_to_response('series.html', data={'series': Serie.query.order_by(Serie.name).all()})
  

@route("/series/new")
def new_serie(req):
  if req.POST:
    serie = req.POST.get('serie', None)
    if serie:
      s = Serie(name=serie)
      session.commit()
    return Redirect(full_path_redirect(req.ENV, "/series"))
  
  return render_to_response('serie_new.html')


@route("/series/delete")
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
    e = Episode.get_by(serie=s, name=episode)
    s.episodes.remove(e)
    session.commit()
  return Redirect(full_path_redirect(req.ENV, "/series/edit/%s" % serie))




@route("/series/edit")
def edit_serie(req, serie):
  if req.POST:
    episode = req.POST.get('episode', None)
    if episode and serie:
      s = Serie.get_by(name=serie)
      e = Episode(name=episode)
      s.episodes.append(e)
      session.commit()
    return Redirect(full_path_redirect(req.ENV, "/series/edit/%s" % serie))
  s = Serie.get_by(name=serie)
  return render_to_response('episode_new.html', {'serie': s})



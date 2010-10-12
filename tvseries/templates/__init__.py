

__all__ = ['render_to_response']

from pyroutes.http.response import Response

def render_to_response(template_name, data):
  return Response("%s" % data)

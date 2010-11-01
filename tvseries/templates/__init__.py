

__all__ = ['render_to_response']

import os
from genshi.template import TemplateLoader
from pyroutes.http.response import Response
from pyroutes import settings

loader = TemplateLoader(os.path.dirname(__file__), auto_reload=True)

def render_to_response(template_name, data={}):
  tmpl = loader.load(template_name)
  data.update({'group': group,
               'SITE_ROOT': settings.SITE_ROOT})

  content = tmpl.generate(**data).render('html', doctype='html')
  return Response(content)



def group(iterable, num):
  return map(None, *[iter(iterable)] * num)

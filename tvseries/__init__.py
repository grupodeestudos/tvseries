


__all__ = ['routes']


'''
  Reconstruct the full URL to be redirected.
  Inside CGI environments you have to always redirect 
  to a complete URL
'''
def full_path_redirect(env, path):
  parts = []
  secure = env.has_key('HTTPS')
  
  protocol = "http"
  protocol += {True: 's:/', False: ':/'}[secure]
  server = env['SERVER_NAME']
  port = env['SERVER_PORT']
  script = env['SCRIPT_NAME'].rstrip("/").lstrip("/")

  parts.append(protocol)

  if (int(port) != 80 and not secure) or (int(port) != 443 and secure):
    server += ":" + port

  parts.append(server)
  if script:
    parts.append(script)

  parts.append(path.lstrip("/").rstrip("/"))

  return "/".join(parts)



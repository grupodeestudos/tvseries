



import ludibrio
import unittest

from tvseries import full_path_redirect

class PathReconstructTest(unittest.TestCase):
  
  #ENV = {}

  def setUp(self):
    self.ENV = {
        'HTTPS': 'on',
        'SERVER_NAME': 'www.somehost.com.br',
        'SERVER_PORT': '443',
        'SCRIPT_NAME': '/cgi-bin/app.py'
        }

  def test_basic_path(self):
    self.assertEquals("https://www.somehost.com.br/cgi-bin/app.py/path/to/go", full_path_redirect(self.ENV, "/path/to/go"))

  def test_http_not_port_80(self):
    self.ENV['SERVER_PORT'] = '8001'
    del self.ENV['HTTPS']
    self.assertEquals("http://www.somehost.com.br:8001/cgi-bin/app.py/path", full_path_redirect(self.ENV, "/path"))

  def test_https_port_443(self):
    self.ENV['SERVER_PORT'] = '443'
    self.assertEquals("https://www.somehost.com.br/cgi-bin/app.py/path", full_path_redirect(self.ENV, "/path"))

  def test_https_not_port_443(self):
    self.ENV['SERVER_PORT'] = '8002'
    self.assertEquals("https://www.somehost.com.br:8002/cgi-bin/app.py/path", full_path_redirect(self.ENV, "/path"))

  def test_script_name_with_trailing_slash(self):
    self.ENV['SCRIPT_NAME'] = '/cgi-bin/app.py/'
    self.assertEquals("https://www.somehost.com.br/cgi-bin/app.py/path", full_path_redirect(self.ENV, "/path"))

  def test_script_name_without_trailing_slash(self):
    self.ENV['SCRIPT_NAME'] = '/cgi-bin/app.py'
    self.assertEquals("https://www.somehost.com.br/cgi-bin/app.py/path", full_path_redirect(self.ENV, "/path"))

  def test_script_name_empty(self):
    self.ENV['SCRIPT_NAME'] = ''
    self.assertEquals("https://www.somehost.com.br/path", full_path_redirect(self.ENV, "/path"))


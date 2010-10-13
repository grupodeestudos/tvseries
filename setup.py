# encoding: utf-8
from distutils.core import setup


setup(
  name="tvseries",
  version="0.1",
  url="http://github.com/daltonmatos/tseries",
  license="GPLv2",
  description="Controlar as séries que eu vejo",
  author="Dalton Barreto",
  packages=['tvseries', 'tvseries.model', 'tvseries.db', 'tvseries.templates'],
  package_data = {'tvseries': ['templates/*.html']}
    )

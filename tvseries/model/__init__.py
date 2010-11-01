
from elixir import *
import os


__all__ = ['Serie', 'Episode']


class Serie(Entity):
  name = Field(String(48), required=True)
  episodes = OneToMany('tvseries.model.Episode', order_by="name")
  using_options(shortnames=True)
  

class Episode(Entity):
  name = Field(String(80), required=True)
  serie = ManyToOne('Serie')
  using_options(shortnames=True)


metadata.bind = "sqlite:///" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "tvseries.sqlite")
setup_all()

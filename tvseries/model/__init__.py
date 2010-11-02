
from elixir import *
import os
import re


__all__ = ['Serie', 'Episode']


class Serie(Entity):
  name = Field(String(48), required=True)
  episodes = OneToMany('tvseries.model.Episode', order_by="name")
  using_options(shortnames=True)

  def last_episode(self):
    if len(self.episodes) > 0:
      return self.episodes[-1:][0]
    return Episode(name="s01e00")
  

class Episode(Entity):
  name = Field(String(80), required=True)
  serie = ManyToOne('Serie')
  using_options(shortnames=True)

  def next(self):
    regex = re.compile("s(\d+)e(\d+)")
    if regex.match(self.name):
      regex_groups = regex.search(self.name).groups()
      next_episode_name = "s%se%02d" % (regex_groups[0], int(regex_groups[1]) + 1)
      return Episode(serie=self.serie, name=next_episode_name)
    else:
      return None


metadata.bind = "sqlite:///" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "tvseries.sqlite")
setup_all()

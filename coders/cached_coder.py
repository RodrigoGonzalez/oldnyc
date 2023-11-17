#!/usr/bin/python
#
# Instead of coding records, this coder loads results from a cache written out by a previous run. This can be used to speed up iteration.

import cPickle

class CachedCoder:
  def __init__(self, name):
    self._name = name
    unpickler = cPickle.Unpickler(open(f'/tmp/coder.{name}.pickle', 'r'))
    recs = unpickler.load()
    self._recs = {}

    for photo_id, loc in recs:
      self._recs[photo_id] = loc

  def codeRecord(self, r):
    return None if r.photo_id() not in self._recs else self._recs[r.photo_id()]

  def name(self):
    return self._name

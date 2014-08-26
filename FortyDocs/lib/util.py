'''
Created on Aug 27, 2014
@author: Mohammed Hamdy
'''

class TwoWayIterator(object):
  
  def __init__(self, items):
    self._items = items
    self._current_index = 0
    
  def __iter__(self):
    return self
  
  def next(self):
    if len(self._items) == self._current_index:
      raise StopIteration
    current_item = self._items[self._current_index]
    self._current_index += 1
    return current_item
  
  def prev(self):
    if self._current_index == 0:
      raise StopIteration
    self._current_index -= 1
    return self._items[self._current_index]
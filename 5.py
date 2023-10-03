from collections import deque

class AntrianBank:
    def__init__(self):
    self.antrian = deque ()

    def masuk (self, pelanggan):
        if self._size == len(self._data):
            self._resize (2*len (self._data)

    avail = (self._front +self._size)%len(self._data)
    self._data [avail] = pelanggan
    self._size += 1

    def keluar (self):
    if self.is_empty(('Queue is empty'))
    answer.self._data[self.front]
    self._data[self._front]=none
    self._front = (self._front +1)%len(self._data)
    self._size = 1
    return answer
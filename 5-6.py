import ctypes
class DynamicArray: 
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n
    
    def __getitem__(self, k):
        """Return element at index k."""
        if not k < self._n:
            raise IndexError('invalid index')
        if k < 0:
            return self._A[self._n + k]
        return self._A[k] # retrieve from array
    
    def append(self, obj):
        """Add object to end of array."""
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity)   # so double the capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c): # non public utility
        """Resize internal array to capacity c."""
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A = B
        self._capacity = c # use the bigger array

    def _make_array(self, c): # non public utility
        """Return new array with capacity c."""
        return (c * ctypes.py_object)() # see ctypes docs
    
    def insert(self, k, value):
        """Insert value at index k, shfting subsequent values rightward."""
        # for simplicity, we assume 0 <= k <= n
        if self._n == self.capacity: # not enough room
            self._resize(2 * self._capacity) # so double capacity
        for j in range(self._n, k, -1): # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
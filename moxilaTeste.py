class FixedSizeArray:
    def __init__(self, size, default=None):
        self._items = [default] * size
        self._size = size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        if index >= self._size or index < -self._size:
            raise IndexError("Index out of bounds.")
        self._items[index] = value

    def __repr__(self):
        return str(self._items)

# Usage
arr = FixedSizeArray(3)
arr[0] = "A"
print(arr)  # Output: ['A', None, None]
"""
Maximum Frequency Stack
"""

from collections import defaultdict

class FreqStack:
    """A stack data structure that efficiently retrieves 
    the element with the highest frequency."""
    def __init__(self):
        """Initializes an empty FreqStack."""
        self.freq = defaultdict(int)
        self.freq_elements = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        """Pushes the integer 'val' onto the top of the stack."""
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.freq_elements[self.freq[val]].append(val)

    def pop(self) -> int:
        """Removes and returns the element with the highest frequency from the stack."""
        val = self.freq_elements[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.freq_elements[self.max_freq]:
            self.max_freq -= 1
        return val

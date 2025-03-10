class RandomizedSet:

    def __init__(self):
        self.values = []
        self.value_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False
        self.values.append(val)
        self.value_to_index[val] = len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False
        
        index = self.value_to_index[val]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.value_to_index[last_val] = index
        self.values.pop()
        del self.value_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
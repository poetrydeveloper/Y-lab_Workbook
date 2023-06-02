
class CyclicIterator(object):
    def __init__(self, collection):
        self.index = 0
        self.collection = collection
        self.len = len(collection)

    def __iter__(self):
        return self

    def __next__(self):
        value = None
        if self.index >= self.len:
            self.index = 0
        val = self.collection[self.index]
        self.index += 1
        return val

        return self.count


cyclic_iterator = CyclicIterator([1, 2, 3])
for i in cyclic_iterator:
    print(i)
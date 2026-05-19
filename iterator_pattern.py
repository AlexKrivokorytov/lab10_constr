class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

class ListIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def has_next(self):
        return self._position < len(self._collection)

    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements in the collection.")
        item = self._collection[self._position]
        self._position += 1
        return item

class Aggregate:
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def create_iterator(self):
        return ListIterator(self._items)

if __name__ == "__main__":
    collection = ConcreteAggregate()
    collection.add_item("Элемент 1")
    collection.add_item("Элемент 2")
    collection.add_item("Элемент 3")

    iterator = collection.create_iterator()

    print("Обход коллекции с помощью Итератора:")
    while iterator.has_next():
        item = iterator.next()
        print(item)

    print("\nПовторный обход коллекции:")
    new_iterator = collection.create_iterator()
    for item in new_iterator._collection:
        print(item)

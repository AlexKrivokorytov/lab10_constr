# Abstract Iterator interface
# Defines the interface for traversing collections
class Iterator:
    # Base iterator class that defines methods for accessing collection elements.
    
    def has_next(self):
        # Check if there are more elements in the collection.
        pass

    def next(self):
        # Get the next element from the collection.
        pass

# Concrete Iterator implementation
class ListIterator(Iterator):
    # Iterator implementation for iterating through a list collection.
    
    def __init__(self, collection):
        # Initialize the iterator with a collection and set the starting position.
        self._collection = collection  # Reference to the collection
        self._position = 0  # Current position in the collection

    def has_next(self):
        # Check if there are more elements to iterate through.
        return self._position < len(self._collection)

    def next(self):
        # Return the current element and move to the next position.
        if not self.has_next():
            raise StopIteration("No more elements in the collection.")
        item = self._collection[self._position]
        self._position += 1
        return item

# Abstract Aggregate (Collection) interface
class Aggregate:
    # Base class that defines the interface for creating iterators.
    
    def create_iterator(self):
        # Create and return an iterator for this collection.
        pass

# Concrete Aggregate (Collection) implementation
class ConcreteAggregate(Aggregate):
    # Concrete collection class that stores items and creates iterators.
    
    def __init__(self):
        # Initialize the collection with an empty list.
        self._items = []  # Internal storage for collection items

    def add_item(self, item):
        # Add an item to the collection.
        self._items.append(item)

    def create_iterator(self):
        # Create and return a new iterator for this collection.
        return ListIterator(self._items)

# Example usage demonstrating the Iterator pattern
if __name__ == "__main__":
    # Create a collection and add items
    collection = ConcreteAggregate()
    collection.add_item("Element 1")
    collection.add_item("Element 2")
    collection.add_item("Element 3")

    # Create an iterator for the collection
    iterator = collection.create_iterator()

    # First traversal using iterator
    print("Traversing collection with Iterator:")
    while iterator.has_next():
        item = iterator.next()
        print(item)

    # Second traversal of the collection
    print("\nSecond traversal of collection:")
    new_iterator = collection.create_iterator()
    for item in new_iterator._collection:
        print(item)

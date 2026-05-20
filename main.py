# Import design pattern implementations
from iterator_pattern import ConcreteAggregate
from mediator_pattern import ConcreteMediator, ConcreteColleague1, ConcreteColleague2
from observer_pattern import ConcreteSubject, ConcreteObserver

def demonstrate_iterator():
    """Demonstrate the Iterator design pattern.
    
    The Iterator pattern provides a way to access elements of a collection
    sequentially without exposing its underlying representation.
    """
    print("\n--- Iterator Pattern Demonstration ---")
    # Create a collection and populate it with items
    collection = ConcreteAggregate()
    collection.add_item("Book 1")
    collection.add_item("Book 2")
    collection.add_item("Book 3")

    # Create an iterator for the collection
    iterator = collection.create_iterator()

    # Traverse the collection using the iterator
    print("Traversing book collection using Iterator:")
    while iterator.has_next():
        item = iterator.next()
        print(item)

def demonstrate_mediator():
    """Demonstrate the Mediator design pattern.
    
    The Mediator pattern defines an object that encapsulates how a set of objects
    interact, promoting loose coupling by keeping objects from referring to each
    other explicitly.
    """
    print("\n--- Mediator Pattern Demonstration ---")
    # Create two colleagues
    colleague1 = ConcreteColleague1()
    colleague2 = ConcreteColleague2()
    # Create a mediator to coordinate their communication
    mediator = ConcreteMediator(colleague1, colleague2)

    # Trigger operation B on colleague1, mediator handles the communication
    print("Client initiates operation B on Colleague1, mediator reacts:")
    colleague1.do_something_b()

    # Trigger operation C on colleague2, mediator handles the communication
    print("\nClient initiates operation C on Colleague2, mediator reacts:")
    colleague2.do_something_c()

def demonstrate_observer():
    """Demonstrate the Observer design pattern.
    
    The Observer pattern defines a one-to-many dependency between objects such that
    when one object changes state, all its dependents are notified and updated
    automatically.
    """
    print("\n--- Observer Pattern Demonstration ---")
    # Create a subject (observable)
    subject = ConcreteSubject()

    # Create two observers
    observer_a = ConcreteObserver("User A")
    observer_b = ConcreteObserver("User B")

    # Attach observers to the subject
    subject.attach(observer_a)
    subject.attach(observer_b)

    # Change subject state - both observers will be notified
    print("\nSubject changes state to (10):")
    subject.set_state(10)

    # Detach one observer and change state again
    print("\nSubject changes state to (20), User A unsubscribes:")
    subject.detach(observer_a)
    subject.set_state(20)

if __name__ == "__main__":
    # Main entry point
    print("LABORATORY WORK No.8: Behavioral Design Patterns")
    # Demonstrate all three behavioral design patterns
    demonstrate_iterator()
    demonstrate_mediator()
    demonstrate_observer()

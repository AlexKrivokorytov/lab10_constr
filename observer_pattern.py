# Subject (Observable) class
class Subject:
    """Subject class that maintains a list of observers and notifies them of state changes."""
    
    def __init__(self):
        """Initialize the subject with an empty list of observers."""
        self._observers = []  # List to store attached observers

    def attach(self, observer):
        """Attach an observer to this subject if not already attached."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove an observer from this subject."""
        self._observers.remove(observer)

    def notify(self):
        """Notify all attached observers about state change."""
        for observer in self._observers:
            observer.update(self)  # Call update method on each observer

# Abstract Observer interface
class Observer:
    """Base observer class that defines the update interface."""
    
    def update(self, subject):
        """Receive update notification from the subject."""
        pass

# Concrete Subject implementation
class ConcreteSubject(Subject):
    """Concrete subject that maintains internal state and notifies observers of changes."""
    
    def __init__(self):
        """Initialize the subject with no state."""
        super().__init__()
        self._state = None  # Internal state

    def get_state(self):
        """Get the current state of the subject."""
        return self._state

    def set_state(self, state):
        """Set a new state and notify all observers."""
        print(f"Subject: Changing state to {state}")
        self._state = state  # Update internal state
        self.notify()  # Notify all observers about the state change

# Concrete Observer implementation
class ConcreteObserver(Observer):
    """Concrete observer that reacts to subject state changes."""
    
    def __init__(self, name):
        """Initialize the observer with a name."""
        self._name = name  # Observer identifier
        self._subject_state = None  # Cached subject state

    def update(self, subject):
        """Update the observer with the subject's new state."""
        self._subject_state = subject.get_state()  # Get the new state from subject
        print(f"Observer {self._name}: Subject state updated to {self._subject_state}")

# Example usage demonstrating the Observer pattern
if __name__ == "__main__":
    # Create a concrete subject
    subject = ConcreteSubject()

    # Create two concrete observers
    observer_a = ConcreteObserver("A")
    observer_b = ConcreteObserver("B")

    # Attach observers to the subject
    subject.attach(observer_a)
    subject.attach(observer_b)

    # Set state and both observers will be notified
    subject.set_state(10)
    subject.set_state(20)

    # Detach one observer
    subject.detach(observer_a)

    # Set state again - only observer B will be notified
    subject.set_state(30)

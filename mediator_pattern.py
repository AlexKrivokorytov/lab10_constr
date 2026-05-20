# Abstract Mediator interface
class Mediator:
    # Base mediator class that defines the interface for communication coordination.
    
    def notify(self, sender, event):
        # Handle communication between colleagues.
        pass

# Concrete Mediator implementation
class ConcreteMediator(Mediator):
    # Concrete mediator that coordinates communication between colleagues.
    
    def __init__(self, colleague1, colleague2):
        # Initialize the mediator with two colleagues and set self as their mediator.
        self._colleague1 = colleague1  # Reference to first colleague
        self._colleague1.mediator = self  # Set this mediator for colleague1
        self._colleague2 = colleague2  # Reference to second colleague
        self._colleague2.mediator = self  # Set this mediator for colleague2

    def notify(self, sender, event):
        # React to events from colleagues and coordinate responses.
        if sender == self._colleague1:
            # If colleague1 sends an event, notify colleague2
            print(f"Mediator reacts to Colleague1 and triggers Colleague2: {event}")
            self._colleague2.do_something_else()
        elif sender == self._colleague2:
            # If colleague2 sends an event, notify colleague1
            print(f"Mediator reacts to Colleague2 and triggers Colleague1: {event}")
            self._colleague1.do_something_a()

# Base Colleague class
class Colleague:
    # Base colleague class with reference to a mediator.
    
    def __init__(self, mediator=None):
        # Initialize the colleague with an optional mediator.
        self._mediator = mediator  # Reference to the mediator

    @property
    def mediator(self):
        # Get the current mediator.
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        # Set the mediator for this colleague.
        self._mediator = mediator

# Concrete Colleague 1 implementation
class ConcreteColleague1(Colleague):
    # First concrete colleague that can perform operations and communicate via mediator.
    
    def do_something_a(self):
        # Perform operation A and notify the mediator.
        print("Colleague1 does something A.")
        self.mediator.notify(self, "A")  # Notify mediator about operation A

    def do_something_b(self):
        # Perform operation B and notify the mediator.
        print("Colleague1 does something B.")
        self.mediator.notify(self, "B")  # Notify mediator about operation B

# Concrete Colleague 2 implementation
class ConcreteColleague2(Colleague):
    # Second concrete colleague that can perform operations and communicate via mediator.
    
    def do_something_c(self):
        # Perform operation C and notify the mediator.
        print("Colleague2 does something C.")
        self.mediator.notify(self, "C")  # Notify mediator about operation C

    def do_something_else(self):
        # Perform another operation without notifying the mediator.
        print("Colleague2 does something else.")

# Example usage demonstrating the Mediator pattern
if __name__ == "__main__":
    # Create two colleagues
    colleague1 = ConcreteColleague1()
    colleague2 = ConcreteColleague2()
    # Create mediator and set it for both colleagues
    mediator = ConcreteMediator(colleague1, colleague2)

    # Client initiates operation B on Colleague1
    print("Client initiates operation B on Colleague1:")
    colleague1.do_something_b()

    # Client initiates operation C on Colleague2
    print("\nClient initiates operation C on Colleague2:")
    colleague2.do_something_c()

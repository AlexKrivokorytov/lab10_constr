class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, colleague1, colleague2):
        self._colleague1 = colleague1
        self._colleague1.mediator = self
        self._colleague2 = colleague2
        self._colleague2.mediator = self

    def notify(self, sender, event):
        if sender == self._colleague1:
            print(f"Mediator reacts on Colleague1 and triggers Colleague2: {event}")
            self._colleague2.do_something_else()
        elif sender == self._colleague2:
            print(f"Mediator reacts on Colleague2 and triggers Colleague1: {event}")
            self._colleague1.do_something_a()

class Colleague:
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

class ConcreteColleague1(Colleague):
    def do_something_a(self):
        print("Colleague1 does something A.")
        self.mediator.notify(self, "A")

    def do_something_b(self):
        print("Colleague1 does something B.")
        self.mediator.notify(self, "B")

class ConcreteColleague2(Colleague):
    def do_something_c(self):
        print("Colleague2 does something C.")
        self.mediator.notify(self, "C")

    def do_something_else(self):
        print("Colleague2 does something else.")

if __name__ == "__main__":
    colleague1 = ConcreteColleague1()
    colleague2 = ConcreteColleague2()
    mediator = ConcreteMediator(colleague1, colleague2)

    print("Клиент запускает операцию B у Colleague1:")
    colleague1.do_something_b()

    print("\nКлиент запускает операцию C у Colleague2:")
    colleague2.do_something_c()

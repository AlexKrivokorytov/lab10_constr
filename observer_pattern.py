class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state):
        print(f"Subject: Changing state to {state}")
        self._state = state
        self.notify()

class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name
        self._subject_state = None

    def update(self, subject):
        self._subject_state = subject.get_state()
        print(f"Observer {self._name}: Subject state updated to {self._subject_state}")

if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserver("A")
    observer_b = ConcreteObserver("B")

    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.set_state(10)
    subject.set_state(20)

    subject.detach(observer_a)

    subject.set_state(30)

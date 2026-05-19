from iterator_pattern import ConcreteAggregate
from mediator_pattern import ConcreteMediator, ConcreteColleague1, ConcreteColleague2
from observer_pattern import ConcreteSubject, ConcreteObserver

def demonstrate_iterator():
    print("\n--- Демонстрация шаблона Iterator ---")
    collection = ConcreteAggregate()
    collection.add_item("Книга 1")
    collection.add_item("Книга 2")
    collection.add_item("Книга 3")

    iterator = collection.create_iterator()

    print("Обход коллекции книг с помощью Итератора:")
    while iterator.has_next():
        item = iterator.next()
        print(item)

def demonstrate_mediator():
    print("\n--- Демонстрация шаблона Mediator ---")
    colleague1 = ConcreteColleague1()
    colleague2 = ConcreteColleague2()
    mediator = ConcreteMediator(colleague1, colleague2)

    print("Клиент запускает операцию B у Colleague1, посредник реагирует:")
    colleague1.do_something_b()

    print("\nКлиент запускает операцию C у Colleague2, посредник реагирует:")
    colleague2.do_something_c()

def demonstrate_observer():
    print("\n--- Демонстрация шаблона Observer ---")
    subject = ConcreteSubject()

    observer_a = ConcreteObserver("Пользователь A")
    observer_b = ConcreteObserver("Пользователь B")

    subject.attach(observer_a)
    subject.attach(observer_b)

    print("\nСубъект изменяет состояние (10):")
    subject.set_state(10)

    print("\nСубъект изменяет состояние (20), Пользователь A отписывается:")
    subject.detach(observer_a)
    subject.set_state(20)

if __name__ == "__main__":
    print("ЛАБОРАТОРНАЯ РАБОТА №8: Поведенческие шаблоны проектирования")
    demonstrate_iterator()
    demonstrate_mediator()
    demonstrate_observer()

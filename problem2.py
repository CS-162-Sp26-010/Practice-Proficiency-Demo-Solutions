class Person:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def print(self) -> None:
        print(self._name)

class Student(Person):
    _gpa: float

    def __init__(self, gpa: float, name: str) -> None:
        super().__init__(name)
        self._gpa = gpa

    def print(self) -> None:
        super().print()
        print(self._gpa)

    def award(self) -> str | None:
        if self._gpa >= 3.9:
            return 'Summa Cum Laude'
        elif self._gpa >= 3.7:
            return 'Magna Cum Laude'
        elif self._gpa >= 3.5:
            return 'Cum Laude'
        else:
            return None

def main() -> None:
    ramesh = Person('Ramesh')
    ramesh.print()

    jasper = Student(3.49, 'Jasper')
    jasper.print()
    print(jasper.award())

if __name__ == '__main__':
    main()

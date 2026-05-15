class Fruit:
    _kind: str

    def __init__(self, kind: str) -> None:
        self._kind = kind

    def print(self) -> None:
        print(self._kind)

class Apple(Fruit):
    _diameter: float
    _color: str

    def __init__(self, diameter: float, color: str) -> None:
        super().__init__('Apple')
        self._diameter = diameter
        self._color = color

    def print(self) -> None:
        super().print()
        print(self._diameter)
        print(self._color)

def main() -> None:
    banana = Fruit('Banana')
    banana.print()

    apple = Apple(3.5, 'Red')
    apple.print()

if __name__ == '__main__':
    main()

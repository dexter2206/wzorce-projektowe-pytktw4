from typing import Protocol


class Drawable(Protocol):

    def draw(self):
        pass


class DrawableContainer:

    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def draw(self):
        for obj in self.objects:
            obj.draw()


class Map(DrawableContainer):

    def draw(self):
        print("Drawing map!")
        super().draw()


class Vehicle(DrawableContainer):

    def draw(self):
        print("Drawing vehicle with players inside.")
        super().draw()


class Player:

    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f"Drawing player {self.name}.")


if __name__ == '__main__':
    game_map = Map()

    game_map.add_object(Player("Konrad"))
    game_map.add_object(Player("Janusz"))

    # Tworzymy pojazd
    vehicle = Vehicle()
    vehicle.add_object(Player("Alice"))
    vehicle.add_object(Player("Bob"))

    game_map.add_object(vehicle)

    game_map.draw()

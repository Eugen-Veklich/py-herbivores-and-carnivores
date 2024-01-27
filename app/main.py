from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    def bite(self, other: Herbivore | Carnivore) -> None:
        if isinstance(other, Herbivore) and other.hidden is not True:
            other.health -= 50
            if other.health <= 0:
                del Animal.alive[Animal.alive.index(other)]

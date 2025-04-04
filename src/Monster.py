from abc import ABC, abstractmethod

class Monster(ABC):
    def __init__(self, name: str, hp: int, max_hp: int, strength: int, defense: int):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.defense = defense

    @property
    def is_defeated(self) -> bool:
        """モンスターが敗北したかどうかを判定するプロパティ"""
        return self.hp <= 0

    @abstractmethod
    def attack(self, target: "Monster"):
        pass

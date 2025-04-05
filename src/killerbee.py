from monster import Monster
from random import random

class KillerBee(Monster):
    def __init__(self, hp: int, max_hp: int, strength: int, defense: int, level: int = 1, name: str = "キラービー"):
        # 親クラスのコンストラクタを呼び出す
        super().__init__(name, hp, max_hp, strength, defense, level)
        
    def attack(self, target: Monster):
        damage = max(0, self.strength - target.defense)
        target.hp -= damage
        print(f"{self.name} の攻撃！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")
            
    def special_attack(self, target: Monster):
        roll = random()
        # 50%の確率で通常攻撃、50%の確率で2倍のダメージを与える
        if roll < 0.5:
            damage = max(0, self.strength * 2 - target.defense)
        else:
            damage = max(0, self.strength - target.defense)
        target.hp -= damage
        print(f"{self.name} の毒針攻撃！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")

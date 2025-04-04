from monster import Monster

class MyMonster(Monster):
    def attack(self, target: Monster):
        damage = max(0, self.strength - target.defense)
        target.hp -= damage
        print(f"{self.name} の攻撃！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")

from monster import Monster

class StrayCat(Monster):
    def __init__(self, hp: int = 100, max_hp: int = 100, strength: int = 10, defense: int = 5, level: int = 1, name: str = "ストレイキャット",):
        # 親クラスのコンストラクタを呼び出す
        super().__init__(name, hp, max_hp, strength, defense, level)

    def attack(self, target: Monster):
        damage = max(0, self.strength - target.defense)
        target.hp -= damage
        print(f"{self.name} の攻撃！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")
      
    def special_attack(self, target: Monster):
        damage = max(0, int(self.strength * 1.5) - target.defense)
        target.hp -= damage
        print(f"{self.name} のねこパンチ！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")

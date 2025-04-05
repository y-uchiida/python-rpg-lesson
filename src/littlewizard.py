from monster import Monster

class LittleWizard(Monster):
    def __init__(self, hp: int, max_hp: int, strength: int, defense: int, level: int = 1, name: str = "リトルウィザード"):
        # 親クラスのコンストラクタを呼び出す
        super().__init__(name, hp, max_hp, strength, defense, level)

    def attack(self, target: Monster):
        damage = max(0, self.strength - target.defense)
        target.hp -= damage
        print(f"{self.name} の攻撃！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")
            
    def special_attack(self, target: Monster):
        # // (切り捨て除算)を用いると、割り算の結果の小数を切り捨てる
        damage = max(0, self.strength - target.defense // 2)
        target.hp -= damage
        print(f"{self.name} は魔法を唱えた！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")

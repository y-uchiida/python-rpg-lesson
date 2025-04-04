from monster import Monster

class MyMonster(Monster):
    def __init__(self, name, hp, max_hp, strength, defense, level=1):
        # 親クラスのコンストラクタを呼び出す
        super().__init__(name, hp, max_hp, strength, defense)
        
        # MyMonster クラスで追加する属性の初期化
        self.level = level
        self.experience = 0

    def attack(self, target: Monster):
        damage = max(0, self.strength - target.defense)
        target.hp -= damage
        print(f"{self.name} の攻撃！ {target.name} に {damage} ダメージを与えた")
        if target.is_defeated:
            print(f"{target.name} は倒れた！")

    def gain_experience(self, exp):
        print(f"{self.name} は {exp} の経験値を獲得した！")
        self.experience += exp
        self.check_level_up()

    def check_level_up(self):
        # レベルアップに必要な経験値を計算 (例: レベル × 100)
        required_exp = self.level * 100
        while self.experience >= required_exp:
            self.experience -= required_exp
            self.level_up()
            required_exp = self.level * 100

    def level_up(self):
        self.level += 1
        self.max_hp += 10  # レベルアップ時に最大HPを増加
        self.hp = self.max_hp  # HPを全回復
        self.strength += 2  # 攻撃力を増加
        self.defense += 1  # 防御力を増加
        print(f"{self.name} のレベルが {self.level} に上がった！")
        print(f"ステータスが上昇しました: HP {self.max_hp}, 攻撃力 {self.strength}, 防御力 {self.defense}")

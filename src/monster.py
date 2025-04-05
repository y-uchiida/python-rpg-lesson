from abc import ABC, abstractmethod

class Monster(ABC):
    def __init__(self, name: str, hp: int, max_hp: int, strength: int, defense: int, level: int = 1, experience: int = 0):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.defense = defense
        self.level = level
        self.experience = experience

    @property
    def is_defeated(self) -> bool:
        """モンスターが敗北したかどうかを判定するプロパティ"""
        return self.hp <= 0

    @abstractmethod
    def attack(self, target: "Monster"):
        pass

    @abstractmethod
    def special_attack(self, target: "Monster"):
        pass

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

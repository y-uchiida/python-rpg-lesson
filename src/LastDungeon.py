from EnemyMonster import EnemyMonster
from Field import Field

class LastDungeon(Field):
    def __init__(self, enemies):
        super().__init__(enemies)
        # ラスボスキャラクターを追加
        boss = EnemyMonster(name="ラスボス", hp=200, max_hp=200, strength=30, defense=10)
        self.enemies.append(boss)

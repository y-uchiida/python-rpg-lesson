from MyMonster import MyMonster
from EnemyMonster import EnemyMonster

def main():
    # 味方キャラクターと敵キャラクターを作成
    hero = MyMonster(name="味方キャラ", hp=100, max_hp=100, strength=20, defense=5)
    enemy = EnemyMonster(name="敵キャラ", hp=80, max_hp=80, strength=15, defense=3)

    # 戦闘ループ
    while not hero.is_defeated and not enemy.is_defeated:
        hero.attack(enemy)
        if enemy.is_defeated:
            print("戦闘に勝利しました！")
            break
        enemy.attack(hero)
        if hero.is_defeated:
            print("戦闘に敗北しました...")
            break

if __name__ == "__main__":
    main()

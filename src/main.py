from MyMonster import MyMonster
from EnemyMonster import EnemyMonster
from Field import Field

def battle(party, field):
    while party and field.enemies:
        # 次に戦闘可能な味方キャラクターを取得
        hero = next((monster for monster in party if not monster.is_defeated), None)
        if not hero:
            print("味方キャラクターが全滅しました。ゲームオーバーです。")
            return False

        # 次に戦闘可能な敵キャラクターを取得
        enemy = next((monster for monster in field.enemies if not monster.is_defeated), None)
        if not enemy:
            print("敵キャラクターを全て倒しました！")
            return True

        # 戦闘ループ
        while not hero.is_defeated and not enemy.is_defeated:
            print("\n次の行動を選択してください:")
            print("1: たたかう")
            print("2: にげる")
            print("3: 交代")
            choice = input("選択肢を入力してください (1/2/3): ")

            if choice == "1":
                # たたかう
                hero.attack(enemy)
                if enemy.is_defeated:
                    print(f"{enemy.name} を倒しました！")
                    break
                enemy.attack(hero)
                if hero.is_defeated:
                    print(f"{hero.name} が倒されました...")
                    break
            elif choice == "2":
                # にげる
                print("戦闘から逃げました！")
                return True  # 戦闘終了後の選択肢に遷移
            elif choice == "3":
                # 交代
                available_monsters = [monster for monster in party if not monster.is_defeated and monster != hero]
                if available_monsters:
                    print("交代可能なキャラクター:")
                    for i, monster in enumerate(available_monsters, start=1):
                        print(f"{i}: {monster.name} (体力: {monster.hp}/{monster.max_hp})")
                    try:
                        selected_index = int(input("交代するキャラクターの番号を入力してください: ")) - 1
                        if 0 <= selected_index < len(available_monsters):
                            new_hero = available_monsters[selected_index]
                            party.remove(new_hero)
                            party.insert(0, new_hero)
                            print(f"{new_hero.name} が戦闘に参加します！")
                            hero = new_hero
                        else:
                            print("無効な番号です。")
                    except ValueError:
                        print("無効な入力です。番号を入力してください。")
                else:
                    print("交代できるキャラクターがいません！")
            else:
                print("無効な入力です。1, 2, または 3 を入力してください。")

    return True

def main():
    # 味方キャラクターの作成
    party = [
        MyMonster(name="味方キャラ1", hp=100, max_hp=100, strength=20, defense=5),
        MyMonster(name="味方キャラ2", hp=80, max_hp=80, strength=18, defense=4)
    ]

    while True:
        # フィールドと敵キャラクターの作成
        field = Field([
            EnemyMonster(name="敵キャラ1", hp=80, max_hp=80, strength=15, defense=3),
            EnemyMonster(name="敵キャラ2", hp=90, max_hp=90, strength=17, defense=4)
        ])

        # 戦闘処理
        if not battle(party, field):
            return  # ゲーム終了

        # 戦闘終了後の選択肢
        while True:
            for monster in party:
                if monster.is_defeated:
                    print(f"{monster.name} は戦闘不能です。")
                else:
                    print(f"{monster.name} の体力: {monster.hp}/{monster.max_hp}")
            print("\n次の行動を選択してください:")
            print("1: 次の戦闘を開始する")
            print("2: 休憩して体力を回復する")
            print("3: ゲームを終了する")
            choice = input("選択肢を入力してください (1/2/3): ")

            if choice == "1":
                break  # 次の戦闘を開始
            elif choice == "2":
                for monster in party:
                    monster.hp = monster.max_hp
                print("味方キャラクターの体力が全回復しました！")
            elif choice == "3":
                print("ゲームを終了します。")
                return
            else:
                print("無効な入力です。1, 2, または 3 を入力してください。")

if __name__ == "__main__":
    main()

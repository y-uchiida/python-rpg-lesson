from mymonster import MyMonster
from enemymonster import EnemyMonster
from field import Field
from party import Party
from lastdungeon import LastDungeon
from random import random, choice
from strengthupitem import StrengthUpItem
from defenceupitem import DefenseUpItem

battle_clear_count = 0 # 戦闘クリア回数
last_dungeon_cleared = False  # 最後のダンジョンをクリアしたかどうかのフラグ

def battle(party, field):
    # battle_clear_count と last_dungeon_cleared をグローバル変数として使用
    global battle_clear_count, last_dungeon_cleared    
    while True:
        # 次に戦闘可能な味方キャラクターを取得
        battler = next((monster for monster in party.members if not monster.is_defeated), None)
        if not battler:
            print("味方キャラクターが全滅しました。ゲームオーバーです。")
            return False

        # 次に戦闘可能な敵キャラクターを取得
        enemy = next((monster for monster in field.enemies if not monster.is_defeated), None)
        if not enemy:
            print("敵キャラクターを全て倒しました！")
            for monster in party.members:
                monster.gain_experience(50)  # 経験値を付与
            battle_clear_count += 1  # 戦闘クリア回数を増加
            print(f"戦闘クリア回数: {battle_clear_count}")
            if battle_clear_count == 3 and not last_dungeon_cleared:
                print("最終ダンジョンに挑戦できるようになりました！")
            return True

        # 戦闘ループ
        while True:
            print("\n次の行動を選択してください:")
            print("1: たたかう")
            print("2: にげる")
            print("3: 交代")
            choice = input("選択肢を入力してください (1/2/3): ")

            if choice == "1":
                # たたかう
                battler.attack(enemy)
                if enemy.is_defeated:
                    # 敵キャラクターを倒した場合、アイテムの獲得判定を行う
                    drop_item(party, enemy)
                    break
                enemy.attack(battler)
                if battler.is_defeated:
                    break
            elif choice == "2":
                # にげる
                print("戦闘から逃げました！")
                return True  # 戦闘終了後の選択肢に遷移
            elif choice == "3":
                # 交代
                available_monsters = [monster for monster in party.members if not monster.is_defeated and monster != battler]
                if available_monsters:
                    print("交代可能なキャラクター:")
                    for i, monster in enumerate(available_monsters, start=1):
                        print(f"{i}: {monster.name} (体力: {monster.hp}/{monster.max_hp})")
                    try:
                        selected_index = int(input("交代するキャラクターの番号を入力してください: ")) - 1
                        if 0 <= selected_index < len(available_monsters):
                            new_battler = available_monsters[selected_index]
                            party.members.remove(new_battler)
                            party.members.insert(0, new_battler)
                            print(f"{new_battler.name} が戦闘に参加します！")
                            battler = new_battler
                        else:
                            print("無効な番号です。")
                    except ValueError:
                        print("無効な入力です。番号を入力してください。")
                else:
                    print("交代できるキャラクターがいません！")
            else:
                print("無効な入力です。1, 2, または 3 を入力してください。")

    return True

def drop_item(party, enemy):
    """
    敵キャラクターを倒した際にアイテムを獲得する関数。
    アイテムの獲得確率は 50%。
    獲得するアイテムはランダムで決定される。
    """
    item_drop_chance = random()
    # if item_drop_chance < 0.5:
    if True:
        # 獲得するアイテムをランダムで決定
        # choice() を使用して、アイテムのリストからランダムに選択
        dropped_item = choice([StrengthUpItem(), DefenseUpItem()])
        
        # アイテムを追加
        party.add_item_storage(dropped_item)

        print(f"{enemy.name} が {dropped_item.name} をドロップしました！")

def choice_dungeon():
    """
    ダンジョンの選択を行う関数。
    既定の戦闘回数をクリアしている場合は最終ダンジョンを選択するかの入力待ちをする。
    最終ダンジョンを選択した場合は、最終ダンジョンのオブジェクトを返す。
    最終ダンジョンを選択しなかった場合既定のクリア回数を満たしていない場合は、通常のダンジョンを選択する。
    """
    global battle_clear_count, last_dungeon_cleared

    # 戦闘クリア回数が既定回数以下の場合、通常ダンジョン(Field)を返す
    if battle_clear_count < 3:
        return Field([
            EnemyMonster(name="通常敵キャラ1", hp=80, max_hp=80, strength=15, defense=3),
            EnemyMonster(name="通常敵キャラ2", hp=90, max_hp=90, strength=17, defense=4)
        ])

    # 最終ダンジョンの選択
    while True:
        choice = input("ラスボスダンジョンに挑戦しますか？(y/n): ")
        if choice.lower() == 'y':
            # 最終ダンジョンを選択
            return LastDungeon([
                EnemyMonster(name="ラストダンジョンの敵1", hp=120, max_hp=120, strength=25, defense=6),
                EnemyMonster(name="ラストダンジョンの敵2", hp=150, max_hp=150, strength=30, defense=8)
            ])
        elif choice.lower() == 'n':
            # 通常ダンジョンを選択
            return Field([
                EnemyMonster(name="通常敵キャラ1", hp=80, max_hp=80, strength=15, defense=3),
                EnemyMonster(name="通常敵キャラ2", hp=90, max_hp=90, strength=17, defense=4)
            ])
        else:
            print("無効な入力です。'y' または 'n' を入力してください。")
            continue

def main():
    global battle_clear_count, last_dungeon_cleared

    # 味方キャラクターの作成
    party = Party([
        MyMonster(name="味方キャラ1", hp=100, max_hp=100, strength=2000, defense=5),
        MyMonster(name="味方キャラ2", hp=80, max_hp=80, strength=1800, defense=4)
    ])

    while True:
        for monster in party.members:
            if monster.is_defeated:
                print(f"{monster.name} は戦闘不能です。")
            else:
                print(f"{monster.name} の体力: {monster.hp}/{monster.max_hp}")
        print("\n次の行動を選択してください:")
        print("1: 次の戦闘を開始する")
        print("2: 休憩して体力を回復する")
        print("3: アイテムを使用する")
        print("4: ゲームを終了する")
        choice = input("選択肢を入力してください (1/2/3/4): ")

        if choice == "1":
            # ダンジョンを選択
            field = choice_dungeon()
            print("ダンジョンに挑戦します！")
            if battle(party, field):
                # 戦闘クリア後の処理
                if isinstance(field, LastDungeon):
                    last_dungeon_cleared = True
                    print("ラスボスを倒しました！")
        elif choice == "2":
            for monster in party.members:
                monster.hp = monster.max_hp
            print("味方キャラクターの体力が全回復しました！")
        elif choice == "3":
            if len(party.item_storage) == 0:
                print("使用可能なアイテムがありません！")
            else:
                print("使用可能なアイテム:")
                for i, item_in_storage in enumerate(party.item_storage, start=1):
                    print(f"{i}: {item_in_storage.item.name} (所持数: {item_in_storage.item_count}/{item_in_storage.item.MAX_ITEM_NUM})")
                try:
                    selected_index = int(input("使用するアイテムの番号を入力してください: ")) - 1
                    if 0 <= selected_index < len(party.item_storage):
                        selected_item = party.item_storage[selected_index]
                        print("使用するキャラクターを選択してください:")
                        for j, monster in enumerate(party.members, start=1):
                            print(f"{j}: {monster.name} (体力: {monster.hp}/{monster.max_hp})")
                        selected_monster_index = int(input("キャラクターの番号を入力してください: ")) - 1
                        if 0 <= selected_monster_index < len(party.members):
                            selected_monster = party.members[selected_monster_index]
                            selected_item.item.use(selected_monster)
                            print(f"{selected_item.item.name} を {selected_monster.name} に使用しました！")
                            party.remove_item_storage(selected_item.item)
                        else:
                            print("無効なキャラクター番号です。")
                    else:
                        print("無効なアイテム番号です。")
                except ValueError:
                    print("無効な入力です。番号を入力してください。")
        elif choice == "4":
            print("ゲームを終了します。")
            return
        else:
            print("無効な入力です。1, 2, または 3 を入力してください。")

if __name__ == "__main__":
    main()

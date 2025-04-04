from MyMonster import MyMonster
from EnemyMonster import EnemyMonster

def main():
    # 味方キャラクターと敵キャラクターを作成
    me = MyMonster(name="味方キャラ", hp=100, max_hp=100, strength=20, defense=5)

    while True:
        enemy = EnemyMonster(name="敵キャラ", hp=80, max_hp=80, strength=15, defense=3)

        # 戦闘ループ
        while not me.is_defeated and not enemy.is_defeated:
            me.attack(enemy)
            if enemy.is_defeated:
                print("戦闘に勝利しました！")
                break
            enemy.attack(me)
            if me.is_defeated:
                print("戦闘に敗北しました...")
                return

        # 戦闘終了後の選択肢
        while True:
            print("\n次の行動を選択してください:")
            print("1: 次の戦闘を開始する")
            print("2: 休憩して体力を回復する")
            print("3: ゲームを終了する")
            choice = input("選択肢を入力してください (1/2/3): ")

            if choice == "1":
                break  # 次の戦闘を開始
            elif choice == "2":
                me.hp = me.max_hp
                print(f"{me.name} の体力が全回復しました！")
            elif choice == "3":
                print("ゲームを終了します。")
                return
            else:
                print("無効な入力です。1, 2, または 3 を入力してください。")

if __name__ == "__main__":
    main()

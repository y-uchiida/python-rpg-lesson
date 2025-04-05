from item import Item

class StrengthUpItem(Item):
    MAX_ITEM_NUM = 10
    
    def __init__(self):
        self.name = "攻撃力アップアイテム"


    def use(self, monster):
        monster.strength += 5
        print(f"{monster.name} の攻撃力が 5 アップしました！")

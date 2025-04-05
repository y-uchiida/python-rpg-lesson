from item import Item

class DefenseUpItem(Item):
    MAX_ITEM_NUM = 10
    
    def __init__(self):
        self.name = "防御力アップアイテム"


    def use(self, monster):
        monster.defense += 5
        print(f"{monster.name} の防御力が 5 アップしました！")

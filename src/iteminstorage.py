class ItemInStorage:
    """
    アイテムの所持数を管理するクラス
    """

    def __init__(self, item, item_count=0):
        self.item = item
        self.item_count = item_count
        
    def add_item(self, count):
        """
        アイテムの所持数を追加する
        アイテムの所持数が最大値を超えないか確認し、超えない場合は追加する
        """
        if self.item_count + count <= self.item.MAX_ITEM_NUM:
            self.item_count += count
            
    def remove_item(self, count):
        """
        アイテムの所持数を減少させる
        アイテムの所持数が0未満にならないか確認し、0未満にならない場合は減少させる
        """
        if self.item_count - count >= 0:
            self.item_count -= count

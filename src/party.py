from mymonster import MyMonster
from iteminstorage import ItemInStorage

class Party:
    def __init__(self, members):
        self.members = members
        self.item_storage = []

    def add_item_storage(self, item):
        """
        パーティの所有アイテムに、引数で指定されたアイテムを追加する
        """
        # item_storage の中から、追加されたアイテムと同じ種類のアイテムを探す
        # next() を使って、最初に見つかったItemInStorage オブジェクトを取得
        # 追加するアイテムの種類と同じかどうかは、isinstance() と type() を使って確認
        item_in_storage = next(
            (item_in_storage for item_in_storage in self.item_storage if isinstance(item_in_storage.item, type(item))),
            None
        )

        if item_in_storage:
            # アイテムが既に存在する場合、所持数を増加させる
            item_in_storage.add_item(1)
        else:
            # アイテムが存在しない場合、新たにアイテムを追加する
            item_in_storage = ItemInStorage(item, 1)
            self.item_storage.append(item_in_storage)

    def remove_item_storage(self, item):
        """
        パーティの所有アイテムから、引数で指定されたアイテムを減少させる
        """
        # item_storage の中から、減少させるアイテムを探す
        item_in_storage = next(
            (item_in_storage for item_in_storage in self.item_storage if isinstance(item_in_storage.item, type(item))),
            None
        )

        if item_in_storage:
            # アイテムが存在する場合、所持数を減少させる
            item_in_storage.remove_item(1)
            if item_in_storage.item_count == 0:
                # 所持数が0になった場合、アイテムを削除する
                self.item_storage.remove(item_in_storage)

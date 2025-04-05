from abc import ABC, abstractmethod

class Item(ABC):
    MAX_ITEM_NUM = 99  # クラス変数として最大所持数を定義

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def use(self, target):
        pass

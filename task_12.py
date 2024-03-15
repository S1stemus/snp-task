from task_11 import Desert
class Jellybean(Desert):
    def __init__(self, name=None, calories=None,flavor=None):
        super().__init__(name,calories)
        self.flavor=flavor
    @property
    def flavor(self):
        return self.__flavor
    @flavor.setter
    def flavor(self, value):
        self.__flavor = value
    def is_delicious(self):
        if self.flavor=="black licorice":
            return False
        else:
            return True


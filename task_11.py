class Dessert:
    def __init__(self, name=None, calories=None):
        if isinstance(name, str) and isinstance(calories, int):
            self.name = name
            self.calories = calories
        else:
            self.name = None
            self.calories = None
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def calories(self):
        return self.__calories
    @calories.setter
    def calories(self, value):
        self.__calories = value
    def is_healthy(self):
        if isinstance(self.calories, (int, float)) and self.calories < 200:  
            return True
        else:
            return False       
    def is_delicious(self):      
        return True


class Human:
    def __init__(self,age:int, health:int, name:str):

        Human._age = age
        Human._health = health
        Human._name = name


    @property
    def age(self):
        return self._age


    @age.setter
    def age(self, value):
        self._age = value


        @property
        def health(self):
            return self._age

        @health.setter
        def heleath(self, value):
            self._heleath = heleath

            @property
            def name(self):
                return self._name

            @name.setter
            def name(self, value):
                self._name = value
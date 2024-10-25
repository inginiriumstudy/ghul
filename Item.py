class Item:
    def __init__(self,sell:int, endurance:int, name:str):

        Item._sell = sell
        Item._endurance = endurance
        Item._name = name


    @property
    def sell(self):
        return self._sell


    @sell.setter
    def sell(self, value):
        self._sell = value


        @property
        def endurance(self):
            return self._endurance

        @endurance.endurance
        def endurance(self, value):
            self._endurance = endurance

            @property
            def name(self):
                return self._name

            @name.setter
            def name(self, value):
                self._name = value
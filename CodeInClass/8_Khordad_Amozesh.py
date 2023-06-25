class A:
    def __init__(self, entry1, entry2) -> None:
        # private
        self.__entry = entry1
        # protected
        self._entry2 = entry2


    def set_entry(self, entry):  # Setter
        self.__entry = entry


    def get_entry(self):  # Getter
        return self.__entry



    def plus(self):
        self.__test()
        self._plus()
        print(self.output)


    def _plus(self):
        # public attr 
        self.output = self.__entry + self._entry2


    def __test(self):
        print("hehehehe!")

a = A(1,2)
a.plus()


# Error
a.__entry
a.__test

# is accessible and changable
a._A__entry
a._A__test

# not error and accessible but hide
a._entry2
a._plus

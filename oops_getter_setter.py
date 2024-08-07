class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

obj = MyClass(8)
obj.show()
print(obj.ten_value)

# ****************************************************************************************************

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
            self._value = new_value/10

obj = MyClass(8)
obj.ten_value=67
obj.show()
print(obj.ten_value)


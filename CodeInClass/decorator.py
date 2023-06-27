def first(number):
    return number

b = first

print(b(2))

def add_num(a, b):
    return a + b

def calculator(func, a, b):
    return func(a, b)

print(calculator(add_num, 12, 15))

# Error string object isn't callable
# print(calculator("abc", 10, 15))


def power(func):
    def inner(*args, **kwargs):
        print("Before function call!")
        print(args, kwargs)
        for i in args:
            if i < 0:
                print(i)
                print("Entry less than zero is not allowed")
                return
        result = func(*args, **kwargs)
        print(f"After function called, result: {result}")
        # result contain dict and tuple from **kwargs and *args
        return result ** 2
    return inner


decorator_function = power(add_num)
print(decorator_function(2, 3))


# Decorator can take some argument as input
def power(power_argument):
    def decorator(function):
        def inner(*args, **kwargs):
            return function(*args, **kwargs) ** power_argument
        return inner
    return decorator

@power(3)
def add_num_power3(a, b):
    return (a + b)

print(add_num_power3(1,2))

# Order of Decorators
def first(func):
    def inner():
        print("*" * 15)
        func()
        print("*" * 15)
    return inner

def second(func):
    def inner():
        print("%" * 15)
        func()
        print("%" * 15)
    return inner

# execute second and then execute first
@first
@second
def func():
    print("hello")

func()


# @staticmethod

#  When function decorated with @staticmethod is called,
#  we don’t pass an instance of the class to it as it is normally done with methods.
#  It means that the function is put inside the class but it cannot access the instance of that class.

# -----------------------------------------------------------------------------
# @classmethod

from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a
	# Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	def display(self):
		print("Name : ", self.name, "Age : ", self.age)

person = Person('ali', 21)
person.display()






# class A:
#     def __init__(self, entry) -> None:
#         self.set_entry(entry)


#     def set_entry(self, value):
#         print("set entry")
#         self._entry = value

#     def get_entry(self):
#         print("get entry")
#         return self._entry

#     @property
#     def entry_power(self):
#         return self._entry ** 2



# a = A(10)
# a.get_entry()
# print(a.entry_power)


# ---------------------------------------------------------------------------------------





class A():
    abbas = 1
    def __init__(self, entry1) -> None:
        self.entry = entry1
    @property
    def entry(self):
        print("get_entry")
        return self._entry
    @entry.setter
    def entry(self, value):
        print("set_entry")
        self._entry = value
    @staticmethod
    def add(a, b):
        return a + b
    @property
    def entry_sqr(self):
        print(self.entry ** 2)
    @classmethod
    def func1(cls, input):
        return cls(input * cls.abbas)
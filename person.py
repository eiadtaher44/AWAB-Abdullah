class Person:
    def __init__(self, age):
        self.__age = age

        if age < 0:
            raise Exception("Age cannot be negative")

    def get_age(self):
        return self.__age


def main():
    try:
        p1 = Person(20)
        print("Age:", p1.get_age())

        p2 = Person(-5)

    except Exception as e:
        print("Error:", e)


main()

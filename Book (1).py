class Book:
    def __init__(self, name, author, publication_date, quantity):
        self.name = name
        self.author = author
        self.__publication_date = publication_date
        self.quantity = quantity

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("الكمية غير كافية")

    def print_info(self):
        print("اسم الكتاب:", self.name)
        print("اسم الكاتب:", self.author)
        print("تاريخ النشر:", self.__publication_date)
        print("الكمية المتبقية:", self.quantity)
        print("-" * 30)


# إنشاء 5 كائنات بقيم مختلفة
book1 = Book("Python", "Ahmed", 2020, 10)
book2 = Book("C++", "Mohammed", 2019, 5)
book3 = Book("Java", "Ali", 2021, 8)
book4 = Book("HTML", "Omar", 2022, 12)
book5 = Book("Database", "Khaled", 2018, 6)

# زيادة كمية الكتاب الأول
book1.increase_quantity(5)

# إنقاص كمية الكتاب الثاني
book2.decrease_quantity(2)

# طباعة بيانات الكتب الخمسة
book1.print_info()
book2.print_info()
book3.print_info()
book4.print_info()
book5.print_info()

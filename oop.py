# OOP - Object Oriented Programming (Obyektga Yo'naltirilgan Dasturlash)
# OOP dasturlash paradigmasi bo'lib, unda dastur obyektlar atrofida tashkil etiladi.
# Obyektlar - bu ma'lumotlar (xususiyatlar) va funksiyalar (metodlar) to'plami bo'lib, ular birgalikda ishlaydi.


# OOP ning asosiy tushunchalari:
# 1. Sinflar (Classes): Sinf - bu obyektlarning shabloni yoki andozasi. U xususiyatlar va metodlarni aniqlaydi.
# 2. Obyektlar (Objects): Obyekt - bu sinfning konkret namunasidir. Har bir obyekt o'zining xususiyatlariga ega bo'lishi mumkin.
# 3. Meros (Inheritance): Meros - bu bir sinfning boshqa sinfdan xususiyatlar va metodlarni olishi.
# 4. Polimorfizm (Polymorphism): Polimorfizm - bu bir nechta sinflar bir xil metod nomiga ega bo'lishi mumkinligi.
# 5. Inkapsulatsiya (Encapsulation): Inkapsulatsiya - bu ma'lumotlarni va metodlarni birlashtirish va ularni tashqi kirishdan himoya qilish.

# OOP dasturlashning asosiy afzalliklari:
# - Kod qayta foydalanish: Sinflar va obyektlar qayta ishlatilishi mumkin.
# - Kod tuzilishi: OOP kod tuzilishini yaxshilaydi va uni o'qishni osonlashtiradi.
# - Murakkab tizimlarni boshqarish: OOP murakkab tizimlarni modullarga bo'lish orqali boshqarishni osonlashtiradi.



# Quyida Python dasturlash tilida OOP ning asosiy tushunchalarini ko'rsatadigan oddiy misol keltirilgan:
class Animal:
    def __init__(self, name):  # Konstruktor
        # inkapsulatsiya uchun xususiyatni private qilish mumkin:
        # self.__name = name  # private xususiyat
        self._name = name  # Xususiyat
    
    def set_name(self, name):  # Setter metod
        self._name = name
    
    def get_name(self):  # Getter metod
        return self._name
    

    def speak(self):  # Metod
        return f"{self._name} makes a sound."


class Dog(Animal):  # Meros olish
    def speak(self):  # Polimorfizm
        return f"{self.name} barks."
    
    
class Cat(Animal):  # Meros olish
    def speak(self):  # Polimorfizm
        return f"{self.name} meows."
    
    
# Obyektlar yaratish
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Metodlarni chaqirish
# print(dog.speak())  # Output: Buddy barks.
# print(cat.speak())  # Output: Whiskers meows.




















class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Salom, {self.name}")
        
    def check_age(self, min_age=15):
        if self.age >= min_age:
            print("Siz katta odamsiz")
        else:
            print("Siz kichkina odamsiz")


abdulloh = Human(name="Abdulloh", age=13)
ubaydulloh = Human(name="Ubaydulloh", age=16)



# abdulloh.greeting()
# ubaydulloh.greeting()


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"Ismi: {self.name}\nYoshi: {self.age}\nBahosi: {self.grade}")



student1 = Student(age=16, name="Palonchi", grade=3)
student2 = Student(age=22, name="Pistonchi", grade=4)
student3 = Student(age=18, name="Handalak", grade=5)



class Product:
    def __init__(self, name, price, stock=1):
        pass
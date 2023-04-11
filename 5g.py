#classlar - start

#link : https://www.youtube.com/watch?v=SrijG7nULpw

#adım 1

# class Human():
#     name = "irem"
#     def talk(self , sentence):
#         print(f"{self.name}: {sentence}")   #self.name yazıyoruz böylece o classın içerisindeki isme işaret ettiğini anlıyoruz.
#     def walk(self):
#         print("Human is walking..")


# #instance => örnek

# human1 = Human()
# human1.talk("Merhaba") #rezerve ettiği parametreyi atadı
# human1.walk()


#adım 2

# class Human():
#     name = "irem"
#     def talk(self , sentence):
#         print(f"{self.name}: {sentence}")   
#     def walk(self):
#         print(f"{self.name} is walking..")

# human1 = Human()    
# human1.name = "tıkız"   #human1 içine yazdığımız isim geçerli olmuş oluyor.
# human1.talk("Merhaba") 
# human1.walk()

# human1 = Human()
# human1.name = "tobi"   
# human1.talk("Selam") 
# human1.walk()

#adım 3

# class Human():
#     #built in
#     #constructor
#     #initialize
#     def __init__(self):
#         print("Bir human instance'ı üretildi.")
#     name = "irem"
#     def talk(self , sentence):
#         print(f"{self.name}: {sentence}")   
#     def walk(self):
#         print(f"{self.name} is walking..")


# human1 = Human()    #üretim gerçekleştiğinde yapıcı blok çalışmış oluyor.
# human1.name = "tıkız"   
# human1.talk("Merhaba") 
# human1.walk()

# human1 = Human()
# human1.name = "tobi"   
# human1.talk("Selam") 
# human1.walk()

#adım 4

# class Human():
#     #built in
#     #constructor
#     #initialize
#     def __init__(self,name):
#         self.name = name
#         print("Bir human instance'ı üretildi.")
#     name = "irem"
#     def talk(self , sentence):
#         print(f"{self.name}: {sentence}")   
#     def walk(self):
#         print(f"{self.name} is walking..")


# human1 = Human("irem")    
# human1.talk("Merhaba") 
# human1.walk()

# human1 = Human("tobi")  
# human1.talk("Selam") 
# human1.walk()

#adım 5

class Human():
    def __init__(self,name):
        self.name = name
        print("Bir human instance'ı üretildi.")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    name = "irem"
    def talk(self , sentence):
        print(f"{self.name}: {sentence}")   
    def walk(self):
        print(f"{self.name} is walking..")


human1 = Human("irem")    
human1.talk("Merhaba") 
human1.walk()
print(human1) #return'le yazdığımız fonksiyon burada çıkıyor.

human1 = Human("tobi")  
human1.talk("Selam") 
human1.walk()

Human("Selin").talk("merhaba")

#classlar - end

#modules - start

#matematik.py dosyasına aşağıdaki kodları yazdım

# def topla(a,b):
#     return a+b
# def bol(a,b):
#     return a/b

#burada yazdıklarımızı bu dosyaya import edebilmemiz için

# import matematik

# print(matematik.topla(10,20))

#alias
#import matematik as m
import random #python'ın bizim için özel olarak üretmiş olduğu kütüphaneler (built-in moduller)

#print(m.topla(10,20))

print(random.randint(0,100))

# from matematik import topla #o module den bir kısmını almak istediğimizde

# print(topla(10,20))

from matematik import topla as top  #isimlendirme verebiliyoruz

print(top(10,20))

#human1 = Human("köpük")
#human1.talk("Merhaba")     class yazdığımız dosya başka bir yerde olsaydı bu şekilde alabilirdik



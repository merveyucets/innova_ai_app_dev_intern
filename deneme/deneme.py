# 1) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
import random
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

for deger in my_dictionary.values():
    if deger == 'c':
        print(f'{deger} anahtarının değeri: c')
    else:
        print('değeri c değildir.')


# 2) Aşağıdaki listedeki sayılardan sadece çift sayı olanları başka bir listeye kaydeden bir kod yazınız.

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

odd_numbers = []
for i in my_numbers:
    if i%2 == 0 :
        odd_numbers.append(i)
print(odd_numbers)


# 3) Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.

r_list = [3,2,5,8,4,6,9,12]
pi=3.14
c_list =[]
for i in r_list:
    c_list.append(2*pi*i)
print(c_list)

# 4) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur. Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.

age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
age_only =[]
for i in age_name_list:
    age_only.append(i[1])
print(age_only)
# 5) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız

metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]

print(random.choice(metal_list))

# 6) Aşağıdaki kodun çıktısı ne olacaktır?

number_list = [5,7,18,21,20,10,405,24]

[num % 2 == 0 for num in number_list]
#true or false yanıt verir.

#7) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz

barcodeList = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]

xyz_barcodes = []
for barcode in barcodeList:
    if 'XYZ' in barcode:
        xyz_barcodes.append(barcode)
print(xyz_barcodes)
#8) Aşağıda yazdırılan sınıfı incelediğinizde my_cat.multiply_age() kodunun çıktısı ne olacaktır?


class Cat:
    def __init__(self, name, age=5):
        self.name = name
        self.age = age

    def multiply_age(self):
        return self.age * 3

my_cat = Cat("Whiskers")
print(my_cat.multiply_age())
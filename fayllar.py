# def sezar_shifrlash(tekst, kalit):
#     shifrlangan_tekst = ""

#     for harf in tekst:
#         if harf.isalpha():  
#             boshlangich_qiymat = ord('a') if harf.islower() else ord('A')
#             harf_o_rni = ord(harf) - boshlangich_qiymat
#             yangi_o_rin = (harf_o_rni + kalit) % 26
#             yangi_harf = chr(boshlangich_qiymat + yangi_o_rin)
#             shifrlangan_tekst += yangi_harf
#         else:
#             shifrlangan_tekst += harf

#     return shifrlangan_tekst


# xabar = "Salom Dunyo"
# siljitish_soni = 3

# shifrlangan = sezar_shifrlash(xabar, siljitish_soni)
# print(f"Asl xabar: {xabar}")
# print(f"Kalit (shift): {siljitish_soni}")
# print(f"Shifrlangan xabar: {shifrlangan}")


# deshifrlangan = sezar_shifrlash(shifrlangan, -siljitish_soni)
# print(f"Deshifrlangan xabar: {deshifrlangan}")





# fayl = open('misol.txt', 'w')  
# fayl.write('real vs refere!\n')  
# fayl.write("bu o'yinda real yutqizdi.\n")
# fayl.close()



# fayl = open('misol.txt', 'r')    
# kontent = fayl.read()  
# print(kontent)  
# fayl.close()




# with open("", "w") as fayl:
#     while True:
#         matn = input("ism kiriting:>")
#         if matn == "q" or matn == "quite":
#             break
        
    
    
#     fayl.write( + "\n")

# print("dastur tugadi. matn.txt faylga qarang!")    










def get_name():
    name = input("ismimngizni kiriting:>").replace(" ", "")
    return name

def get_fav_fruits():
    fruits = []
    print("yoqtirgan meva nomini kiriting(chiqish uchun q yoki quit)")
    while True:
        fruit = input(">>>")
        if fruit == "q" or fruit == "quit":
            break

        fruits.append(fruit)
    return fruits

def create_file_with_name(name: str):
    f = open(name + ".txt", "w")
    f.close()

def file_file_with_data(fruits: list, file_name: str):
    with open(file_name + ".txt", "a") as file:
        for fruit in fruits:
            file.write(str(fruit) + "\n")
    print("malumotlar yoziladi")        

def read_data(file_name: str):
    import os
    is_exist = os.path.exsits(file_name + ".txt")
    if not is_exist:
        return False
    with open(file_name + ".txt", "r") as file:
        data = file.read()
        return data
    

def main():
    name = get_name()
    fruits = get_fav_fruits()
    create_file_with_name(name)
    file_file_with_data(fruits, name)
    print("faylni o'qishni xolaysizmi?")
    yes_or_no =input("(yes/no)>>>")
    if yes_or_no.lower() == "yes":
        data = read_data(name)
        if not data:
            print("bunday fayl topilmadi")
        else:
            print(data)
    print("dastur tugadi")

main()

from random import randint



def main():
    greeting()
    random_number = get_random_number()
    
    
    while True:
        
        input_number = get_number_from_user()
        
        if input_number == 0:
            break
    
        hint = get_hint(random_number, input_number)
    
        if hint == "imkoniyat 3 taga teng":
            print("sizning son taxminingiz 3 taga teng")
            break
        elif hint == "kichik":
            print("Men o'ylagan son kichik siz kiritgan sondan")
            continue
        elif hint == "katta":
            print("Men o'ylagan son katta siz kiritgan sondan")
            continue
        elif hint == "teng":
            print("Tabriklayman siz yutdingiz!")
            print("Yana kutib qolamiz")
            break
            
        
        

def greeting():
    print("""
    Assalomu alaykum
    Omad o'yiniga xush kelibsiz
    men son o'ylayman siz topasiz!
    son o'yladim men. uni toping
    """)


def get_random_number(from_ = 1, _to = 10):
    return randint(from_, _to)


def get_number_from_user():
    print("Son kiriting:>>")
    return int(input())

def get_hint(random_number: int, input_number: int):
    if random_number > input_number:
        return "katta"
    elif random_number < input_number:
        return "kichik"
    else:
        return "teng"


main()

kontaktlar = {}

def kontakt_qoshish(ism, raqam):
    kontaktlar[ism] = raqam
    print(f"Kontakt '{ism}' muvaffaqiyatli qo'shildi.")

def kontaktlarni_korish():
    if not kontaktlar:
        print("Kontaklar ro'yxati bo'sh.")
        return

    print("\n Barcha Kontaktlar ")
    saralangan_kontaktlar = sorted(kontaktlar.items())
    for ism, raqam in saralangan_kontaktlar:
        print(f"Ism: {ism:<15} Raqam: {raqam}")


def kontakt_ochirish(ism):
    if ism in kontaktlar:
        del kontaktlar[ism]
        print(f"Kontakt '{ism}' muvaffaqiyatli o'chirildi.")
    else:
        print(f"Xatolik: Kontakt '{ism}' topilmadi.")
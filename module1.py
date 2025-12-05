# 6-topshiriq

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
# natija = faktorial(5)
# print("faktorial:>", natija)

# 7-topshiriq

def fibonachi(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + fibonachi(n - 1)
# natija = fibonachi(5)
# print("fibonachi:>", natija)

# 8-topshiriq

def to_uppercase(s):
    return s.upper()
# natija = to_uppercase("ishlar qale")
# print("natija:>", natija)
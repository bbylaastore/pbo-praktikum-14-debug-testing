
def divide(a, b):
    return a / b

def main():
    print("=== DEBUG PRAKTIKUM 14 ===")
    try:
        x = int(input("Masukkan angka pertama: "))
        y = int(input("Masukkan angka kedua: "))
        result = divide(x, y)
        print("Hasil:", result)
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol!")
    except ValueError:
        print("Error: Input harus angka!")

if __name__ == "__main__":
    main()

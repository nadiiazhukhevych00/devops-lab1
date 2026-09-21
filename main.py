# main.py
# Головний файл, який імпортує функції з lib.py

from lib import calculate_sum, calculate_product

def main():
    x = 5
    y = 3
    
    total_sum = calculate_sum(x, y)
    total_product = calculate_product(x, y)
    
    print(f"Сума {x} та {y} дорівнює: {total_sum}")
    print(f"Добуток {x} та {y} дорівнює: {total_product}")

if __name__ == "__main__":
    main()
import random

def ukrainian_alphabet():
    # Повний український алфавіт, включаючи всі літери
    return 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя '

def create_homophones():
    """
    Створення таблиці гомофонів для кожної літери, включаючи пробіли.
    """
    alphabet = ukrainian_alphabet()
    homophones = {}
    base_num = 10  # Початок нумерації гомофонів

    # Для кожної літери створюється список гомофонів
    for i, letter in enumerate(alphabet):
        # Додаємо по 3 гомофони для кожної літери
        homophones[letter] = [str(base_num + j) for j in range(i * 3, (i + 1) * 3)]
    
    return homophones

def gronsfeld_encrypt(text, homophones):
    """
    Шифрування тексту за допомогою гомофонів.
    """
    encrypted_text = []

    for char in text.lower():
        if char in homophones:
            # Вибираємо випадковий гомофон для літери
            encrypted_char = random.choice(homophones[char])
            encrypted_text.append(encrypted_char)
        else:
            # Якщо символ не в алфавіті, додаємо його без змін
            encrypted_text.append(char)
    
    return ' '.join(encrypted_text)

def gronsfeld_decrypt(encrypted_text, homophones):
    """
    Розшифрування тексту за допомогою таблиці гомофонів.
    """
    # Створюємо зворотну таблицю для розшифрування
    reverse_homophones = {}
    for letter, codes in homophones.items():
        for code in codes:
            reverse_homophones[code] = letter
    
    decrypted_text = []

    # Розбиваємо зашифрований текст по пробілах
    encrypted_parts = encrypted_text.split()
    
    for part in encrypted_parts:
        if part in reverse_homophones:
            decrypted_text.append(reverse_homophones[part])
        else:
            decrypted_text.append(part)
    
    return ''.join(decrypted_text)

# Створення таблиці гомофонів
homophones = create_homophones()

# Виведення таблиці гомофонів для ознайомлення
print("Таблиця гомофонів:")
for letter, codes in homophones.items():
    print(f"{letter}: {', '.join(codes)}")

# Введення тексту з клавіатури
text = input("Введіть текст для шифрування: ")

# Шифрування
encrypted_text = gronsfeld_encrypt(text, homophones)
print("\nЗашифрований текст:", encrypted_text)

# Запит на розшифрування
choice = input("\nБажаєте розшифрувати текст? (так/ні): ").strip().lower()
if choice == 'так':
    decrypted_text = gronsfeld_decrypt(encrypted_text, homophones)
    print("\nРозшифрований текст:", decrypted_text)
else:
    print("\nРозшифрування не було виконано.")

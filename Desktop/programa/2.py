def ukrainian_alphabet():
    return 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя'

def gronsfeld_encrypt(text, key):
    alphabet = ukrainian_alphabet()
    key = [int(k) for k in str(key)]
    encrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(text.lower()):
        if char in alphabet:
            index = alphabet.index(char)
            shift = key[i % key_length]  # Вибір відповідної цифри з ключа
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char  # Якщо символ не в алфавіті, залишаємо його без змін

    return encrypted_text

def gronsfeld_decrypt(encrypted_text, key):
    alphabet = ukrainian_alphabet()
    key = [int(k) for k in str(key)]
    decrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(encrypted_text.lower()):
        if char in alphabet:
            index = alphabet.index(char)
            shift = key[i % key_length]
            new_index = (index - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char  # Якщо символ не в алфавіті, залишаємо його без змін

    return decrypted_text

# Введення даних з клавіатури
text = input("Введіть текст для шифрування: ")
key = input("Введіть числовий ключ (наприклад, 531): ")

# Шифрування
encrypted_text = gronsfeld_encrypt(text, key)
print("\nЗашифрований текст:", encrypted_text)

# Запит на розшифрування
choice = input("\nБажаєте розшифрувати текст? (так/ні): ").strip().lower()
if choice == 'так':
    decrypted_text = gronsfeld_decrypt(encrypted_text, key)
    print("\nРозшифрований текст:", decrypted_text)
else:
    print("\nРозшифрування не було виконано.")

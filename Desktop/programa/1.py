import math
import random

def create_matrix(text, rows, cols):
    # Доповнення тексту пробілами до повного розміру матриці
    padded_text = text.ljust(rows * cols)
    matrix = [list(padded_text[i * cols:(i + 1) * cols]) for i in range(rows)]
    return matrix

def sort_key_indices(key):
    # Отримання індексів літер в алфавітному порядку
    return sorted(range(len(key)), key=lambda k: key[k])

def permute_rows(matrix, row_order):
    # Перестановка рядків за заданим порядком
    return [matrix[i] for i in row_order]

def permute_columns(matrix, col_order):
    # Перестановка стовпців за заданим порядком
    return [[row[i] for i in col_order] for row in matrix]

def display_matrix(matrix, col_key, row_key, message, col_order=None, row_order=None):
    print(f"\n{message}:")
    if col_order:
        col_key = ''.join(col_key[i] for i in col_order)
    print("    ", ' '.join(col_key))
    print("    ", ' '.join('-' * len(col_key)))
    if row_order:
        row_key = ''.join(row_key[i] for i in row_order)
    for rk, row in zip(row_key, matrix):
        print(f"{rk} | {' '.join(row)}")
    print()

def generate_key(length):
    # Генерація випадкового ключа заданої довжини з українських літер
    alphabet = 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя'
    key = ''.join(random.sample(alphabet, length))
    return key

def encrypt(text):
    # Визначення розмірів матриці
    length = len(text)
    cols = math.ceil(math.sqrt(length))  # Визначення кількості стовпців (корінь з довжини тексту)
    rows = math.ceil(length / cols)  # Визначення кількості рядків
    
    # Генерація ключових слів для стовпців та рядків
    col_key = generate_key(cols)
    row_key = generate_key(rows)
    
    # Створення матриці з тексту
    matrix = create_matrix(text, rows, cols)
    display_matrix(matrix, col_key, row_key, "Матриця перед перестановкою")
    
    # Отримання індексів для перестановки на основі ключів
    col_order = sort_key_indices(col_key)
    row_order = sort_key_indices(row_key)
    
    # Перестановка стовпців у алфавітному порядку ключа
    matrix = permute_columns(matrix, col_order)
    display_matrix(matrix, col_key, row_key, "Матриця після перестановки стовпців", col_order=col_order)
    
    # Перестановка рядків у алфавітному порядку ключа
    matrix = permute_rows(matrix, row_order)
    display_matrix(matrix, col_key, row_key, "Матриця після перестановки рядків", row_order=row_order)

    # Формування зашифрованого тексту
    encrypted_text = ''.join([''.join(row) for row in matrix])
    return encrypted_text.strip(), col_key, row_key

def decrypt(encrypted_text, col_key, row_key):
    rows = len(row_key)
    cols = len(col_key)
    
    # Створення матриці з зашифрованого тексту
    matrix = create_matrix(encrypted_text, rows, cols)
    display_matrix(matrix, col_key, row_key, "Матриця перед розшифруванням")
    
    # Отримання обернених індексів для перестановок
    col_order = sort_key_indices(col_key)
    row_order = sort_key_indices(row_key)
    inverse_col_order = sorted(range(len(col_order)), key=lambda k: col_order[k])
    inverse_row_order = sorted(range(len(row_order)), key=lambda k: row_order[k])
    
    # Обернена перестановка рядків
    matrix = permute_rows(matrix, inverse_row_order)
    display_matrix(matrix, col_key, row_key, "Матриця після оберненої перестановки рядків", row_order=inverse_row_order)
    
    # Обернена перестановка стовпців
    matrix = permute_columns(matrix, inverse_col_order)
    display_matrix(matrix, col_key, row_key, "Матриця після оберненої перестановки стовпців", col_order=inverse_col_order)

    # Формування розшифрованого тексту та обрізання зайвих пробілів
    decrypted_text = ''.join([''.join(row) for row in matrix]).strip()
    return decrypted_text

# Введення даних з клавіатури
text = input("Введіть текст для шифрування: ")

# Виконання шифрування
encrypted_text, col_key, row_key = encrypt(text)
print("\nЗашифрований текст:", encrypted_text)


# Запит на розшифрування
choice = input("\nБажаєте розшифрувати текст? (так/ні): ").strip().lower()
if choice == 'так':
    decrypted_text = decrypt(encrypted_text, col_key, row_key)
    print("\nРозшифрований текст:", decrypted_text)
else:
    print("\nРозшифрування не було виконано.")

# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок

initial_text = input("Введите текст: ")
string_to_find = input("Задайте строку: ")
result = [i for i in initial_text.split() if string_to_find not in i]
print(" ".join(result))

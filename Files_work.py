#  Создание переменной, в которой путь к файлу
inputfile = "../name.txt"
# Открытие файла. Выбор в каком режиме открыть файл. Пока только чтение
myfile = open(inputfile, mode='r', encoding='latin_1')
# Чтение файла, который был указан
# print(myfile.read())
# Вывод студентов с номерами строк по порядку, начиная с 1
for num, line in enumerate(myfile, 1):
    print("Student № " + str(num) + ": " + line.strip())

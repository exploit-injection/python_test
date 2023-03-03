#  Создание переменной, в которой путь к файлу
inputfile = "../name.txt"
# Открытие файла. Выбор в каком режиме открыть файл. Пока только чтение
myfile = open(inputfile, mode='r', encoding='latin_1')
# Чтение файла, который был указан
print(myfile.read())
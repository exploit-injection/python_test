#  Создание переменной, в которой путь к файлу
inputfile = "../password.txt"
#  Создание переменной для нового файла, куда будет производиться запись
outputfile = "../my_password.txt"

password_tolookfor = "vasya"
# Открытие файла. Выбор в каком режиме открыть файл. Пока только чтение
myfile = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='w', encoding='latin_1')
# Если поставить mode=a (append), то будет добавление данных к созданному файлу, не перезапись
# Чтение файла, который был указан

for num, line in enumerate(myfile, 1):
    #  Вывод всех паролей, в которых есть vasya
    if password_tolookfor in line:
        print("Line № " + str(num) + ": " + line.strip())
        myfile2.write("Found password:  " + line)

myfile.close()
myfile2.close()


import translater
import random
import logging


def f_load():
    choice_f = input('файл или csv :')
    if choice_f == 'файл':
        file_list = translater.load_rus()  
        return file_list
    elif choice_f == 'csv':
        name_file = input('введите имя файла csv :')
        file_list = translater.load_csv_list(name_file)
        return file_list

my_list = []


while True:
    ch = ['exit', 'load', 'tran', 'save', 'show']
    print('--------------------------------------------------------------------------------------------------------')
    print(f'{ch[0]} -выход | {ch[1]} - загрузка | {ch[2]} -перевод | {ch[3]} -сохранить | {ch[4]} -показать')
    choice = input('выберите действие :')
    print()
    if choice == ch[0]: #выход
        break

    elif choice == ch[1]: #загрузка
        list_word = f_load()
        my_list = list_word
        print(list_word)
        print(len(list_word))

    elif choice == ch[2]: #Перевод
        try:
            tran = translater.translater(my_list)
            print(tran)
            my_list = tran
        except NameError:
            print('---------------------')
            print('Нет исходного текста')
            print('---------------------')

    elif choice == ch[3]: #сохранение
        try:
            my_list = []
            data = [['ru','eng'],]
            for word in tran:
                data.append(word)
            fieldnames = data[0]
            for values in data[1:]:
                inner_dict = dict(zip(fieldnames, values))
                my_list.append(inner_dict)
            path = input('введите имя файла для сохранения :')
            translater.save_word(path, fieldnames, my_list)
        except NameError:
            print('---------------------')
            print('нет данных для записи')
            print('---------------------')

    elif choice == ch[4]: #Показать
        try:
            print(my_list)
            logging.basicConfig(filename="MyLog.log", level=logging.INFO)
            logging.info(my_list[random.randint(0,len(my_list)-1)])
            print(my_list[random.randint(0,len(my_list)-1)])
            print(my_list[random.randint(0,len(my_list)-1)])
            print(my_list[random.randint(0,len(my_list)-1)])
        except ValueError:
            print('---------------------')
            print('Нет загруженного текста')
            print('---------------------')
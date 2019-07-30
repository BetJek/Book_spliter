import csv
import random
import pickle
import google_1

def load_rus():
    '''функция загрузки текста книги из файла \n
    спашивает имя файла, выводит длину файла, \n
    тип возвращаемого файла(list)
    '''
    try:
        rus='йцукенгшщзхъфывапролджэячсмитьбю'
        name=input('введите имя файла ')
        print('          {0} -  файл загружается' .format(name))
        with open(name,'r') as file:
            file=file.read()
            print('          {0} -  файл загружен' .format(name))
        f=lambda s: ''.join((c for c in s if c in rus or c is ' ')).replace(' ',',')
        f=f(file)
        file=f.split(',')
        file=list(set(file))
        len_translate=len(file)    
        print('          Длина файла {0} = {1} слов'.format(name,len_translate) )
        print(type(file))
        return file

    except(ValueError):
        print('нет такого файла')
        return 0

def load_rus_2():
    '''функция загрузки текста из файла разбитого по строкам \n
    спашивает имя файла, выводит длину файла, \n 
    тип возвращаемого файла(list) и первое вхождение
    '''
    try:
        print(' файл загружается')
        file = open('рус.txt','r')
        file = file.read()
        print(' файл загружен')

        file = file.split('\n')
        print(len(file))
        file = set(file)
        file = list(file)

        len_translate = len(file) 
        print('Длина файла {} слов'.format(len_translate) )
        print(type(file))
        print(file[1])

        return file

    except(ValueError):
        print('нет такого файла')
        return 0


def write_rus(rus_text_list):
    '''записывает слова из списка в файл'''
    try:
        with open('рус.txt', 'w') as rus:
            for word in rus_text_list:
                rus.writelines(word + '\n')
        return 1
    except:
        return 0



def print_word(textv):
    '''Печатает 40 переводов от указанного\n
    принимает на вход список из слово=перевод
    '''
    try:
        a=int(input())
        print(textv[0])
        print('------------')
        for i in range(40):
            print(textv[a+i]+'= '+str(a+i))
        return 'ok'
    except(ValueError):
        print('неправитльный файл')
        return 'bad'


def load_eng():
    ''' читает переведенные слова из файла eng
    '''
    try:
        with open('eng.txt', 'r') as eng:
            text = eng.read()
            text = text.replace(' ', ',').replace('\n', ',').split(',')
            print(text[0:10])
        return text

    except:
        return 0


def translater(text):
    '''переводит слова через гугл'''
    translate_text = []
    for word in text:
        tr_word = google_1.translate(word)
        translate_text.append([word,tr_word['data']['translations'][0]['translatedText']])
    return translate_text


def save_word(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def load_csv(path):
    """
    Read a CSV file using csv.DictReader
    возвращает список кортежей ключ/значение
    """
    translate_list =[]
    with open(path, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for word in reader:
            translate_list.append(word)
    return translate_list


def load_csv_list(path):
    '''переводит список словарей читаемый из csv
    в спискок списков 
    '''
    list_tupl = load_csv(path)
    list_words = []
    for word in list_tupl:
        list_words.append([word['ru'],word['eng']])
    return list_words

#f = load_csv_list('translate.csv')
#print(f)



'''
f = load_csv('translate.csv')

print(f[0]['ru'])
 '''

'''
if __name__ == "__main__":
    data = [['ru','eng'],]
    f = translater(load_rus_2())
    for word in f:
        data.append(word)
    
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    
    path = "translate.csv"
    save_word(path, fieldnames, my_list)
'''
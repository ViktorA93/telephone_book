# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Рабочий txt- файл для записи контактов
filename_work = "phon.txt" # при указании файла если не указываем абсодютный адрес, 
# то требуется открывать (open folder) именно ту директорию в которой этот файл находится

# Работа с телефонной книгой
def work_with_phonebook():
    choice=show_menu() # вызывает функцию show_menu()
    phone_book = read_txt(filename_work) # работа с текстовым файлом, 
# если файл находится в одной директории с нашей программой, то указывать путь не требуется

    while (choice!=7):
        if choice==1:
            display_contacts(phone_book) # +++ Отображаем телефонную книгу

        elif choice==2:
            search_record(phone_book)
            

        elif choice==3: # +++ Добавляем абонента в тел книгу
            add_contact(phone_book)
            
        elif choice==4: # +++ Сохраняем изменения в файл
            write_txt(filename_work , phone_book)
            

        choice=show_menu()

# +++Отображаем наше меню
def show_menu(): 
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n" #+
          "2. Найти абонента по фамилии, имени или номеру телефона\n" #+
          "3. Добавить абонента в справочник\n" # +
          "4. Сохранить справочник в текстовом формате\n" #+
          )
    choice = int(input('Введите цифру интересующего действия: ')) # вводим с консоли цифру и он воспринимает её
    return choice

# +++Функция для чтения файла
def read_txt(filename_work): 

    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename_work,'r', encoding='utf-8') as file: # при использовании with нам не требуется принудительно закрывать его
        for line in file:
            if line.strip() != '': # условия для пропуска пустых строк в словаре
                record = dict(zip(fields, line.strip().split('; '))) 
            #line.split(',') = [Питонов,    Антон,     '777',    'умеет в Питон']
			#dict(( (фамилия,Иванов),(имя, Игорь),(номер,8928) ))	     
                phone_book.append(record)
            continue # иначе если строка путая переходим к след. элементу line
    return phone_book

# +++Функция для записи в файл
def write_txt(filename_work , phone_book):
    with open(filename_work,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + '; '
            phout.write(f'{s[:-2]}\n')

# +++Отобразить весь справочник
def display_contacts(phone_book):
    for contact in phone_book:
        print(contact)

# +++добавить контакт
def add_contact(phone_book):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_contact = []
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер: ")
    patronymic = input("Введите описание: ")
    new_contact.extend([surname, name, phone, patronymic])
    record = dict(zip(fields, new_contact))
    phone_book.append(record)

# +++функция поиска абонента
def search_record(phone_book):
    search_term = input("Введите фамилию или имя для поиска: ")
    results = [record for record in phone_book if search_term in record.values()]
    if not results:
        print("Записи не найдены.")
    else:
        for record in results:
            print(f"Фамилия: {record['Фамилия']}, Имя: {record['Имя']},  Телефон: {record['Телефон']}, Описание: {record['Описание']}")

# +++вызов самой программы
work_with_phonebook() 
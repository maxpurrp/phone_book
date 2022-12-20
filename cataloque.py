number_books=[]
def work():
    while True:
        command=input().split()
        if command[0]=="add":
            name=command[1]
            number=command[2]
            add_user(number_books,name,number)
            continue
        if command[0]=="delete":
            name=command[1]
            delete_user(number_books,name)
            continue
        if command[0]=="replace":
            if len(command)!=3:
                print("Повторите корректный ввод")
                continue
            if name in number_books.keys():
                name=command[1]
                number=command[2]
                replace_user_in_number_books(number_books,name,number)
                continue
        if command[0]=="show_book":
            show_book(number_books)
            continue
        if command[0]=="exit":
            close_prog()
        if command[0]=="help":
            help_in_number_books()
            continue
        if command[0]=="save":
            save()
            print("Справочник сохранен")
            continue
        else:
            print("Команда не распознана,введите еще раз")
def save():
    print("Хотите добавить в существующий справочник или создать новый?")
    print("<add> or <new>")
    choise=input()
    if choise=="add":
        f=open("C:\\Users\\Максим\\Desktop\\Python\\hollyshit.txt","a")
        for key,value in number_books.items():
            f.write(key + ":" + value + "\n")
        f.close()
    if choise=="new":
        f=open("C:\\Users\\Максим\\Desktop\\Python\\hollyshit.txt","w")
        for key,value in number_books.items():
            f.write(key + ":" + value + "\n")
        f.close()
        print("Данные внесены в справочник")
    else:
        print("Команда не распознана")
def close_prog():
    print("Хотите сохранить справочник?")
    print("yes or no")
    a=input()
    if a=="yes":
        save()
        exit()
    else:
        exit()
def add_user(number_books,name,number):
    if name in number_books.keys():
        print("Абонент уже назписан")
    else:
        number_books[name]=number
        print(name, "добавлен в справочник")
def delete_user(number_books,name):
    if name in number_books:
        number_books.pop(name)
        print(name, "удален из справочника")
    else:
        print("Абонент не записан в справочник")
def replace_user_in_number_books(number_books,name,number):
    if name in number_books.keys():
        number_books[name]=number
        print("Номер изменен")
    else:
        print("Абонент не существует")
def show_book(number_books):
    print("Список имен и их номеров предоставлен ниже")
    for key,value in number_books.items():
            print(key,value)
def help_in_number_books():
    print("add < name > < nubmer > Позволяет добавить номер телефона в справочник")
    print("delete < name > Позволяет удалить номер телефона")
    print("replace < name > < number > Позволяет заменить номер абонента")
    print(" showbook  Позволяет посмотореть содержимое справочника")
    print(" exit  Выход из справочника")
    print(" help  Печать списка с пояснениями")
    print(" save   Сохранить текущую версию справочника")
if __name__=="__main__":
    help_in_number_books()
    work()
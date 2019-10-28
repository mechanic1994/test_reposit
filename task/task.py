import datetime
now = datetime.date.today()
show = 1
create = 2
remove = 3
exit = 4
new_row = []
running = True
list_task = []
while running:
    print(" ")
    print("1 Просмотр задач ")
    print("2 Создать задачу ")
    print("3 Удалить задачу ")
    print("4 Выход ")
    print(" ")
    try:
        activity = abs(int(input("Введите номер пункта для управления: ")))
        if activity > 4 or activity == 0:
            print(" ")
            print("Ошибка ввода! ")
            continue
    except ValueError:
        print(" ")
        print("Это не номер пункта! Попробуйте снова ")
        continue
    if activity == show:
        menu_show = True
        while menu_show:
            number_task = 0
            print("{: ^3}|".format("#"), "{: ^15}|{: ^70}|{: ^10}|\
{: ^20}|".format("Название", "Описание", "Дедлайн", "Статус"))
            print("-------------------------------------------------------\
---------------------------------------------------------------------")
            for row in list_task:
                number_task += 1
                print("{: ^3}|".format(number_task),"{: <15}|{: <70}|{:2}-\
{:2}-{:4}|{: ^20}|".format(row[0], row[1], row[2], row[3], row[4], row[5]))
            try:
                print(" ")
                exit_2 = abs(int(input("Введите '4' для выхода: ")))
                if exit_2 != 4:
                    print(" ")
                    print("Неверное число! Попробуйте снова ")
                    continue
            except ValueError:
                print(" ")
                print("Это не число! Попробуйте снова ")
                continue
            break
    elif activity == create:
        menu_create = True
        while menu_create:
            while True:
                print(" ")
                name = input("Введите название задачи не более 15 символов: ")
                if len(name) > 15:
                    print(" ")
                    print("Имя больше 15 символов! Попробуйте снова ")
                else:
                    break
            while True:
                print(" ")
                description = input("Введите описание задачи не более \
70 символов: ")
                if len(description) > 70:
                    print(" ")
                    print("Описание больше 70 символов! Попробуйте снова ")
                else:
                    break
            while True:
                print(" ")
                print("Введите крайний срок выполнения задачи: ")
                print(" ")
                try:
                    day = abs(int(input("Введите день в формате ДД: ")))
                    print(" ")
                    month = abs(int(input("Введите месяц в формате ММ: ")))
                    print(" ")
                    year = abs(int(input("Введите год в формате ГГГГ: ")))
                    if year < 2019 or year > 9999:
                        print(" ")
                        print("Год меньше текущего или неверный формат! \
Попробуйте снова ")
                        continue
                    elif month > 12 or month == 1:
                        print(" ")
                        print("Несуществующий месяц или неверный формат! \
Попробуйте снова ")
                        continue
                    elif day > 31 or day == 1:
                        print(" ")
                        print("Нет такого дня или неверный формат! \
Попробуйте снова ")
                    deadline = datetime.date(year, month, day)
                    period = deadline - now
                    status_1 = "Задача просрочена"
                    status_2 = "Крайний срок сегодня"
                    status_3 = "Осталось {} дней".format(period.days)
                except ValueError:
                    print(" ")
                    print("Неверный формат! Попробуйте снова")
                    continue
                print(" ")
                break
            new_row.append(name)
            new_row.append(description)
            new_row.append(deadline.day)
            new_row.append(deadline.month)
            new_row.append(deadline.year)
            if deadline == now:
                new_row.append(status_2)
            elif deadline > now:
                new_row.append(status_3)
            elif deadline < now:
                new_row.append(status_1)
            while len(new_row) >= 6:
                part = new_row[:6]
                list_task.append(part)
                new_row = new_row[6:]
            break
    elif activity == remove:
        remove_menu = True
        while remove_menu:
            print(" ")
            number_task = 0
            print("{: ^3}|".format("#"), "{: ^15}|{: ^70}|{: ^10}|\
{: ^20}|".format("Название", "Описание", "Дедлайн", "Статус"))
            print("-------------------------------------------------------\
---------------------------------------------------------------------")
            for row in list_task:
                number_task += 1
                print("{: ^3}|".format(number_task),"{: <15}|{: <70}|{:2}-\
{:2}-{:4}|{: ^20}|".format(row[0], row[1], row[2], row[3], row[4], row[5]))
            try:
                print(" ")
                remove_2 = abs(int(input("Введите номер \
задачи, чтобы удалить её: ")))
                if remove_2 > number_task or remove_2 == 0:
                    print(" ")
                    print("Под таким номером нет задачи! \
Попробуйте снова ")
                    continue
            except ValueError:
                print(" ")
                print("Это не число! Попробуйте снова ")
                continue
            del list_task[remove_2-1]
            break
    elif activity == exit:
        quit()

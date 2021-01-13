import datetime


SHOW = 1
CREATE = 2
REMOVE = 3
EXIT = 4
running = True
list_task = []
DAY = 0
MONTH = 0
YEAR = 0


def show_list_task():
    while True:
        number_task = 0
        print(f"\n{'#': ^3}|{'Название': ^15}|{'Описание': ^70}|{'Дедлайн': ^10}"
              f"|{'Статус': ^20}|")
        print("-" * 124)
        for row in list_task:
            number_task += 1
            print("{: ^3}|{: <15}|{: <70}|{:2}-{:2}-{:4}|"
                 "{: ^20}|\n".format(number_task, *row))
        try:
            exit_2 = abs(int(input("Введите '4' для выхода: ")))
        except ValueError:
            print(" ")
            print("Это не число! Попробуйте снова \n")
            continue
        if exit_2 != 4:
            print("\nНеверное число! Попробуйте снова \n")
            continue
        break


def create_name():
    while True:
        print(" ")
        name = input("Введите название задачи не более 15 символов: ")
        if len(name) > 15:
            print("\nИмя больше 15 символов! Попробуйте снова ")
        else:
            break
    return name


def create_description():
    while True:
        print(" ")
        description = input("Введите описание задачи не более 70 символов: ")
        if len(description) > 70:
            print("\nОписание больше 70 символов! Попробуйте снова ")
        else:
            break
    return description


def create_day():
    global DAY
    while True:
        now = datetime.date.today()
        deadline = datetime.date(now.year, now.month, now.day)
        try:
            print(" ")
            DAY = abs(int(input("Введите день в формате ДД: ")))
            deadline = datetime.date(now.year, now.month, DAY)
        except ValueError:
            print("\nНеверный формат! Попробуйте снова ")
            continue
        break
    return DAY


def create_month():
    global MONTH
    while True:
        now = datetime.date.today()
        try:
            print(" ")
            MONTH = abs(int(input("Введите месяц в формате ММ: ")))
            deadline = datetime.date(now.year, MONTH, DAY)
        except ValueError:
            print("\nНеверный формат! Попробуйте снова ")
            continue
        if deadline < now:
            print("\nПрошедший месяц или неверный формат! Попробуйте снова ")
            continue
        else:
            break
    return MONTH


def create_year():
    global YEAR
    while True:
        now = datetime.date.today()
        try:
            print(" ")
            YEAR = abs(int(input("Введите год в формате ГГГГ: ")))
            deadline = datetime.date(YEAR, MONTH, DAY)
        except ValueError:
            print("\nНеверный формат! Попробуйте снова ")
            continue
        if deadline < now:
            print("\nПрошедший год или неверный формат! Попробуйте снова ")
            continue
        else:
            break
    return YEAR


def create_status():
    now = datetime.date.today()
    deadline = datetime.date(YEAR, MONTH, DAY)
    period = deadline - now
    status_1 = "Задача просрочена"
    status_2 = "Крайний срок сегодня"
    status_3 = "Осталось {} дней".format(period.days)
    if deadline == now:
        return status_2
    elif deadline > now:
        return status_3
    elif deadline < now:
        return status_1


def create_new_task():
    new_row = []
    print("\nВведите крайний срок выполнения задачи ")
    new_row.append(create_name())
    new_row.append(create_description())
    new_row.append(create_day())
    new_row.append(create_month())
    new_row.append(create_year())
    new_row.append(create_status())
    list_task.append(new_row)


def remove_completed_task():
    while True:
        number_task = 0
        print("\n{#: ^3}|{Название: ^15}|{Описание: ^70}|{Дедлайн: ^10}|"
             "{Статус: ^20}|")
        print("-" * 124)
        for row in list_task:
            number_task += 1
            print("{: ^3}|{: <15}|{: <70}|{:2}-{:2}-{:4}|"
                  "{: ^20}|\n".format(number_task, *row))
        try:
            remove = abs(int(input("Введите номер задачи,"
                                   "чтобы удалить её: ")))
        except ValueError:
            print("\nЭто не число! Попробуйте снова ")
            continue
        if remove > number_task or remove == 0:
            print(" ")
            print("Под таким номером нет задачи! Попробуйте снова ")
            continue
        del list_task[remove-1]
        break


while running:
    print("\n"
            "1 Просмотр задач\n"
            "2 Создать задачу\n"
            "3 Удалить задачу\n"
            "4 Выход\n"
          )
    try:
        activity = abs(int(input("Введите номер пункта для управления: ")))
    except ValueError:
        print("\nОшибка ввода! ")
        continue
    if activity not in range(5):
        print("\nЭто не номер пункта! Попробуйте снова ")
        continue
    elif activity == SHOW:
        show_list_task()
    elif activity == CREATE:
        create_new_task()
    elif activity == REMOVE:
        remove_completed_task()
    elif activity == EXIT:
        quit()

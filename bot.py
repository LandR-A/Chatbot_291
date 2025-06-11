import datetime
import json
today = datetime.datetime.today()
weekday = today.weekday()

# Виводить вітальне повідомлення
def greetings():
    print('Вас вітає Бот “Помічник розкладу студента”')
    print('Введіть "Допомога" щоб отримати список команд.')

# Виводить список доступних команд користувача
def help():
    print('Введіть "Розклад на сьогодні" щоб отримати розклад на поточний день.\n'
          'Введіть "Розклад на завтра" щоб отримати розклад на завтрашній день.\n'
          'Введіть "Додати завдання" щоб бот додав предмет, дату виконання, короткий опис.\n'
          'Введіть "Завдання" щоб вивести список всіх актуальних завдань.\n'
          'Введіть "Нагадування" щоб отримати список завдань, які потрібно здати завтра або сьогодні.\n'
          'Введіть "Вийти" щоб завершити роботу бота.')

# Розклад занять на тиждень
schedule = {"Понеділок": ["Українська література", "Схемотехніка"],
            "Вівторок": ["Фізична культура", "Англійська мова", "ОБЗ"],
            "Середа": ["Українська мова", "Інформатика", "Алгоритмізація"],
            "Четвер": ["Математика", "Алгоритмізація", "Мистецтво", "Інформатика"],
            "П'ятниця": ["Математика", "Охорона праці", "Електротехніка"],
            "Субота": [],
            "Неділя": []}

# Список днів тижня
days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']
weekday_d = list(enumerate(days))


# Виводить розклад на поточний день
def schedule_today():
    if schedule[days[weekday]]:
        print("Твій розклад на сьогодні: \n")
        for id, i in enumerate(schedule[days[weekday]]):
            print(f"Пара № {id+1} {i}")
    else:
        print('Сьогодні завданнь немає, сьогодні - вихідний')

# Виводить розклад на завтрашній день
def schedule_tomorrow():
    if schedule[days[weekday+1]]:
        for id, i in enumerate(schedule[days[weekday + 1]]):
            print(f"Пара № {id + 1} {i}")
    else:
        print('Завдань на завтра немає, завтра - вихідний')

# Ім’я файлу для збереження завдань
filename = 'values.json'

# Зберігає список завдань у файл
def save_value(input_value):
    with open(filename, 'w') as f:
        json.dump(input_value, f, indent=2)

# Завантажує список завдань із файлу
def load_value():
    try:
        with open(filename) as f:
            return json.load(f)
    except json.decoder.JSONDecodeError and FileNotFoundError:
        return []

# Завантажує існуючі завдання при старті
tasks = load_value()

# Додає нове завдання з введенням користувача
def task_add():
    task = input('Введіть назву завдання: ')
    try:
        date_task = input('Введіть дату виконання завдання(Формат - день місяць рік(X X XXXX)): ')
        # Перевірка правильності формату дати
        datetime.datetime.strptime(date_task, "%d %m %Y")
        description = input('Додайте опис до завдання: ')
        tasks.append({'task': task, 'date_task': date_task, 'description': description})
        save_value(tasks)
        print('Завдання додано успішно')
    except ValueError:
        print('Неправильний формат дати')


# Виводить усі збережені завдання
def all_tasks():
    print('Список усіх завдань: \n')
    for i in load_value():
        print(f"Предмет: {i['task']}, Дата здачі: {i['date_task']}, Опис: {i['description']}")

# Виводить завдання, що мають бути здані сьогодні або завтра
def notification():

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    upcoming_tasks = []
    for task in load_value():
        calculeted_date = datetime.datetime.strptime(task['date_task'], "%d %m %Y").date()
        if calculeted_date == datetime.date.today() or calculeted_date == tomorrow:
            upcoming_tasks.append(task)

    if upcoming_tasks:
        print("Завдання на найближчі дні:\n")
        for task in upcoming_tasks:
            print(f"Предмет: {task['task']}, Дата здачі: {task['date_task']}, Опис: {task['description']}")

# Основний цикл
greetings()
while True:
    user_input = input('Введіть команду: ').lower()
    if user_input == 'допомога':
        help()
    elif user_input == 'розклад на сьогодні':
        schedule_today()
    elif user_input == 'розклад на завтра':
        schedule_tomorrow()
    elif user_input == 'додати завдання':
        task_add()
    elif user_input == 'завдання':
        all_tasks()
    elif user_input == 'нагадування':
        notification()
    elif user_input == 'вийти':
        print("До зустрічі! Гарного дня!")
        break
    else:
        print('Невідома команда.')

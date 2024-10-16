tasks_list = [
              ('tasks', 'time complited', 'time start', 'prio'),
              ('test', '60', '15', '1'),
              ('vito test', '150', '15', '1')
             ]
count = 'count'

def output_tasks(tasks):
    global count
    print('_' * 100)
    for each in tasks:
        space = len(each[0]) - 50
        s_1 = '| ' + count + ' ' * (abs(len(count) - 6)) + '|'
        if (len(each[0]) / 2) % 2 == 0: s_2 =  ' ' * abs(space//2 - 1) + each[0] + ' ' * abs(space//2 - 1) + '|'
        else: s_2 = ' ' * abs(space//2) + each[0] + ' ' * abs(space//2 - 1)  + '|'
        s_3 = each[1] + ' ' * (abs(len(each[1]) - 15)) + '|'
        s_4 = each[2] + ' ' * (abs(len(each[2]) - 11)) + '|'
        s_5 = each[3] + ' ' * (abs(len(each[3]) - 5)) + '|'
        print(s_1, s_2, s_3, s_4, s_5)
        if count == 'count':
            count = '0'
            print('_' * 100)
        count = str(int(count) + 1)

    print('_' * 100)


def input_tasks(tasks_list):
    global count
    if count == 'count':
        count = '0'
        count = str(int(count) + 1)
        interval = input('введите интервал выполнения задачи: ')
        cpu = input('Введите количество одновременно выполняемых задач: ')

    print('Введите входные данные')
    title_tasks = input('1 - Имя задачи: ')
    time_complited = input('2 - время на выполнение этой задачи: ')
    time_start = input('3 - время начала выполнения этой задачи: ')

    prio = input('4 - Приоритет (1-5): ')
    tasks_list.append((title_tasks, time_complited, time_start, prio))
    action = input('Хотите еще ввести задачу?\n1 - ввести еще задачу\n0 - выйти в главное меню ')
    if action == '1': input_tasks(tasks_list)
    else: print(' ' * 100)


input_tasks(tasks_list)
print(tasks_list)
output_tasks(tasks_list)
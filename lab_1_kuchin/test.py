import heapq

# Класс для представления задачи
class Task:
    def __init__(self, name, activation_time, execution_time, priority):
        self.name = name  # Имя задачи
        self.activation_time = activation_time  # Момент активации задачи
        self.execution_time = execution_time  # Время выполнения задачи
        self.priority = priority  # Абсолютный приоритет задачи
        self.remaining_time = execution_time  # Оставшееся время для выполнения

    def __lt__(self, other):
        # Сравниваем задачи по приоритету (больший приоритет - выше)
        if self.priority == other.priority:
            return self.activation_time < other.activation_time  # Если приоритеты равны, выбираем по времени активации
        return self.priority < other.priority  # Меньший приоритет означает больший приоритет

    def __str__(self):
        return f"{self.name}"

# Диспетчер задач
class Scheduler:
    def __init__(self, interval):
        self.time = 0  # Время симуляции (такт)
        self.ready_queue = []  # Очередь готовых задач
        self.tasks = []  # Список всех задач
        self.interval = interval  # Длительность интервала (время работы задачи)

    def add_task(self, name, activation_time, execution_time, priority):
        # Добавляем задачу в список задач
        task = Task(name, activation_time, execution_time, priority)
        self.tasks.append(task)

    def run(self):
        # Сортируем задачи по времени активации
        self.tasks.sort(key=lambda t: t.activation_time)
        task_index = 0  # Индекс текущей задачи в списке задач

        current_task = None  # Текущая задача, которая выполняется
        remaining_time_in_interval = 0  # Оставшееся время в текущем интервале
        state_changes = []  # Список для хранения изменений состояния

        # Форматируем заголовки таблицы
        print(f"{'Такт':<5}{'Загрузка процессора':<25}{'Очередь готовности':<30}")
        print("-" * 60)

        # Запускаем диспетчер задач
        while task_index < len(self.tasks) or self.ready_queue or current_task:
            # Добавляем все задачи, которые активировались на данный момент времени
            while task_index < len(self.tasks) and self.tasks[task_index].activation_time <= self.time:
                heapq.heappush(self.ready_queue, self.tasks[task_index])
                task_index += 1

            # Если нет задачи на текущий момент или приоритет в очереди выше текущей
            if current_task is None and self.ready_queue:
                current_task = heapq.heappop(self.ready_queue)
            elif current_task and self.ready_queue:
                # Если есть задача с более высоким приоритетом в очереди, прерываем выполнение текущей
                if self.ready_queue[0].priority < current_task.priority:
                    state_changes.append((self.time, f"Прерывание: {current_task.name} прервана"))
                    heapq.heappush(self.ready_queue, current_task)
                    current_task = heapq.heappop(self.ready_queue)
                    state_changes.append((self.time, f"Начинаем выполнение задачи {current_task.name}"))

            # Выводим информацию о текущем такте
            cpu_load = current_task.name if current_task else "Пусто"
            ready_queue = " ".join([task.name for task in self.ready_queue])

            # Сохранение состояний для вывода
            state_changes.append((self.time, f"Загрузка процессора: {cpu_load} | Очередь готовности: {ready_queue}"))

            # Выполняем задачу в течение одного интервала
            if current_task:
                execution_time_in_current_interval = min(self.interval, current_task.remaining_time)

                # Уменьшаем оставшееся время задачи
                current_task.remaining_time -= execution_time_in_current_interval
                remaining_time_in_interval = execution_time_in_current_interval

                # Если задача завершена, освобождаем текущую задачу
                if current_task.remaining_time == 0:
                    state_changes.append((self.time, f"Задача {current_task.name} завершена"))
                    current_task = None

            # Обновляем время на величину интервала
            self.time += 1  # Каждый такт увеличиваем на 1
            remaining_time_in_interval = 0

        # Вывод всех изменений состояний в таблице
        for change in state_changes:
            print(f"{change[0]:<5}{change[1]:<50}")
        print("Все задачи выполнены.")

# Функция для ввода данных о задачах вручную
def input_tasks():
    tasks = []
    num_tasks = int(input("Введите количество задач: "))  # Количество задач

    for _ in range(num_tasks):
        name = input("Введите имя задачи: ")  # Имя задачи
        activation_time = int(input(f"Введите момент активации задачи {name}: "))  # Время активации задачи
        execution_time = int(input(f"Введите время выполнения задачи {name}: "))  # Время выполнения задачи
        priority = int(input(f"Введите приоритет задачи {name}: "))  # Приоритет задачи

        tasks.append((name, activation_time, execution_time, priority))

    return tasks

# Пример использования
if __name__ == "__main__":
    # Вводим интервал
    interval = int(input("Введите длительность интервала (время одного такта): "))

    scheduler = Scheduler(interval)

    # Вводим задачи вручную
    tasks = input_tasks()

    # Добавляем задачи в диспетчер
    for task in tasks:
        scheduler.add_task(*task)

    # Запускаем диспетчер
    scheduler.run()

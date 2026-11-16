
import queue
import threading
import time


# Класс заказа
class Order:

    def __init__(self, order_id, customer, products, total_price, priority):
        self.id = order_id
        self.customer = customer
        self.products = products
        self.total_price = total_price
        self.status = "Ожидает обработки"
        self.priority = priority

    def show_info(self):
        print(f"\nНомер заказа: {self.id}")
        print(f"Клиент: {self.customer}")
        print(f"Товары: {', '.join(self.products)}")
        print(f"Сумма: {self.total_price}")
        print(f"Приоритет: {self.priority}")
        print(f"Статус: {self.status}")


# Класс обработки заказов
class OrderProcessor:

    def __init__(self):
        self.orders = []
        self.order_queue = queue.Queue()

        self.order_id = 1

        self.processed_count = 0

        # Защита общего счетчика
        self.lock = threading.Lock()

        # Количество рабочих потоков
        self.workers_count = 3

    # Добавление заказа
    def add_order(self):

        customer = input("Введите имя клиента: ").strip()

        if customer == "":
            print("Ошибка! Имя клиента не может быть пустым.")
            return

        products_input = input("Введите товары через запятую: ")

        products = []

        for product in products_input.split(","):
            if product.strip():
                products.append(product.strip())

        if len(products) == 0:
            print("Ошибка! Нужно добавить хотя бы один товар.")
            return

        try:
            total_price = float(input("Введите общую сумму заказа: "))

            if total_price < 0:
                print("Ошибка! Сумма не может быть отрицательной.")
                return

        except ValueError:
            print("Ошибка! Нужно ввести число.")
            return

        print("\nВыберите приоритет заказа:")
        print("1. Обычный")
        print("2. Срочный")
        print("3. Критический")

        priority_choice = input("Ваш выбор: ")

        priorities = {
            "1": "Обычный",
            "2": "Срочный",
            "3": "Критический"
        }

        if priority_choice not in priorities:
            print("Ошибка! Неправильный приоритет.")
            return

        priority = priorities[priority_choice]

        order = Order(
            self.order_id,
            customer,
            products,
            total_price,
            priority
        )

        self.orders.append(order)

        print(f"\nЗаказ №{self.order_id} успешно добавлен!")

        self.order_id += 1

    # Обработка одного заказа
    def process_order(self, order):

        order.status = "Обрабатывается"

        print(
            f"\nПоток {threading.current_thread().name}: "
            f"начал обработку заказа №{order.id}"
        )

        # Имитация обработки заказа
        time.sleep(2)

        order.status = "Обработан"

        print(
            f"Поток {threading.current_thread().name}: "
            f"завершил обработку заказа №{order.id}"
        )

        # Увеличиваем счетчик обработанных заказов
        with self.lock:
            self.processed_count += 1

    # Функция рабочего потока
    def worker(self):

        while True:

            order = self.order_queue.get()

            try:
                # None означает завершение работы потока
                if order is None:
                    return

                self.process_order(order)

            finally:
                self.order_queue.task_done()

    # Запуск обработки заказов
    def start_processing(self):

        # Получаем только необработанные заказы
        pending_orders = []

        for order in self.orders:
            if order.status == "Ожидает обработки":
                pending_orders.append(order)

        if len(pending_orders) == 0:
            print("\nНет заказов для обработки.")
            return

        # Сортировка по приоритету
        priorities = {
            "Обычный": 1,
            "Срочный": 2,
            "Критический": 3
        }

        pending_orders.sort(
            key=lambda order: priorities[order.priority],
            reverse=True
        )

        # Добавляем заказы в очередь
        for order in pending_orders:
            self.order_queue.put(order)

        print("\nЗапуск рабочих потоков...")

        threads = []

        # Создаем три рабочих потока
        for i in range(self.workers_count):

            thread = threading.Thread(
                target=self.worker,
                name=f"Worker-{i + 1}"
            )

            threads.append(thread)
            thread.start()

        # Отправляем каждому потоку сигнал завершения
        for i in range(self.workers_count):
            self.order_queue.put(None)

        # Ожидаем завершения всех задач
        self.order_queue.join()

        # Ожидаем завершения потоков
        for thread in threads:
            thread.join()

        print("\nОбработка всех заказов завершена!")

    # Показать все заказы
    def show_orders(self):

        if len(self.orders) == 0:
            print("\nСписок заказов пуст.")
            return

        print("\n===== ВСЕ ЗАКАЗЫ =====")

        for order in self.orders:
            order.show_info()

    # Показать статистику
    def show_statistics(self):

        total_orders = len(self.orders)

        with self.lock:
            successful_orders = self.processed_count

        unprocessed_orders = total_orders - successful_orders

        print("\n===== СТАТИСТИКА =====")
        print(f"Всего получено заказов: {total_orders}")
        print(f"Успешно обработано: {successful_orders}")
        print(f"Не обработано: {unprocessed_orders}")

    # Главное меню
    def menu(self):

        while True:

            print("\n===== ORDER PROCESSOR =====")
            print("1. Добавить заказ")
            print("2. Показать все заказы")
            print("3. Запустить обработку")
            print("4. Показать статистику")
            print("0. Выход")

            choice = input("\nВыберите пункт меню: ")

            if choice == "1":
                self.add_order()

            elif choice == "2":
                self.show_orders()

            elif choice == "3":
                self.start_processing()

            elif choice == "4":
                self.show_statistics()

            elif choice == "0":
                print("\nЗавершение программы.")
                self.show_statistics()
                break

            else:
                print("Ошибка! Выберите пункт от 0 до 4.")


# Запуск программы
if __name__ == "__main__":

    processor = OrderProcessor()

    processor.menu()

print("hello")
#1)
# def display_quote():
#     print(('"Don\' t compare yourself with anyone in this world...if you do so, you are insulting yourself."'))
#     print("Bill Gates")
# display_quote()
#2)
# def display_even_numbers(start, end):
#     if start > end:
#         start, end = end, start
#     for number in range(start, end):
#         if number % 2 == 0:
#             print(number)
# display_even_numbers(1, 20)
#3)
# def display_square(side_lenght, char, is_filled):
#     if is_filled:
#         for _ in range(side_lenght):
#             print(char * side_lenght)
#     else:
#         for i in range(side_lenght):
#             if i == 0 or i == side_lenght - 1:
#                 print(char * side_lenght)
#             else:
#                 print(char + ' ' * (side_lenght - 2) + char)
# print("Заполненный квадрат: ")
# display_square(3, '*', True)
# print("\nПустой квадрат: ")
# display_square(3, '*', False)
# import random
# #1)
# class Number:
#     def init(self, size):
#         self.numbers = [random.randint(-100, 100) for _ in range(size)]
#     def process_list(self):
#         print(f"Исходный список: {self.numbers}")
#         n = len(self.numbers)
#         n1 = n // 3
#         n2 = 2 * n // 3
#         average = sum(self.numbers) / n
#         print(f"Среднее арифметическое: {average:.2f}")
#         if average > 0:
#             self.numbers[:n2] = sorted(self.numbers[:n2])
#         else:
#             self.numbers[:n1] = sorted(self.numbers[:n1])
#         remaining_part = self.numbers[n2:]
#         remaining_part.reverse()
#         self.numbers[n2:] = remaining_part
#         print(f"Обработанный список: {self.numbers}")
# num_list = Number(15)
# num_list.process_list()
# print("\n")
#2)
# def student_performance_program():
#     grades = [random.randint(1, 12) for _ in range(10)]
#     while True:
#         print("\n--- Программа «Успеваемость» ---")
#         print("Меню:")
#         print("1. Вывод оценок")
#         print("2. Пересдача экзамена")
#         print("3. Выходит ли стипендия")
#         print("4. Вывод отсортированного списка оценок")
#         print("5. Выход")
#         choice = input("Выберите пункт меню: ")
#         if choice == '1':
#             print(f"Текущие оценки: {grades}")
#         elif choice == '2':
#             try:
#                 index = int(input("Введите номер элемента (от 1 до 10) для пересдачи: ")) - 1
#                 if 0 <= index < 10:
#                     new_grade = int(input("Введите новую оценку (от 1 до 12): "))
#                     if 1 <= new_grade <= 12:
#                         grades[index] = new_grade
#                         print("Оценка обновлена.")
#                     else:
#                         print("Неверная оценка. Оценка должна быть от 1 до 12.")
#                 else:
#                     print("Неверный номер элемента.")
#             except ValueError:
#                 print("Неверный ввод. Пожалуйста, введите число.")
#         elif choice == '3':
#             average_grade = sum(grades) / len(grades)
#             if average_grade >= 10.7:
#                 print(f"Средний балл: {average_grade:.2f}. Стипендия выходит!")
#             else:
#                 print(f"Средний балл: {average_grade:.2f}. Стипендия не выходит.")
#         elif choice == '4':
#             sort_choice = input("Выберите порядок сортировки: (в)озрастание или (у)бывание: ")
#             if sort_choice.lower() == 'в':
#                 print(f"Отсортированные оценки (возрастание): {sorted(grades)}")
#             elif sort_choice.lower() == 'у':
#                 print(f"Отсортированные оценки (убывание): {sorted(grades, reverse=True)}")
#             else:
#                 print("Неверный выбор порядка сортировки.")
#         elif choice == '5':
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")
# student_performance_program()
# print("\n")
#3)
# def advanced_bubble_sort(arr):
#     n = len(arr)
#     print(f"Исходный список для сортировки: {arr}")
#     for i in range(n - 1):
#         swaps_count = 0
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# swaps_count = ()
# swaps_count += 1
# print(f"Пройден шаг {i + 1}, количество перестановок: {swaps_count}")
# if swaps_count == 0:
#     print("Количество перестановок равно нулю, список отсортирован досрочно.")
# break
# return arr
# print("--- Задание 3 Пример ---")
# list_to_sort_1 = [64, 34, 25, 12, 22, 11, 90]
# advanced_bubble_sort(list_to_sort_1)
# print(f"Отсортированный список 1: {list_to_sort_1}")
# print("-" * 20)
# list_to_sort_2 = [1, 2, 3, 4, 5, 0]
# advanced_bubble_sort(list_to_sort_2)
# print(f"Отсортированный список 2: {list_to_sort_2}")



#1)
# import random
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
# def task1():
#     print("# Задание 1")
#     list1 = [random.randint(1, 20) for _ in range(5)]
#     list2 = [random.randint(1, 20) for _ in range(5)]
#     list3 = [random.randint(1, 20) for _ in range(5)]
#     list4 = [random.randint(1, 20) for _ in range(5)]
#     combined_list = list1 + list2 + list3 + list4
#     print(f"Исходный объединенный список: {combined_list}")
#     sort_choice = input("Выберите тип сортировки (asc - по возрастанию, desc - по убыванию): ")
#     if sort_choice.lower() == 'desc':
#         combined_list.sort(reverse=True)
#         print(f"Список после сортировки по убыванию: {combined_list}")
#     else:
#         combined_list.sort()
#         print(f"Список после сортировки по возрастанию: {combined_list}")
#     try:
#         search_value = int(input("Введите целое число для поиска: "))
#         index = linear_search(combined_list, search_value)
#         if index != -1:
#             print(f"Ответ: Элемент {search_value} найден по индексу {index}.")
#         else:
#             print(f"Ответ: Элемент {search_value} не найден в списке.")
#     except ValueError:
#         print("Ошибка ввода. Пожалуйста, введите целое число.")
#2)
# def binary_search(arr, target):
#     high = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# def task2():
#     print("# Задание 2")
#     list1 = [random.randint(1, 15) for _ in range(5)]
#     list2 = [random.randint(1, 15) for _ in range(5)]
#     list3 = [random.randint(1, 15) for _ in range(5)]
#     list4 = [random.randint(1, 15) for _ in range(5)]
#     print(f"Список 1: {list1}\nСписок 2: {list2}\nСписок 3: {list3}\nСписок 4: {list4}")
#     all_elements = list1 + list2 + list3 + list4
#     unique_to_each = []
#     for elem in all_elements:
#         count = list1.count(elem) + list2.count(elem) + list3.count(elem) + list4.count(elem)
#         if count == 1 and elem not in unique_to_each:
#             unique_to_each.append(elem)
#     print(f"Список уникальных элементов (встречающихся только в одном из списков): {unique_to_each}")
#     sort_choice = input("Выберите тип сортировки (asc - по возрастанию, desc - по убыванию): ")
#     if sort_choice.lower() == 'desc':
#         unique_to_each.sort(reverse=True)
#         print(f"Список после сортировки по убыванию: {unique_to_each}")
#     else:
#         unique_to_each.sort()
#         print(f"Список после сортировки по возрастанию: {unique_to_each}")
#     try:
#         search_value = int(input("Введите целое число для поиска бинарным поиском: ")):
# index = binary_search(unique_to_each, search_value)
#         if index != -1:
#             print(f"Ответ: Элемент {search_value} найден по индексу {index}.")
#         else:
#             print(f"Ответ: Элемент {search_value} не найден в списке.")
#     except ValueError:
#         print("Ошибка ввода. Пожалуйста, введите целое число.")
# task1()
# task2()
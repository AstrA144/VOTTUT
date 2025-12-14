
# def linear_search(arr, target):
#     for i, item in enumerate(arr):
#         if item == target:
#             return i
#     return -1
# list1 = [11, 22, 33]
# list2 = [44, 55, 66]
# list3 = [77, 88, 99]
# list4 = [100, 111, 122]
# combined_list = list1 + list2 + list3 + list4
# print(f"Объединенный список: {combined_list}")
# sort_choice = input("Выберите тип сортировки (asc/desc): ")
# if sort_choice.lower() == 'desc':
#     combined_list.sort(reverse=True)
#     print(f"Список отсортирован по убыванию: {combined_list}")
# else:
#     combined_list.sort()
#     print(f"Список отсортирован по возрастанию: {combined_list}")
# try:
#     user_value = int(input("Введите значение для поиска: "))
#     index = linear_search(combined_list, user_value)
#     if index != -1:
#         print(f"Значение {user_value} найдено в списке на позиции {index}.")
#     else:
#         print(f"Значение {user_value} не найдено в списке.")
# except ValueError:
#     print("Некорректный ввод. Пожалуйста, введите целое")
#2)
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# list1 = [11, 22, 33, 10]
# list2 = [44, 55, 66, 20]
# list3 = [77, 88, 99, 30]
# list4 = [100, 111, 122, 40]
# # Объединение уникальных элементов с использованием множеств
# unique_elements = set(list1 + list2 + list3 + list4)
# combined_list = list(unique_elements)
# print(f"Объединенный список уникальных элементов: {combined_list}")
# sort_choice = input("Выберите тип сортировки (asc/desc): ")
# if sort_choice.lower() == 'desc':
#     combined_list.sort(reverse=True)
#     print(f"Список отсортирован по убыванию: {combined_list}")
# else:
#     combined_list.sort()
#     print(f"Список отсортирован по возрастанию: {combined_list}")
# try:
#     user_value = int(input("Введите значение для поиска: "))
#     index = binary_search(combined_list, user_value)
#     if index != -1:
#         print(f"Значение {user_value} найдено в списке на позиции {index}.")
#     else:
#         print(f"Значение {user_value} не найдено в списке.")
# except ValueError:
#     print("Некорректный ввод. Пожалуйста, введите целое")

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

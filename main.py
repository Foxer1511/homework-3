# # У всіх завданнях використовувати обробку винятків
# #
# # 1 завдання. Користувач вводить із клавіатури номер дня тижня (1-7).
# # Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис
# # понеділок, 2 — вівторок тощо.
#
# try:
#     day = int(input("Введіть день неділі від 1 до 7 де 1 - понеділок, 2 - вівторок і тд. "))
#
#     match day:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")
#         case 7:
#             print("Sunday")
#         case _:
#             print("Error!! Please enter 1-7.")
# except ValueError as error:
#     print(f"Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:
#     print(f"Exeption occured: {error}")

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
#
#
# 2 завдання. Користувач вводить два числа. Визначити, чи рівні ці числа,
# і, якщо ні, вивести їх на екран у порядку зростання
#
# try:
#     num1 = int(input("Введіть перше число: "))
#     num2 = int(input("Введіть друге число: "))
#
#     if num1 == num2:
#         print("same")
#     else:
#         if num1 > num2:
#             print(num2, num1)
#         else:
#             print(num1, num2)
# except ValueError as error:
#     print(f"Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:
#     print(f"Exeption occured: {error}")
#
#3. Користувач вводить два числа та матем дію: + - * або /
#Залежно від введеної матем дії вивести результат
#
#
# try:
#     num1 = int(input("enter 1 number = "))
#     num2 = int(input("enter 2 number = "))
#     math_action = input("Enter math action: + - * / ")
#
#     match math_action:
#         case "+":
#             print(f"{num1} {math_action} {num2} = {num1 + num2}")
#         case "-":
#             print(f"{num1} {math_action} {num2} = {num1 - num2}")
#         case "*":
#             print(f"{num1} {math_action} {num2} = {num1 * num2}")
#         case "/":
#             if num2 != 0:
#                 print(f"{num1} {math_action} {num2} = {num1 / num2}")
#             else:
#                 print("Division by zero!!")
#         case _:
#             print("Error!!")
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occcurred: {error}")
# except ValueError as error:
#     print(f"Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:
#     print(f"Exeption occurred: {error}")


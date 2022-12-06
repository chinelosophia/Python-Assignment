total = 0
num_positive_integers = 0
num_negative_integers = 0
sum_positive_integers = 0
sum_negative_integers = 0
number_counter = 0
average = 0
user_input = float(input("Enter number or Exit with 0: "))
while user_input != 0:

    if user_input > 0:
        sum_positive_integers = sum_positive_integers + user_input
        num_positive_integers += 1

    if user_input < 0:
        sum_negative_integers = sum_negative_integers + user_input
        num_negative_integers += 1
    user_input = int(input("Enter a number or exit with 0: "))
    number_counter += 1
    total = sum_negative_integers + sum_positive_integers
    average = float(total / number_counter)


print(
    f" the number of positive number is: {num_positive_integers} The number of negative number is: {num_negative_integers} "
    f" the total is:  {total} the average is: {average} ")

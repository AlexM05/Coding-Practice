import random

target_number = random.randrange(1000, 10000)
attempt_count = 0

while True:
    try:
        user_guess = int(input("Guess the 4-digit number: "))
        if len(str(user_guess)) == 4:
            break
        else:
            print("Invalid input")
    except ValueError:
        print("That is out of range")

if user_guess == target_number:
    print("Congratulations! You guessed the number in 1 attempt!")
else:
    if attempt_count == 3:
        print("Game over")
        quit()

    while user_guess != target_number:
        attempt_count += 1
        correct_digit_count = 0
        misplaced_digit_count = 0
        user_guess_str = str(user_guess)
        target_number_str = str(target_number)

        correct_digits = ["X"] * 4

        for i in range(0, 4):
            if (target_number_str.count(user_guess_str[i])) > 0 and (user_guess_str[i] != target_number_str[i]):
                misplaced_digit_count += 1
            elif misplaced_digit_count >= 2:
                misplaced_digit_count = 1

        for i in range(0, 4):
            if user_guess_str[i] == target_number_str[i]:
                correct_digit_count += 1
                correct_digits[i] = user_guess_str[i]
            else:
                continue

        if (correct_digit_count < 4) and (correct_digit_count != 0):
            print("Incorrect. You guessed", correct_digit_count, "correct digit(s).")
            print("You have", misplaced_digit_count, "digit(s) that are correct but in the wrong position.")
            print("These numbers in your input were correct:")
            print(*correct_digits, sep=' ')

            while True:
                try:
                    user_guess = int(input("Guess the 4-digit number: "))
                    if len(str(user_guess)) == 4:
                        break
                    else:
                        print("Invalid input")
                except ValueError:
                    print("That is out of range")

        elif (misplaced_digit_count != 0) and (correct_digit_count == 0):
            print("You guessed", misplaced_digit_count, "digit(s) correctly but in the wrong position.")
            user_guess = int(input("Enter your next guess: "))

        elif (correct_digit_count == 0) and (misplaced_digit_count == 0):
            print("None of the digits in your guess match.")
            user_guess = int(input("Enter your next guess: "))

        if attempt_count == 11:
            print("Game over! You have reached the maximum number of attempts which was set at ", attempt_count + 1)
            quit()

    if user_guess == target_number:
        print("Congratulations! You won!")
        attempt_count += 1
        print("It took you", attempt_count, "attempts.")

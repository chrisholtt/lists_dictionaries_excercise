# For the following list of numbers:
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for num in numbers:
    if num % 2 == 0:
        print(num)


# 2. Print the difference between the largest and smallest value:
difference = max(numbers) - min(numbers)
print(difference)


# 3. Print True if the list contains a 2 next to a 2 somewhere.
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
previous_number = None
index = -1
indexes_containing_a_2 = []

for number in numbers:
    index += 1
    if previous_number == number:
        print(True)
        indexes_containing_a_2.append(index)
    elif number == 2:
        indexes_containing_a_2.append(index)
        previous_number = number
    else:
        previous_number = number

print(indexes_containing_a_2)


# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
unwanted_numbers = []
sum = 0
skipping = False

for number in numbers:
    if not skipping and number != 6:
        sum += number
    elif number == 6:
        skipping = True
        unwanted_numbers.append(number)
    elif number == 7:
        skipping = False
    elif skipping:
        unwanted_numbers.append(number)


print(f"the sum is {sum} and the numbers skipped were: {unwanted_numbers}")

# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
unwanted_numbers = []
accumulator = 0
current_index = -1
index_to_skip = None

for number in numbers:
    current_index += 1

    if number != 13 and current_index != index_to_skip:
        accumulator += number
        print(
            f"current index: {current_index}: value: {number} running total: {accumulator}")

    elif number == 13:
        index_to_skip = current_index + 1
        unwanted_numbers.append(number)
        print(
            f"current index: {current_index}: value: {number} running total: {accumulator}")

    elif current_index == index_to_skip:
        unwanted_numbers.append(number)
        print(
            f"current index: {current_index}: value: {number} running total: {accumulator}")

print(f"numbers skipped: {unwanted_numbers}")

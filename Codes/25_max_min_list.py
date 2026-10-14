def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return (maximum, minimum)
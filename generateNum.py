import random

# Generate a list of 1000 random numbers between 0 and 1000
randomNumber500 = [random.randint(0, 1000) for i in range(500)]
sortedNumber500 = randomNumber500.copy()
sortedNumber500.sort()
reversedNumber500 = randomNumber500.copy()
reversedNumber500.sort(reverse=True)

# Generate a list of 5000 random numbers between 0 and 10000
randomNumber5000 = [random.randint(0, 10000) for i in range(5000)]
sortedNumber5000 = randomNumber5000.copy()
sortedNumber5000.sort()
reversedNumber5000 = randomNumber5000.copy()
reversedNumber5000.sort(reverse=True)


# Generate a list of 50000 random numbers between 0 and 100000
randomNumber50000 = [random.randint(0, 100000) for i in range(50000)]
sortedNumber50000 = randomNumber50000.copy()
sortedNumber50000.sort()
reversedNumber50000 = randomNumber50000.copy()
reversedNumber50000.sort(reverse=True)

# Small

with open("small_random.txt", "w") as file:
    for number in randomNumber500:
        file.write(str(number) + "\n")

with open("small_sorted.txt", "w") as file:
    for number in sortedNumber500:
        file.write(str(number) + "\n")

with open("small_reversed.txt", "w") as file:
    for number in reversedNumber500:
        file.write(str(number) + "\n")

# Medium

with open("medium_random.txt", "w") as file:
    for number in randomNumber5000:
        file.write(str(number) + "\n")

with open("medium_sorted.txt", "w") as file:
    for number in sortedNumber5000:
        file.write(str(number) + "\n")

with open("medium_reversed.txt", "w") as file:
    for number in reversedNumber5000:
        file.write(str(number) + "\n") 

# Large

with open("large_random.txt", "w") as file:
    for number in randomNumber50000:
        file.write(str(number) + "\n")

with open("large_sorted.txt", "w") as file:
    for number in sortedNumber50000:
        file.write(str(number) + "\n")

with open("large_reversed.txt", "w") as file:
    for number in reversedNumber50000:
        file.write(str(number) + "\n") 


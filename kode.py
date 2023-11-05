import time
import math
import tracemalloc

# =========================================================================================================================================

# BIDIRECTIONAL CONDITIONAL INSERTION SORT

def bcis(array):
    SL = 0
    SR = len(array) - 1

    while SL < SR:
        right = SR
        left = SL
        
        SWAP(array, SR, SL + math.ceil((SR-SL)/2))

        if array[SL] == array[SR]:
            if ISEQUAL(array, SL, SR) == -1:
                return

        if array[SL] > array[SR]:
            SWAP(array, SL, SR)

        if (SR - SL) >= 100:
            i = SL + 1
            for i in range(i, math.ceil(math.sqrt(SR-SL))):
                if array[SR] < array[i]:
                    SWAP(array, SR, i)
                elif array[SL] > array[i]:
                    SWAP(array, SL, i)
        else:
            i = SL + 1

        LC = array[SL]
        RC = array[SR]

        while i < SR:
            CurrItem = array[i]

            if CurrItem >= RC:
                array[i] = array[SR - 1]
                INS_RIGHT(array, CurrItem, SR, right)
                SR -= 1
            elif CurrItem <= LC:
                array[i] = array[SL + 1]
                INS_LEFT(array, CurrItem, SL, left)
                SL += 1
                i += 1
            else:
                i += 1

        SL += 1
        SR -= 1


def ISEQUAL(array, SL, SR):
    for k in range(SL + 1, SR, 1):
        if array[k] != array[SL]:
            SWAP(array, k, SL)
            return k
    return -1


def INS_RIGHT(array, CurrItem, SR, right):
    j = SR
    while j <= right and CurrItem > array[j]:
        array[j - 1] = array[j]
        j += 1
    array[j - 1] = CurrItem


def INS_LEFT(array, CurrItem, SL, left):
    j = SL
    while j >= left and CurrItem < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = CurrItem

def SWAP(array, i, j):
    array[i], array[j] = array[j], array[i]


# =========================================================================================================================================

# COUNTING SORT
# Taken from https://www.geeksforgeeks.org/counting-sort/

def count_sort(input_array):
    # Finding the maximum element of input_array.
    M = max(input_array)
 
    # Initializing count_array with 0
    count_array = [0] * (M + 1)
 
    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1
 
    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    # Creating output_array from count_array
    output_array = [0] * len(input_array)
 
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
 
    return output_array


# =========================================================================================================================================


def hitungKompleksitas(file_name, algoritma):
    tracemalloc.start()
    with open(file_name) as file:
        file = file.readlines()
    array = [int(line.strip()) for line in file]

    if algoritma == "BCIS":
        start_time = time.perf_counter()
        bcis(array)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
    elif algoritma == "CS":
        start_time = time.perf_counter()
        output_array = count_sort(array)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
    
    print(f"Execution time for {file_name} with {algoritma} algorithm is {execution_time} ms")

    print("Traced Memory (Current, Peak): ", tracemalloc.get_traced_memory())
    tracemalloc.reset_peak()
    tracemalloc.stop()
    print()


files = ["small_sorted.txt", "small_random.txt", "small_reversed.txt", "medium_sorted.txt", "medium_random.txt", "medium_reversed.txt", 
         "large_sorted.txt", "large_random.txt", "large_reversed.txt"]

for file in files:
    hitungKompleksitas(file, "BCIS")
    hitungKompleksitas(file, "CS")
    print()
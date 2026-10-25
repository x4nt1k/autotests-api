

def binary_search(array_num: list, item: int) -> None:
    low = 0
    high = len(array_num) -1

    while low <= high:
        mid = (low + high) // 2
        guess = array_num[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

a = [1, 3, 6, 8, 9, 12, 15, 17]
i = 12
print(binary_search(a, i))
print(a[binary_search(a, i)])
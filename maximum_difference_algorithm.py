<<<<<<< HEAD
#justification in pdf file
def max_difference(arr):
    if len(arr) < 2:
        return 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    max_left = max_difference(left_half)
    max_right = max_difference(right_half)

    min_val = min(arr)
    max_val = max(arr)

    max_diff = max(max_left, max_right, max_val - min_val)

    return max_diff


def main():
    A = [4, 5, 10, -2, 3.14159, -7.115]
    result = max_difference(A)
=======
#justification in pdf file
def max_difference(arr):
    if len(arr) < 2:
        return 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    max_left = max_difference(left_half)
    max_right = max_difference(right_half)

    min_val = min(arr)
    max_val = max(arr)

    max_diff = max(max_left, max_right, max_val - min_val)

    return max_diff


def main():
    A = [4, 5, 10, -2, 3.14159, -7.115]
    result = max_difference(A)
>>>>>>> 9681e1f43439df2f2b411d2e26963757fec5caae
    print(result)
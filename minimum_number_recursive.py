def find_minimum(arr, steps=0):
    steps += 1
    if len(arr) == 1:
        return arr[0], steps
    else:
        mid = len(arr) // 2
        left_min, left_steps = find_minimum(arr[:mid], steps)
        right_min, right_steps = find_minimum(arr[mid:], steps)
        steps = left_steps + right_steps
        if left_min < right_min:
            return left_min, steps
        else:
            return right_min, steps


# Example usage
array = [5, 3, 9, 1, 4, 6]
minimum = find_minimum(array)
print("Minimum number:", minimum[0])
print("Steps:", minimum[1])

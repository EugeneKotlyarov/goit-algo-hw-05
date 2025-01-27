def binary_search_with_bounds(arr, x):
    left, right = 0, len(arr) - 1
    steps = 0
    up_bound = None

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if arr[mid] == x:
            return steps, arr[mid]

        if arr[mid] < x:
            left = mid + 1

        else:
            up_bound = arr[mid]
            right = mid - 1

    return steps, up_bound


def main():
    arr = [2.5, 3.5, 4.5, 10.5, 40.5]
    res = binary_search_with_bounds(arr, 7.5)
    print(f"Кроків: {res[0]}\nВерхня межа: {res[1]}")


if __name__ == "__main__":
    main()

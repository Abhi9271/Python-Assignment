def merge(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while(i < len_a and j < len_b):
        if a[i] <= b[j]:
            arr[k] = (a[i])
            i += 1
            k += 1
        else:
            arr[k] = (b[j])
            j += 1
            k += 1

    while i < len_a:
        arr[k] = (a[i])
        i += 1
        k += 1

    while j < len_b:
        arr[k] = (b[j])
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = (len(arr))//2

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)
    return merge(left, right, arr)


if __name__ == '__main__':
    # arr = [10, 9, 7, 3, 4, 95, 37, 5]
    arr = []
    size = int(input("Enter the size of the array: "))
    print(f"Enter {size} unsorted values: ")
    for i in range(0, size):
        arr.append(int(input(f"a[{i}]: ")))

    mergeSort(arr)
    print(arr)

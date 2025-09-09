def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    arr3 = []

    # Merge while both arrays have elements
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    # Add remaining elements
    while i < n:
        arr3.append(arr1[i])
        i += 1

    while j < m:
        arr3.append(arr2[j])
        j += 1

    return arr3
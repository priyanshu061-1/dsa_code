def ispossible(arr, n, m, mid):
    studentcount = 1
    pagesum = 0

    for i in range(n):
        if arr[i] > mid:
            return False  # A single book has more pages than mid

        if pagesum + arr[i] <= mid:
            pagesum += arr[i]
        else:
            studentcount += 1
            if studentcount > m:
                return False
            pagesum = arr[i]

    return True

def book(arr, n, m):
    if m > n:
        return -1  # Not enough books for students

    s = max(arr)         # Min value of max pages = max book size
    e = sum(arr)         # Max value of max pages = total sum of pages
    ans = -1

    while s <= e:
        mid = (s + e) // 2
        if ispossible(arr, n, m, mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    return ans


arr = [12, 34, 67, 90]
n = len(arr)
m = 2
print(book(arr, n, m))  # Output: 113

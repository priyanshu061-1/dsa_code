def reverseanarray(arr):
    n=len(arr)
    s=0
    e=n-1

    while(s<=e):
        arr[s],arr[e] = arr[e],arr[s]
        s+=1
        e-=1

    return arr

arr=[1,2,3,4]
print(reverseanarray(arr))


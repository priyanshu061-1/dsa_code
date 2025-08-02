def ispossible(arr,k,mid):
    cowcount=1;
    lastpos=arr[0]

    for i in range(len(arr)):
        if arr[i]-lastpos>=mid:
            cowcount+=1
            lastpos=arr[i]

            if cowcount==k:
                return True
        
    return False

def agressive(arr,k):
    s=0
    maxi=-1
    for i in range(len(arr)):
        maxi=max(maxi,arr[i])

    e=maxi
    ans=-1
    mid=s+(e-s)//2


    while(s<=e):
        if ispossible(arr,k,mid):
            ans=mid
            s=mid+1

        mid=s+(e-s)//2

    return ans


arr=[10,20,30,40,50]
k=2
print(agressive(arr,k))
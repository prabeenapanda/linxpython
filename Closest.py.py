#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
#Return the sum of the three integers.
def findTriplets(arr):
    target=int(input("enter a number:"))
    n = len(arr)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum=arr[i] + arr[j] + arr[k]
                if (sum == target-1 or sum == target+1):
                    return str(sum)+' = ' + str(arr[i])+','+str(arr[j])+','+str(arr[k])
                else:
                    return "not available."
arr = [-1, 2, -4, 1]
print(findTriplets(arr))


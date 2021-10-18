#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

def RainWater(arr):
    n=len(arr)
    left_max=n*[0]
    right_max=n*[0]

    left_max[0]=arr[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],arr[i])
    right_max[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right_max[i]=max(right_max[i+1],arr[i])

    water=0
    for i in range(n):
        water=water+min(left_max[i],right_max[i])-arr[i]
    return water

if __name__=='__main__':
    arr=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(RainWater(arr))
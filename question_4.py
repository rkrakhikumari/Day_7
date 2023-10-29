#sum of two digits

def sum_2(arr,sum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while (left <= right):
        if(arr[left] + arr[right] > sum):
            right = right - 1
        elif(arr[left] + arr[right] < sum):
            left = left + 1
        elif(arr[left] + arr[right] == sum):
            print(f"Values of pair are {arr[left]} & {arr[right]}")

            right = right - 1
            left = left + 1

arr = [5,7,4,3,9,8,19,21]
sum = 17
sum_2(arr, sum)

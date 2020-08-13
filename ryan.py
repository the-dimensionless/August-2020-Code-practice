def rotate(arr, d):
    array_size = len(arr)
    arr[:] = arr[array_size - d:] + arr[:array_size - d]
    print(arr)


array_size = int(input())
arr = list(map(int, input().split(" ") ) )
d = int(input())
d = d % array_size
d = array_size - d

rotate(arr, d)

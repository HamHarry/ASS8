def merge(array):
    if len(array) > 1:
        mid = len(array) //2
        left = array[:mid]
        right = array[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def output(array):
    print("Sorted array is: ",array)


array = [29,10,14,37,14,20,7,16,12]
merge(array)
output(array)
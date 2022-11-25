def partition(array,low,high):
    pivot = low
    for i in range(low+1,high+1):
        if array[i] <= array[low]:
            pivot += 1
            array[i],array[pivot] = array[pivot],array[i]
    array[pivot],array[low] = array[low],array[pivot]
    return pivot

def quick(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    def sort(array,low,high):
        if low >= high:
            return
        pivot = partition(array,low,high)
        sort(array,low,pivot-1)
        sort(array,pivot+1,high)
    return sort(array,low,high)

array = [29,10,14,37,14,20,7,16,12]
quick(array)
print(array)

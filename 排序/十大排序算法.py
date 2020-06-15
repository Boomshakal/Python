# 冒泡排序
def bubblesort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 选择排序
def selectionsort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minindex:
            arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr


# 插入排序
def insertionsort(arr):
    for i in range(len(arr)):
        preindex = i - 1
        current = arr[i]
        while preindex >= 0 and arr[preindex] > current:
            arr[preindex + 1] = arr[preindex]
            preindex -= 1
        arr[preindex + 1] = current
    return arr


# 希尔排序
def shellsort(arr):
    import math
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr


# 归并排序
def mergesort(arr):
    import math
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# 快速排序
def quicksort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionindex = partition(arr, left, right)
        quicksort(arr, left, partitionindex - 1)
        quicksort(arr, partitionindex + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def buildmaxheap(arr):
    import math
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrlen and arr[left] > arr[largest]:
        largest = left
    if right < arrlen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


# 堆排序
def heapsort(arr):
    global arrlen
    arrlen = len(arr)
    buildmaxheap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrlen -= 1
        heapify(arr, 0)
    return arr


# 计数排序
def countingsort(arr):
    bucketlen = max(arr) + 1
    bucket = [0] * bucketlen
    sortedindex = 0
    arrlen = len(arr)
    for i in range(arrlen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketlen):
        while bucket[j] > 0:
            arr[sortedindex] = j
            sortedindex += 1
            bucket[j] -= 1
    return arr


# 桶排序
def bucket_sort(arr):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶的大小
    bucket_range = (max_num - min_num) / len(arr)
    # 桶数组
    count_list = [[] for i in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        count_list[int((i - min_num) // bucket_range)].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            arr.append(j)


# 基数排序
def radixsort(arr):
    i = 0  # 初始为个位排序
    n = 1  # 最小的位数置为1（包含0）
    max_num = max(arr)  # 得到带排序数组中最大数
    while max_num > 10 ** n:  # 得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}  # 用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])  # 将每个桶置空
        for x in arr:  # 对每一位进行排序
            radix = int((x / (10 ** i)) % 10)  # 得到每位的基数
            bucket[radix].append(x)  # 将对应的数组元素加入到相 #应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:  # 若桶不为空
                for y in bucket[k]:  # 将该桶中每个元素
                    arr[j] = y  # 放回到数组中
                    j += 1
        i += 1
    return arr


if __name__ == '__main__':
    a = [3, 6, 8, 4, 2, 6, 7, 3]
    a = bubblesort(a)
    a = selectionsort(a)
    a = insertionsort(a)
    a = shellsort(a)
    a = mergesort(a)
    a = quicksort(a)
    a = heapsort(a)
    a = countingsort(a)
    bubblesort(a)
    a = radixsort(a)
    print(a)

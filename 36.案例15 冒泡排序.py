# 冒泡排序

"""
冒泡排序是一种基础的排序算法，其思想是多次遍历待排序数组，每次比较相邻的两个元素，如果顺序不正确则交换它们的位置，
这样每一轮遍历都会把当前未排序部分中的最大值（或最小值）“冒泡”到数组的最后一位，直到整个数组都有序为止。
"""


def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制遍历次数, 有多少轮比较
    for i in range(n - 1):
        # 内层循环控制比较和交换操作, 每轮比较, 进行的次数
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = bubble_sort(arr)
print(sorted_arr)





























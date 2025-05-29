import MergeSort
# 呼叫另一個py檔引用同一個function用import


def merge_sort(numbers):
    if len(numbers) < 2:  # length == 0 or 1
        return numbers

    # Divide
    mid_index = len(numbers)//2  # 整除
    left_part = numbers[0:mid_index]  # 0~(mid_index-1)
    right_part = numbers[mid_index:]  # mid_index~最後一個值
    # conquer(merge)
    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)
    sorted_numbers = MergeSort.merge(sorted_left, sorted_right)

    return sorted_numbers


if __name__ == '__main__':
    result = merge_sort([1, 10, 80,  110, 19, 40, 70])
    print(result)

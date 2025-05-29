# 針對已排序好的資料成果做合併
# Merget Sort
def merge(sorted_left, sorted_right):
    # 先定義排序的邊界大小
    sorted_numbers = list()
    while len(sorted_left) > 0 and len(sorted_right) > 0:
        if sorted_left[0] < sorted_right[0]:  # 左頭 < 右頭，將左頭塞入已排序的地方
            # list.opo(index)表示移除並回傳移除值
            sorted_numbers.append(sorted_left.pop(0))
        else:
            sorted_numbers.append(sorted_right.pop(0))
        print(sorted_left, sorted_right, sorted_numbers)
    # 若左或右有少值，已排序好但仍有未排的
    if len(sorted_left) > 0:
        sorted_numbers = sorted_numbers + sorted_left
    else:
        sorted_numbers = sorted_numbers + sorted_right
    return sorted_numbers


if __name__ == '__main__':
    result = merge([1, 10, 80,  110], [19, 40, 70])
    print(result)

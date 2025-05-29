# birarySearch
# data = [10, 20, 30, 10, 50, 55, 60, 160, 70, 80, 90, 10, 100]
# target = 10


def birarySearch(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = int((start + end) / 2)  # 取整數去小數點
        if target == arr[mid]:
            return "search OK ==> in " + str(mid+1)
            break  # 找到就離開迴圈
        elif target > arr[mid]:
            start = mid + 1  # 找右邊
        else:
            end = mid - 1  # 找左邊
    return "search not fund."


# print(birarySearch(data, target))
if __name__ == '__main__':
    result = birarySearch(
        [10, 20, 30, 10, 50, 55, 60, 160, 70, 80, 90, 10, 100], 55)
    print(result)

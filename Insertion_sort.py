def insertion_sort(numbers):
    for round in range(len(numbers)-1):
        newCard = numbers[round + 1]
        old_idx = round

        while old_idx >= 0 and newCard <= numbers[old_idx]:
            # 在尚未比到end(old_id>=0)且newcard還是小於(newCard <= numbers[old_idx])時繼續
            numbers[old_idx + 1] = numbers[old_idx]  # 不是交換是直接插入排序值
            old_idx -= 1  # 往前找值
            numbers[old_idx+1] = newCard

    sorted_numbers = numbers
    return sorted_numbers


if __name__ == '__main__':
    result = insertion_sort([1, 10, 80,  110, 19, 40, 70])
    print(result)

# selectionSort
def selection_sort(numbers):
    for r in range(len(numbers)):
        min_idx = r
        for i in range(r+1, len(numbers)):
            if numbers[i] < numbers[min_idx]:
                min_idx = i
            if min_idx != r:
                numbers[r], numbers[min_idx] = numbers[min_idx], numbers[r]
        print("roung", r, numbers)


if __name__ == '__main__':
    numbers = [40, 30, 60, 50, 20]
    selection_sort(numbers)

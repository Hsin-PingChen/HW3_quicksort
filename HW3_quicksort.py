def quick_sort(array, start=None, end=None):
    # 初始化參數
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1
    
    # 終止條件 
    if start >= end:
        return
    
    # 選擇 pivot 
    pivot_index = (start + end) // 2  # 使用中間元素作為 pivot
    pivot_value = array[pivot_index]
    
    print(f"Sorting subarray {array[start:end+1]}, pivot: {pivot_value}")
    
    # 將 pivot 移到最後面以便分割
    array[pivot_index], array[end] = array[end], array[pivot_index]
    
    left = start
    right = end - 1  # 因為 pivot 現在在最右邊
    
    while left <= right:
        # 從左找第一個大於 pivot 的元素 (修正比較對象)
        while left <= right and array[left] <= pivot_value:
            left += 1
        # 從右找第一個小於 pivot 的元素 (修正比較對象)
        while left <= right and array[right] >= pivot_value:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            print(f"  Swapped {array[right]} and {array[left]}: {array[start:end+1]}")
    
    # 將 pivot 放回正確位置 
    array[left], array[end] = array[end], array[left]
    print(f"Placed pivot {pivot_value} at position {left}: {array[start:end+1]}")
    print(f"Current array state: {array}\n")
    
    # 遞迴排序左右子數組
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)

# 測試數據
data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("原始數組:", data)
print("開始快速排序...\n")

quick_sort(data)

print("\n最終排序結果:", data)
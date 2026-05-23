def partition(nums, low, high):
    pivot = nums[low]
    i, j = low, high

    while i < j:
        while i < high and nums[i] <= pivot:
            i += 1
        while j > low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_ind = partition(nums, low, high)
        quick_sort(nums, low, p_ind - 1)   # sort left side
        quick_sort(nums, p_ind + 1, high)  # sort right side


# Example usage
nums = [4, 1, 2, 3, 3, 7, 8]
quick_sort(nums, 0, len(nums) - 1)
print("Sorted:", nums)

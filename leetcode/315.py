class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        res = [0] * n

        def merge(l, mid, r):
            left = arr[l:mid+1]
            right = arr[mid+1:r+1]
            i = j = 0
            k = l
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    arr[k] = right[j]
                    j += 1
                else:
                    res[left[i][1]] += len(right) - j
                    arr[k] = left[i]
                    i += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        def mergeSort(l, r):
            if l < r:
                mid = (l + r) // 2
                mergeSort(l, mid)
                mergeSort(mid+1, r)
                merge(l, mid, r)

        mergeSort(0, n-1)
        return res

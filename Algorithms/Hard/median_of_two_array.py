# Just first thought solution.


class Solution:
    def merge_sorted_arr(self, arr1, arr2):
        arr = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
        while i < len(arr1):
            arr.append(arr1[i])
            i += 1
        while j < len(arr2):
            arr.append(arr2[j])
            j += 1
        return arr

    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:

        nums1 = self.merge_sorted_arr(nums1, nums2)
        n = len(nums1)
        return (nums1[n // 2] + nums1[(n - 1) // 2]) / 2.0


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))

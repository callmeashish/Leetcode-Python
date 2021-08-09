class RemoveDuplicates:
    def removeDuplicatesForward(self, nums: list) -> int:
        if not nums:
            return 0

        pos = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                pos += 1
                nums[pos] = nums[i]

        nums = nums[: pos + 1]
        # OR
        # for j in range(pos+1,len(nums)):
        #     nums.pop(-1)
        print(nums)

        return pos + 1

    def removeDuplicatesBackwards(self, nums: list) -> int:
        if not nums:
            return 0

        length = len(nums) - 1
        pos = length
        for i in range(length - 1, -1, -1):
            if nums[i] != nums[i + 1]:
                pos -= 1
                nums[pos] = nums[i]

        nums[: pos + 1] = nums[pos:]
        # OR
        # for j in range(0, pos):
        #     nums.pop(0)

        print(nums)

        return pos

    def removeDuplicatesSimplest(self, nums: list) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)


if __name__ == "__main__":
    num_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(RemoveDuplicates().removeDuplicatesBackwards(num_list))

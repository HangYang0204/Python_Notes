class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {} #buff_dict{int:int}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
##    def twosum2(self,nums,target):
##        if len(nums) <= 1:
##            return False
##        buff_list = []
##        for i in range(len(nums)):
##            if target - buff_list[i] == nums[i]:
##                return [i, len(buff_list) -1]
##            else:
##                buff_list.append(target - num[i])


s = Solution()
print(s.twosum([4,5,1,2,3],9))




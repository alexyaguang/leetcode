class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        li=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif count>0:
                li.append(count)
                li.append(nums[i])
                count=0
            else:
                li.append(nums[i])
        if nums[-1]==1:
            li.append(count)
        max_res=0
        if len(li)<=3:
            max_res=sum(li)
        else:
            for i in range(len(li)-2):
                res=li[i]+li[i+1]+li[i+2]
                if res> max_res:
                    max_res=res
        if max_res==len(nums):
            max_res-=1
        return max_res
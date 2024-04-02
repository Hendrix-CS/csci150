nums = []
for i in range(3):
    nums.append(i * 2)
print(nums)

for i in range(len(nums)):
    nums[i] += 1
print(nums)

for i in range(len(nums) - 1):
    nums[i] += nums[i + 1]
print(nums)
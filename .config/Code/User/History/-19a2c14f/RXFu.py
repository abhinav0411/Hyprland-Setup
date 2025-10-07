nums = [1,2,3,1]
odd_sum = 0
even_sum = 0
for i in range(0, len(nums), 2):
    odd_sum += nums[i]
    print(odd_sum)

for j in range(1, len(nums), 2):
    even_sum += nums[j]
    print(eve)

if odd_sum > even_sum:
    print(odd_sum)
else:
    print(even_sum)
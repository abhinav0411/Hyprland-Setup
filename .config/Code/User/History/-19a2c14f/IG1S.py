nums1 = [1,2,3,0,0]
nums2 = [2, 5, 6]
m = len(nums1)
n = len(nums2)
i, j = 0, 0
while i < m and j < n:
    if nums1[i] < nums2[j]:
        j += 1 
    else:
        temp = nums1[i]
        nums1[i] = nums2[j]
        nums1.append(temp)
        i += 1
        j += 1
        
while j < n:
    nums1.append(nums2[j])
    j += 1

print(nums1)
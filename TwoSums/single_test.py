from TwoSums import twosums

num = [2,4,5,6,7]
target = 13

ans = twosums(nums,target)
expected = [[3, 4]]
if ans == expected:
	print("test pass")
print("Output : ",ans)
print("Expected : ",expected)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(11, 21):
    nums.append(i)
    print(nums)
    for _ in range(5):
        nums.pop()
    print(nums)



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
for i in range(11, 21):
    nums.append(i)
    print(nums)
    for i in range(1, 6):
        nums.remove(i)
    print(nums)




nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = len(nums) // 2
for i in range(11, 21):
   nums.insert(nums, i)
print(nums)
for i in range(11,16):
        nums.remove(i)
        print(nums)
        for _ in range(5):
            nums.pop()
            print(nums)


nums = [10, 20, 30, 40]
nums.append(50)
print(nums)

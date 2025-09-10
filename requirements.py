num_list1 = [1,2,3,4,5,6]

num_list2 = [16,23,4,3,45,7]

print(num_list1, num_list2)

total_sum = 0

for num in range(0, 6):
    total_sum = total_sum + num_list1[num]

print(total_sum)

total_sum = 0
for num in range(0, 6):
    total_sum = total_sum + num_list2[num]

print(total_sum)

total_sum = 0
count_index = 0
for num in num_list1:
    total_sum = total_sum + num
    count_index = count_index + 1
if count_index > 0:
    total_avg = total_sum / count_index
else:
    total_avg = 0
print(total_avg)

total_sum = 0 
count_index = 0
for num in num_list2: 
    total_sum = total_sum + num 
    count_index = count_index + 1 
if count_index > 0: 
    total_avg = total_sum / count_index 
else: 
    total_avg = 0 

print(total_avg)

count_index = 0
minimum_number = 0
for num in num_list1:
    if count_index == 0:
        minimum_number = num
    else:
        if num < minimum_number:
            minimum_number = num
    count_index = count_index + 1
print(minimum_number)

for num in num_list2: 
    minimum_number = min(num_list2)
print(minimum_number)
    

for number in num_list1: 
    max_number = max(num_list1)
print( max_number)

for number in num_list2: 
    max_number = max(num_list2)
print(max_number)

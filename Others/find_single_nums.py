def find_single_nums(nums):
    n1xn2=0
    for num in nums:
        n1xn2^=num
    print(f'n1xn2 is {n1xn2}')

    right_most_set_bit=1
    while( (n1xn2&right_most_set_bit)==0 ):
        right_most_set_bit=right_most_set_bit<<1
    print(right_most_set_bit)
    num1,num2=0,0
    for num in nums:
        if (num&right_most_set_bit)!=0:
            num1^=num
        else:
            num2^=num
    return [num1,num2]

print('Single numbers are:' + str(find_single_nums([4,3,3,2,8,2])))
print('Single numbers are:' + str(find_single_nums([2, 1, 3, 2])))
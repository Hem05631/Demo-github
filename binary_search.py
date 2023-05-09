import random
def guess(computer_number,array,lower_number,high_number):
    # lower_number=0
    mid_number=(high_number - lower_number)//2
    if lower_number>high_number:
        return "not valid"
    if computer_number==mid_number:
        return mid_number
    elif computer_number<mid_number:
        high_number=mid_number-1
        # new_high=mid_number-1
        # return guess(computer_number,array,lower_number,new_high)
    elif computer_number>mid_number:
        lower_number=mid_number+1
        # new_low=mid_number+1
        # return guess(computer_number,array,new_low,high_number)
    return True


if __name__ == '__main__':
    array=[]
    b=100
    for i in range(b):
        array+=[i]
    computer_number = random.choice(array)
    f=guess(computer_number,array,10,100)
    # if f==True:
    print(f)
# computer_number = random.choice(array)
# find=guess(computer_number,array,0,100)
# if find:
#     print("the number is",find)






'''
5.14 LAB: Interstate highway numbers
Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. 
Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90. 

Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

'''

# receive input
hwy_num = int(input())

# determine higway direction
direction = hwy_num % 2
if direction == 0:
    hwy_direction = 'east/west'
else:
    hwy_direction = 'north/south'
    
# determine valid input
if hwy_num <= 0 or hwy_num > 999:
    print(f'{hwy_num} is not a valid interstate highway number.')

# determine if higway is primary
if hwy_num >= 1 and hwy_num <= 99:
    print(f'I-{hwy_num} is primary, going {hwy_direction}.')

# determine if highway is auxiliary and what primary it services
if hwy_num >= 100 and hwy_num <= 999:
    serviced_hwy = hwy_num % 100
    if serviced_hwy == 0:
        print(f'{hwy_num} is not a valid interstate highway number.')
    else:
        print(f'I-{hwy_num} is auxiliary, serving I-{serviced_hwy}, going {hwy_direction}.')
 



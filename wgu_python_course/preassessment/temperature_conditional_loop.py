'''
Task:
Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of the water state based on the following scale:

If the temperature is below 33° F, the water is “Frozen”.
If the water is between 33° F and 80° F (including 33), the water is “Cold”.
If the water is between 80° F and 115° F (including 80), the water is "Warm".
If the water is between 115° F and 211° (including 115) F, the water is “Hot".
If the water is greater than or equal to 212° F, the water is “Boiling”.
Additionally, output a safety comment only during the following circumstances:

If the water is exactly 212° F, the safety comment is "Caution: Hot!"
If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
The solution output should be in the format

water_state
optional_safety_comment
Sample Input/Output:
If the input is

118
then the expected output is

Hot
Alternatively, if the input is

32
then the expected output is

Frozen
Watch out for ice!
'''

#temperature >= 212, water state is "Boiling"
#temperature (115, 211], water state is "Hot"
#temperature [80, 115], water state is "Warm"
#temperature [33, 80), water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution accepts integer input representing a water temperature
#solution outputs the water state and potential safety comment based on temperature

curr_temp = int(input())
water_state = None
optional_safety_comment = None

if curr_temp >= 212:
    print('Boiling')
    if curr_temp == 212:
        print('Caution: Hot!')
elif 115 <= curr_temp <= 211:
    print('Hot')
elif 80 <= curr_temp < 115:
    print('Warm')
elif 33 <= curr_temp < 80:
    print('Cold')
elif curr_temp < 33:
    print('Frozen')
    print('Watch out for ice!')


    
    
try:
    user_temp = int(input())
    if user_temp >= 212:
        print('Boiling')
        if user_temp == 212:
            print('Caution: Hot!')
    elif 115 <= user_temp <= 211:
        print('Hot')
    elif 80 <= user_temp < 115:
        print('Warm')
    elif 33 <= user_temp < 80:
        print('Cold')
    elif user_temp < 33:
        print('Frozen')
        print('Watch out for ice!')
except ValueError:
    print('Input must be a number.')
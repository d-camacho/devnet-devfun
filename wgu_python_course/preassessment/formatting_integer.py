'''
Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.

The solution output should be in the format

111-22-3333
Sample Input/Output:
If the input is

154175430
then the expected output is

154-17-5430
'''

#hint: modulo (%) and floored division (//) may be used
#solution accepts a 9-digit integer representing an unformatted student identification number (i.e.,"5417543010")
#solution outputs formatted student identification number as a string (i.e.,"541-75-3010")

user_input = int(input())

segment_1 = str(user_input // 1000000)
tmp_segment_2 = user_input % 1000000
segment_2 = str(tmp_segment_2 // 10000)
segment_3 = str(tmp_segment_2 % 10000)
print(f'{segment_1}-{segment_2}-{segment_3}')
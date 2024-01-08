'''

Task:
Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:

Employee A: 15.62 miles
Employee B: 41.85 miles
Employee C: 32.67 miles
The solution output should be in the format

Distance: total_miles_traveled
Sample Input/Output:
If the input is

1
2
3
then the expected output is

Distance: 197.33 miles
'''

#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places
dist_a = 15.62
dist_b = 41.85
dist_c = 32.67

num_travel_a = float(input())
num_travel_b = float(input())
num_travel_c = float(input())

total_dist = (num_travel_a * dist_a) + (num_travel_b * dist_b) + (num_travel_c * dist_c)
print(f'Distance: {total_dist:.2f} miles')


dista = 15.62
distb = 41.85 
distc = 32.67

num_travela = int(input())
num_travelb = int(input())
num_travelc = int(input())

total_distance = (dista * num_travela) + (distb * num_travelb) + (distc * num_travelc)
print(f'Distance: {total_distance:.2f} miles')

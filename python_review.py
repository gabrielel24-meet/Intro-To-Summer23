import random

Temprature = []

for i in range(7):
	Temprature.append(random.randint(26,40))

days_of_the_week=["Sunday","Monday","Tuesday","Wednesdat","Thursday", "Friday","Saturday"]


good_days_count = []

for i in range(7):
	if Temprature[i] % 2 == 0:
		good_days_count.append(Temprature[i])


highest_temp = 0
for i in range(7):
	if Temprature[i] > highest_temp:
		highest_temp = Temprature[i]

highest_temp_day = days_of_the_week[Temprature.index(highest_temp)]


lowest_temp = Temprature[0]
for i in range(7):
 	if Temprature[i] < lowest_temp:
 		lowest_temp = Temprature[i]

lowest_temp_day = days_of_the_week[Temprature.index(lowest_temp)]

Sum = 0
for i in range(7):
	Sum = Sum + Temprature[i]

Avg = Sum/7

above_avg = []

for i in range(7):
	if Temprature[i] > Avg:
		above_avg.append(Temprature[i])


print("The weather report:")
print("")

for i in range(7):
	print(days_of_the_week[i] , ": " , Temprature[i])

print("*")
print("*")

print("Shelly had " , len(good_days_count) , " good days")

print("*")
print("*")

print("The hottest temprature was: " , highest_temp , " on " , highest_temp_day)
print("The lowest temprature was: " , lowest_temp , " on " , lowest_temp_day)

print("*")
print("*")

print("The average temprature was: ", Avg)
print("The days with above average tempratures were: ", end='' )

for i in range(len(above_avg)):
	print(above_avg[i]," " , end='')
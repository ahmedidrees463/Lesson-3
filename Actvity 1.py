import datetime
import calendar

city=input("Enter your city name")
temp=float (input("What is the temperature in your city"))
if temp>35:
    print("Warning It's very hot today")

if temp>25:
    print("It's a great day to go outside")
else:
    print("Grab a jacket before you go out")

if temp>35:
    print("Weather scorishing hot ")
elif temp>25:
    print("Weather is warm & sunny")
elif temp>15:
    print("Weather:Cool and brezzy")
else:
    print("Weather cold stay warm!")

now=datetime.datetime.now()
print("city:",city)
print("time now:",now)
print(calendar.calendar(now.year))






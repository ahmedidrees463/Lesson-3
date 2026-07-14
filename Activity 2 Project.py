

name = input("Enter your name: ")
mood = input("How are you feeling today? happy/sad/tired/stressed/excited: ")
energy = int(input("Enter your energy level from 1 to 10: "))


if energy < 3:
    print("Alert: Your energy is low take some rest.")


if energy >= 5:
    print("You have Enough Energy today go and play outside !")
else:
    print("Take it slow take some rest.")


if mood == "happy":
    advice = "Glad to hear that keep being happy!"
elif mood == "sad":
    advice = "Looks like your having a rough day go play outside or talk to friends that will make you have better day."
elif mood == "tired":
    advice = "Take it slow Dinrk some water and do take some rest."
elif mood == "stressed":
    advice = "Sorry to hear that try deep breathing."
elif mood == "excited":
    advice = "Happy to hear that make something creative today!"
else:
    advice = "Take care of yourself and take some rest.."


import datetime

today = datetime.datetime.now()

print("\n================================")
print("DAILY MOOD ADVISOR REPORT")
print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy)
print("Date and Time:", today)
print("Advice:", advice)


try:
    Number_of_Isotopes = int(input("Choose the number of Isotopes for your element. (Whole positive numbers) "))
except ValueError or TypeError:
    print("Whole numbers")
    exit()
if Number_of_Isotopes < 1:
    raise Exception("Positive please")

Is_100 = 0
Percent = []
Weight = []
Number_element = 1
Final = 0

for x in range(Number_of_Isotopes):
    print("Enter the percent abundance of " + str(Number_element) + "st/th element")
    try:
        Percent.append((int(input())))
    except ValueError:
        print("A whole number please")
        exit()
    print("Enter the mass of that one")
    try:
        Weight.append(int(input()))
    except ValueError:
        print("A WHOLE NUMBER I SAID")
        exit()
    Is_100 += Percent[Number_element - 1]
    if Percent[Number_element - 1] < 0 or Weight[Number_element - 1] < 0:
        print("Why did you enter negative numbers though?")
        exit()
    Number_element += 1

if Is_100 != 100:
    print("The percentages should be 100 total")
    exit()
Number_element = 0
for x in range(Number_of_Isotopes):
    Final += (Percent[Number_element]/100) * (Weight[Number_element])
    Number_element += 1
print("The average atomic mass of said element is " + str(Final))
print("Thank you for using this program made by Eitan Ben-Ari")

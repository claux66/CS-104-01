#Averaging Algorithm

total = 0
averave = 0
howManyEntered = 0
howMany = int(input("How many test scores would you like to average?   "))
while howManyEntered != howMany:
    howManyEntered =howManyEntered +1
    testScore = int(input("Enter test score:    "))
    total = total + testScore
average = total / howMany
print("The average for the test scores you entered is",average)

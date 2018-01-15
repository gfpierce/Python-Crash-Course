guests = ['JJ Abrams', 'Guido van Rossum', 'Sturgill Simpson']

print('Hello ' + guests[0] + ', would you like to come to dinner?')
print('Hello ' + guests[1] + ', would you like to come to dinner?')
print('Hello ' + guests[2] + ', would you like to come to dinner?')

print("Unfortunately, " + guests[2] + " can't make it.")

guests[2] = 'Luke Skywalker'

print("I'll invite " + guests[2] + " instead.")

print("")

print("I found a bigger table, so we'll be adding a few guests.")

guests.insert(0, 'Ben Howard')
guests.insert(2, 'Jeff Bezos')
guests.append('R2-D2')

print('Hello ' + guests[0] + ', would you like to come to dinner?')
print('Hello ' + guests[1] + ', would you like to come to dinner?')
print('Hello ' + guests[2] + ', would you like to come to dinner?')
print('Hello ' + guests[3] + ', would you like to come to dinner?')
print('Hello ' + guests[4] + ', would you like to come to dinner?')
print('Hello ' + guests[5] + ', would you like to come to dinner?')

print("")

print("I regret to inform you I can only invite two people for dinner. Amazon won't have my new dinner table here in "
      "time. Bezos, you're obviously out.")
guests.pop()
guests.pop()
guests.pop()
guests.pop()

print('Hello ' + guests[0] + ', would you like to come to dinner?')
print('Hello ' + guests[1] + ', would you like to come to dinner?')

del guests[1]
del guests[0]

print(guests)
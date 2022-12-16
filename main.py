import random

Deck = [ "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", 
         "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", 
        "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦",
         "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥"]
print("Your Cards:")
for count in range(2):
    card = random.choice(Deck)
    print(card)
    Deck.remove(card)

print()
print("Cards Remaining in Deck:")
Deck.sort(     )
print(Deck)

print()
num = input
x = (int(input("Type your first number here to see your value:  ")))

y = (int(input("Type your second number here to see your total value:  ")))
print(x + y)
if (x+y) <21:
  print("Since you are less than 21 here is another card!") 
  print()
  print("Your Cards:")
for count in range(1):
    card = random.choice(Deck)
    print(card)
    Deck.remove(card)
if (x+y) >21:
 print("You lost!")
print()
print("Cards Remaining in Deck:")
Deck.sort(     )
print(Deck)
x = (int(input("Type your first number here to see your value:  ")))

y = (int(input("Type your second number here to see your total value:  ")))
z = (int(input("Type your third number here to see your value:  ")))
print(x + y + z)
if (x+ y +z) <21:
  print("Since you have less than 21 here is another card!")
if (x + y +z) >21:
  print ("You lost!")
for count in range(1):
    card = random.choice(Deck)
    print(card)
    Deck.remove(card)
x = (int(input("Type your first number here to see your value:  ")))

y = (int(input("Type your second number here to see your value:  ")))
z = (int(input("Type your third number here to see your value:  ")))
w = (int(input("Type your fourth number here to see your total value:   ")))
if (x+ y + z + w) <21:
  print("Since you have less than 21 here is another card!")
if (x + y +z + w) >21:
  print ("You lost!")
else:
  print("YOU WIN!")
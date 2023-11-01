import random

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
play_again = 'yes'
while play_again == 'yes':
  value += random.choice(card_values)
  print("First card was "+str(sum))
  turn = "hit"
  while turn == "hit":
      value = random.choice(card_values)
      print("Second card was "+str(value))
      sum += value
      print("You currently have: " + str(sum))
      if sum >= 21:
        break
      turn = input("What do you want to do? ")

  if sum == 21:
    print("You got Blackjack!")
  elif sum > 21:
    print("Busted")
  else:
    print("You stopped at: " + str(sum))

  play_again = input("Want to play again? ")

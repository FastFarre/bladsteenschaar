import random
print("blad steen schaar spelletje")
def main():
  print("")
  print("blad = 1")
  print("steen = 2")
  print("schaar = 3")
  print("")
  selection = int(input("kies blad, steen of schaar: "))
  bot_selection = random.randint(1, 3)
  options = ["blad", "steen", "schaar"]
  winner = [[1, 2], [2, 3], [3, 1]]
  print("\njij koos: " + options[selection - 1])
  print("bot koos: " + options[bot_selection - 1])
  
  def check_winner(a, b):
    global player_won
    if a == b:
      print("niemand heeft gewonnen. Probeer opnieuw")
      main()
    else:
      for i in range(3):
        if a == winner[i][0] and b == winner[i][1]:
          player_won = True
        elif b == winner[i][0] and a == winner[i][1]:
          player_won = False
  check_winner(selection, bot_selection)
main()
if player_won == True:
  print("\nplayer won")
else:
  print("\nbot won")
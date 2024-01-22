def show_game_board():
     
          for i in range (3):
              for j in range (3):
                  print (game[i][j],end="   ") 
          print ()

game=[["-","-","-"],
      ["-","-","-"],
      ["-","-","-"]]

show_game_board()

while True:
          print ("player 1")
          row = int(input("enter row: "))
          col = int(input("enter col: "))
          game [row][col]="X"

          show_game_board()

          print("player 2")
          row = int(input("enter row: "))
          col = int(input("enter col: "))
          game [row][col]="O"

          show_game_board()
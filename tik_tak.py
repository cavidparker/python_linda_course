game = [
    [0, 0 ,0],
    [0, 0, 0],
    [0, 0, 0]
]

def game_board(player=0, row=1, column=1):
    print("   a, b, c")
    if not just_display:
        game[row][column] = player
    for count,games in enumerate(game):
        print(count, games)



game_board()
game_board(player=1, row=2, column=1)

# game[0][1] = 1

# game_board()
    
   
    
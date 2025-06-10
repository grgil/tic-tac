import pandas as pd

board = {'A': ['-' , '-' , '-'], 'B': ['-' , '-' , '-'], 'C': ['-' , '-' , '-']}
df = pd.DataFrame(board, index=['1', '2', '3'])
print(df)

NoWinner = True
while NoWinner:
    move = input('enter player one next move - ')
    column = move[0]
    row = move[1]
    df.loc[row, column] = 'X'
    print(df)

    move = input('enter player two next move - ')
    column = move[0]
    row = move[1]
    df.loc[row, column] = 'O'
    print(df) 
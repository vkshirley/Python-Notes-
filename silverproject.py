#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
          


# In[3]:


board=['#','X','O','X','O','X','O','X','O','X','O']


# In[4]:


display_board(board)


# In[5]:


def player_input():
    marker=''
    while not (marker == 'X' or marker == "O"):
        marker =input("enter a marker x\o :").upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    


# In[6]:


player_input()


# In[9]:


def place_marker(board,marker,position):
    board[position] = marker


# In[10]:


place_marker(board,"X",5)


# In[13]:


display_board(board)


# In[16]:


def win_check(board,marker):
    if( (board[7]==marker and board[8]==marker and board[9]==marker) or 
        (board[4]==marker and board[5]==marker and board[6]==marker) or
        (board[1]==marker and board[2]==marker and board[3]==marker) or
        (board[7]==marker and board[4]==marker and board[1]==marker) or
        (board[8]==marker and board[5]==marker and board[2]==marker) or
        (board[9]==marker and board[6]==marker and board[3]==marker) or
        (board[7]==marker and board[5]==marker and board[3]==marker) or
        (board[9]==marker and board[5]==marker and board[1]==marker)):
         return True
    else:
         return False


# In[17]:


win_check(board,'X')


# In[18]:


win_check(board,'O')


# In[19]:


import random
def choose_first():
    num=random.randint(0,1)
    if num==1:
        return 'Player 1'
    else:
        return 'Player 2'


# In[20]:


choose_first()


# In[21]:


board =['#','X','O','O','O','X',' ','X',' ','X','O']


# In[22]:


def space_check(board,position):
    return board[position]== ' '


# In[23]:


space_check(board,6)


# In[24]:


def full_board_check(board):
    isFull = True
    for i in board:
        if i == ' ':
            isFull = False
    return isFull


# In[25]:


full_board_check(board)


# In[27]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[28]:


full_board_check(board)


# In[29]:


def players_choice(board):
    position = 0 
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("enter your next positon ; " ))
    return position
        


# In[31]:


players_choice(board)


# In[32]:


def replay():
    return input("do you want to play again (Y/N) : ").lower().startswith('y')


# In[ ]:


replay()


# In[ ]:


while True:
    board = [' ']* 10
    player1_marker,player2_marker = player_input()
    turn= choose_first()
    print(turn + "will play first")
    play_game = input("you ready ?!? ").lower().startswith('y')
    
    if play_game:
        game_on = True
    else:
        game_on = False 
    while game_on:
        if turn == 'PLayer 1':
            display_board(board)
            position = players_choice(board)
            place_marker(board,player1_marker,position)
            
            if win_check(board,player1_marker):
                display_board(board)
                print("PLayer 1 jeet gya , enjoy ")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("are re game draw ho gya ")
                    break
                else:
                    turn = "player 2 "
        else:
            display_board(board)
            position = players_choice(board)
            place_marker(board,player2_marker,position)
            
            if win_check(board,player2_marker):
                display_board(board)
                print("PLayer 2 jeet gya , enjoy ")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("are re game draw ho gya ")
                    break
                else:
                    turn = "player 1 "
    if not replay():
        break
            


# In[ ]:





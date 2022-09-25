from tkinter.tix import COLUMN


#searches for the position of a number
def search(arr,num):
    row = 0
    col = 0
    for i in range(3):
        for j in range(3):
            if (arr[i][j] == num):
                #print("position %d %d"%(i,j))
                row = i
                col = j
    return row, col

# used to find all the possible actions
'''
def actions(arr):
    action_list = [0,0,0,0]
    action_list_index = 0
    row, col = search(arr,0) #searches the empty tile and saves its position

    for i in range(3):
        for j in range(3):
            empty_tile = arr[row][col]
            cur_tile = arr[i][j]
            if empty_tile !=  cur_tile:
                #print(i,j)
                if i == row or j == col:
                    if ((row - 1 == i) or (row + 1 == i)) or ((col - 1 == j) or (col + 1 == j)):
                        if(row - 1 == i):
                            action_list[action_list_index] = "U"
                        elif(row + 1 == i):
                            action_list[action_list_index] = "D"
                        elif(col - 1 == i):
                            action_list[action_list_index] = "L"
                        else:
                            action_list[action_list_index] = "R"

                        action_list_index = action_list_index + 1

    return action_list
'''

def actions(arr):
    action_list = []
    row, col = search(arr,0) #searches the empty tile and saves its position
    for i in range(3):
        for j in range(3):
            empty_tile = arr[row][col]
            cur_tile = arr[i][j]
            if empty_tile !=  cur_tile:
                #print(i,j)
                if i == row or j == col:
                    if ((row - 1 == i) or (row + 1 == i)) or ((col - 1 == j) or (col + 1 == j)):
                        if(row - 1 == i):
                            action_list.append("U")
                        elif(row + 1 == i):
                            action_list.append("D")
                        elif(col - 1 == i):
                            action_list.append("L")
                        else:
                            action_list.append("R")
    return action_list


def goalTest(arr):
    row,col = search(arr,0)
    if row == 2 and col == 2:
        return True
    else:
        return False


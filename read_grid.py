def input_to_grid():
    with open("puzzle.in", mode="r") as file:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
    
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0,3):
        if i == 0:
            grid[i][0] = int(line1[0])
            grid[i][1] = int(line1[2])
            grid[i][2] = int(line1[4])
        elif i == 1:
            grid[i][0] = int(line2[0])
            grid[i][1] = int(line2[2])
            grid[i][2] = int(line2[4])
        else:
            grid[i][0] = int(line3[0])
            grid[i][1] = int(line3[2])
            grid[i][2] = int(line3[4])

    return grid

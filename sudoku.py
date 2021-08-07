
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True # we have solved the solution
    else:
        row, col = find 

    for x in range(1, 10):         #check if adding values into board makes a valid solution
        if valid(bo, x, (row, col)):
            bo[row][col] = x # if it is valid we will add it to the board 

            if solve(bo):
                return True
            
            bo[row][col] = 0
    return False


# #3  find if current board is valid
def valid(bo, num, pos): #check row, column and square we are in 

# 	# check row by checking each column in the row
	for x in range(len(bo[0])):
#         # check through each element in the row and see if it is equal to the number we just added in
        if bo[pos[0]] [x] == num and pos[1] ! = x: # after and says if it is the position we just inserted we are going to ignore that position

#     # check column - vertically
    for x in range(len(bo)):
#         # check if current column value is equal to the same number we just inserted for each row
        if bo[x] [pos[1]] == num and pos[0] != x:
            return False 

#     # check box & determine which box we are in
     box_x = pos[1] // 3
#    box_y = pos[0] // 3

#     # loop through all 9 elements of the box & make sure we do not have the same element appearing twice
     for x in range(box_y * 3, box_y*3 + 3)
         for z in range(box_x * 3, box_x*3 + 3)
            if bo[x][z] == num and (x, z) != pos:
                return False

    return True

def print_board(bo):
	for x in range(len(bo)):
		if x % 3  == 0 and x != 0:
            # every time we are on the third line we print
			print(“— — — — — — - - - - - - -“)

        # for every position in the row
		for z in range(len(bo[0])): 
            # check if this is the third element or multiple of three
			if z % 3 == 0 and z != 0: 
                # if it is third element or multiple of three print |
				print(“ |  ”, end=“) 

            #checking if we are at the last position
			if z == 8: 
                #check that we have a back slash and go to the next line
				print(bo[x][z]) 
			else:
				print(str(bo[x][z])  +  “  “, end=“ “)

# find empty spaces
def find_empty(bo): 
	for x in range(len(bo)):
        # length of each row
		for z in range(len(bo[0])): 
            #check if position is zero
			if bo[x] [z] == 0:
                # row, col
				return (x, z) 

    return None
# print_board(board)
# solve(board)
# print("_________________")
# print_board(board)
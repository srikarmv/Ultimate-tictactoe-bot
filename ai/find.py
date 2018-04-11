def find_heuristic(temp_board,player,opponent,row,column):
	heuristic_value = 0


        for i in range(row,row+4):
		countr = 0
		countc = 0
		for j in range(column,column+4):
			
                        if temp_board[i][j] == player:                  #for row
				countr += 1
			
                        if temp_board[i][j] == opponent:
				countr = -10
                        
                        if temp_board[j-column+row][i-row+column] == player:                  # for column
				countc += 1

			
                        if temp_board[j-column+row][i-row+column] == opponent:
				countc = -10
                
                if countr == 1:
			heuristic_value += 1
		elif countr == 2:
			heuristic_value += 10
		elif countr == 3:
			heuristic_value += 70
		elif countr==4:
			heuristic+value+=100
                if countc == 1:
			heuristic_value += 1
		elif countc == 2:
			heuristic_value += 10
		elif countc == 3:
			heuristic_value += 70
		elif countc==4:
			heuristic+value+=100
        count=0
	for i in range (4):                                             # first diagonal
		if temp_board[row+i][column+i] == player:
			count += 1
		if temp_board[row+i][column+i] == opponent:
			count -= 10
        if count == 1:
		heuristic_value += 1
	elif count == 2:
		heuristic_value += 10
	elif count == 3:
		heuristic_value += 70
	elif count == 4:
		heuristic_value += 100



	count=0
	for i in range (4):                                             # second diagonal
		if temp_board[row+i][column+3-i] == player:
			count += 1
		if temp_board[row+i][column+3-i] == opponent:
			count -= 10


        if count == 1:
		heuristic_value += 1
	elif count == 2:
		heuristic_value += 10
	elif count == 3:
		heuristic_value += 70
        elif count == 4:
		heuristic_value += 100
	if heuristic_value > 100:   
		heuristic_value = 100
	return  (heuristic_value*1.0)/100
	

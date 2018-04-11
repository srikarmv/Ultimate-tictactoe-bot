def calculate_heuristic_block(temp_board,block_no,player):
        row=(block_no/4)*4
        column=(block_no%4)*4
	if player == 1:
            player = 'x'
	    opponent = 'o'
        else:
	    player = 'o'
	    opponent = 'x'
        return find_heuristic(temp_board,player,opponent,row,column)

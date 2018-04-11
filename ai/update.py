def update(temp_board, block_stat, move_ret, fl):

        block_no = (move_ret[0]/4)*4 + move_ret[1]/4	
	startx = (block_no/4)*4
	starty = (block_no%4)*4
	mflg = 0
        flag = 0
	for i in range(startx,startx+4):  
		for j in range(starty,starty+4):
			if temp_board[i][j] == '-':
				flag = 1
        x=move_ret[0]-startx
        y=move_ret[1]-starty
        bl=3*x+y
        if(block_stat[block_no]== '-'):
            if(check_won_along_path(bl,temp_board,startx,starty)==1):
                mflg=1

        if flag == 0:
		block_stat[block_no] = 'D'
	if mflg == 1:
		block_stat[block_no] = fl
	return block_stat

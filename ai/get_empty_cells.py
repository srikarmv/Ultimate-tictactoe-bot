def get_empty_cells(block_stat,game_board, a_b,count):
        empty_cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	for idb in a_b:
		id1 = idb/4
		id2 = idb%4
		for i in range(id1*4,id1*4+4):
			for j in range(id2*4,id2*4+4):
				if game_board[i][j] == '-':
					empty_cells.append((i,j))
    
        #    print "z"
         #   print empty_cells
    
	# If all the possible blocks are full, you can move anywhere
	if empty_cells == [] and count==0:
            new=[]

            for i in range(0,16):
                if(block_stat[i]=='-'):
                    new.append(i)
            
            return get_empty_cells(block_stat,game_board,new,1)
                
	'''	for idb in new_blal:
			id1 = idb/3
			id2 = idb%3
			for i in range(id1*3,id1*3+3):
				for j in range(id2*3,id2*3+3):
					if gameb[i][j] == '-':
						cells.append((i,j))'''
	return empty_cells

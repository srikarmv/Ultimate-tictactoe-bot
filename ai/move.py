def move(self, temp_board, old_move, flag):
		if(flag=='x')
		   k='o'
		else
		   k='x'
		temp_block = update(temp_board,temp_block,old_move,k)  
		cccc = 0
                global moves
                global heuristic_arr1
                if(flag=='x'):
                 temp=1
                else:   
                    temp=0
                if(old_move!=(-1,-1)):

                    block_number=find_block_from_move(old_move)
                    heuristic_arr1[block_number]=assign_heuristic(temp_board,block_number,temp) 
                else:
                    temp_board[3][3]='x'
                    heuristic_arr1[4]=assign_heuristic(temp_board,4,temp)
                    temp_board[3][3]='-'


                if(flag=='x' and old_move[0]==-1 and old_move[1]==-1):
                    return (3,3)
                
                blocks_allowed = determine_allowed_blocks(old_move, temp_block)
		cells  = get_empty_cells(temp_block,temp_board, blocks_allowed,0)
                if(moves>=60):
                        ply=7

                elif(moves>=30):
                        ply=6
                else:
                        ply=5

                best_cell = findbestcell(temp_board,cells,old_move,ply,temp,temp_block,-10e6,10e6,temp,heuristic_arr1)
                block_number=find_block_from_move(f(best_cell))
                temp_board[best_cell[0]][best_cell[1]]=flag
		temp_block = update(temp_board,temp_block,best_cell,flag) 
                heuristic_arr1[block_number]=assign_heuristic(temp_board,block_number,temp) 
                temp_board[best_cell[0]][best_cell[1]]='-'
                moves+=1
                return f(best_cell)

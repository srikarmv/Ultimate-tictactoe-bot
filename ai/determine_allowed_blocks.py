def determine_allowed_blocks(old_move, temp_block):
	blocks_allowed = []
        if old_move[0]%4==0:
            if old_move[1]%4==0:
		blocks_allowed.append(0)
               
            elif old_move[1]%3==1:
                blocks_allowed.append(1)
             
            elif old_move[1]%4==2:
              
                blocks_allowed.append(2)
	    else
		blocks_allowed.append(3)
       	if old_move[0]%4==1:
            if old_move[1]%4==0:
		blocks_allowed.append(4)
               
            elif old_move[1]%3==1:
                blocks_allowed.append(5)
             
            elif old_move[1]%4==2:
              
                blocks_allowed.append(6)
	    else
		blocks_allowed.append(7)
 	if old_move[0]%4==2:
            if old_move[1]%4==0:
		blocks_allowed.append(8)
               
            elif old_move[1]%3==1:
                blocks_allowed.append(9)
             
            elif old_move[1]%4==2:
              
                blocks_allowed.append(10)
	    else
		blocks_allowed.append(11)
 	if old_move[0]%4==3:
            if old_move[1]%4==0:
		blocks_allowed.append(12)
               
            elif old_move[1]%3==1:
 		blocks_allowed.append(13)
           
            elif old_move[1]%4==2:             
                blocks_allowed.append(14)
	    else
		blocks_allowed.append(15)
        else:
            sys.exit(1)
        final_blocks_allowed = []
	for i in blocks_allowed:
		if temp_block[i] == '-':
			final_blocks_allowed.append(i)
	return final_blocks_allowed

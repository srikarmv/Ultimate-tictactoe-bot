from operator import itemgetter
import copy
import time

temp = 0
cccc = 0
moves=0
heuristic_arr1=[]
block_list=[]
temp_block=[]
class Player143:
	def __init__(self):
                global moves
                moves=0
                global heuristic_arr1
                global block_list
		global temp_block
		temp_block=['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
                heuristic_arr1=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
                for i in range(16):
                    block_list.append([])
                block_list[0].append([0,1,2,3])
                block_list[0].append([0,5,10,15])
                block_list[0].append([0,4,8,12])
                block_list[1].append([0,1,2,3])
                block_list[1].append([1,5,9,13])
                block_list[2].append([0,1,2,3])
                block_list[2].append([2,6,10,14])
                block_list[3].append([0,1,2,3])
                block_list[3].append([3,7,11,15])
                block_list[3].append([3,6,9,12])
                block_list[4].append([4,5,6,7])
                block_list[4].append([0,4,8,12])
                block_list[5].append([1,5,9,13])
                block_list[5].append([4,5,6,7])
                block_list[5].append([0,5,10,15])
                block_list[6].append([4,5,6,7])
                block_list[6].append([2,6,10,14])
                block_list[6].append([3,6,9,12])
                block_list[7].append([3,7,11,15])
                block_list[7].append([4,5,6,7])
                block_list[8].append([0,4,8,12])
                block_list[8].append([8,9,10,11])
                block_list[9].append([8,9,10,11])
                block_list[9].append([3,6,9,12])
                block_list[9].append([2,5,9,13])
                block_list[10].append([2,6,10,14])
                block_list[10].append([8,9,10,11])
                block_list[10].append([0,5,10,15])
                block_list[11].append([3,7,11,15])
                block_list[11].append([8,9,10,11])
                block_list[12].append([12,13,14,15])
                block_list[12].append([0,4,8,12])
                block_list[12].append([3,6,9,12])
                block_list[13].append([1,5,9,13])
                block_list[13].append([12,13,14,15])
                block_list[14].append([12,13,14,15])
                block_list[14].append([2,6,10,14])
                block_list[15].append([12,13,14,15])
                block_list[15].append([3,7,11,15])
                block_list[15].append([0,5,10,15])

		pass
	def move(self, board, old_move, flag):

		temp_board = board.board_status
		kk = board.block_status
		if(flag=='x'):
		   k='o'
		else:
		   k='x'
		global temp_block
		for i in range(0,4):
			for j in range(0,4):
				temp_block[i*4+j]=kk[i][j]
		#temp_block = update(temp_board,temp_block,old_move,k)

		cccc = 0
                global moves
                global heuristic_arr1
                if(flag=='x'):
                 temp=1
                else:
                    temp=0
                if(old_move!=(-1,-1)):
 		    #print 'sdfasf'
                    block_number=find_block_from_move(old_move)
		    #print 'sdf12asf'
                    heuristic_arr1[block_number]=assign_heuristic(temp_board,block_number,temp)
		    #print 'sdsrf12asf'
                else:

                    temp_board[3][3]='x'

                    heuristic_arr1[0]=assign_heuristic(temp_board,5,temp)
                    temp_board[3][3]='-'


                if(flag=='x' and old_move[0]==-1 and old_move[1]==-1):

			return (3,3)
                #print temp_block,old_move
                blocks_allowed = determine_allowed_blocks(old_move, temp_block)
		#print 'asdfasdfasdfasdf'
		cells  = get_empty_cells(temp_block,temp_board, blocks_allowed,0)
		#print 'sdsrf12asfsdfasfasf'
                if(moves>=60):
                        ply=3

                elif(moves>=30):
                        ply=4
                else:
                        ply=4

                best_cell = findbestcell(temp_board,cells,old_move,ply,temp,temp_block,-10e6,10e6,temp,heuristic_arr1)
                block_number=find_block_from_move(f(best_cell))
                temp_board[best_cell[0]][best_cell[1]]=flag
		#print '12312345fsdfasfasf'
		temp_block = update(temp_board,temp_block,best_cell,flag)
		#	print '123456789'
		heuristic_arr1[block_number]=assign_heuristic(temp_board,block_number,temp)
                temp_board[best_cell[0]][best_cell[1]]='-'
                moves+=1
		#print blocks_allowed
		#print temp_block
		print 'Hello',best_cell[0],best_cell[1],'hello'
                return f(best_cell)
def f(t):
	return (t[0],t[1])

def assign_heuristic(temp_board,block_no,me):
	h1=calculate_heuristic_block(temp_board,block_no,me)
	h2=calculate_heuristic_block(temp_board,block_no,1-me)
	#h2=1212;
	if(h1==1):
	   return 1
	elif(h2==-1):
	   return -1
	else:
	   return h1-h2
def find_block_from_move(move):
	block_number = (move[0]/4)*4 + move[1]/4
	return block_number

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
	bl=4*x+y

	if(block_stat[block_no]== '-'):
	    if(check_won_along_path(bl,temp_board,startx,starty)==1):
	        mflg=1

	if flag == 0:
		block_stat[block_no] = 'D'
	if mflg == 1:
		block_stat[block_no] = fl
	return block_stat
def check_won(bl,temp_block,player):
	for i in block_list[bl]:
		f=temp_block[i[0]]
		mflg=1
		if(f!=player):
   			continue
		for j in range(1,len(i)):
  			if(f!=temp_block[i[j]]):
       				mflg=0
       			     	break
		if(mflg==1):
    			return 1
	return 0
def check_won_along_path(bl,temp_board,startx,starty):
    global block_list
    mflg=1
    for i in block_list[bl]:
            sx=i[0]/4
            sy=i[0]%4
            f=temp_board[startx+sx][starty+sy]
            if(f=='-'):
                continue
            mflg=1
            for j in range(1,len(i)):
                if(f!=temp_board[startx+i[j]/4][starty+i[j]%4]):
                    mflg=0
                    break
            if(mflg==1):
                return 1
    return 0
def findbestcell(temp_board,cells,old_move,level,player,temp_block,alpha,beta,me,heuristic_arr):
	if(me==1):
	    a='x'
	    b='o'
	else:
	    a='o'
	    b='x'
    	if level == 0:

	        h=calculate_heuristic(temp_board,me,heuristic_arr)
		#print 'tereere',h
	        return (0,0,h)

	else:
	        if(player==me):
	            v=(0,0,-10e9)
	        else:
	            v=(0,0,10e9)

	        for cell in cells:
	             	#print 'vinay'
			#print cell[0],cell[1],player
			if player == 1:
	                        temp_board[cell[0]][cell[1]]='x'
	                else:
				temp_board[cell[0]][cell[1]]='o'

	                bl_number=find_block_from_move(cell)
			save1=temp_block[bl_number]
			save=heuristic_arr[bl_number]
	                if(player==1):
	                        x='x'
	                        y='o'
	                else:
	                        x='o'
	                        y='x'
	                temp_block=update(temp_board,temp_block,cell,x)
	                if  check_won(bl_number,temp_block,a)==1 :
	                        c=cell + (10000,)
	                        temp_board[cell[0]][cell[1]]='-'
	                        heuristic_arr[bl_number]=save
	                        temp_block[bl_number]=save1
				#print '1'
	                        return c
	                elif check_won(bl_number,temp_block,b)==1 :
	                        c=cell + (-10000,)
				#print '2'
	                else:

	                    heuristic_arr[bl_number]=assign_heuristic(temp_board,bl_number,me)

	                    blocks_all = determine_allowed_blocks(cell,temp_block)
	                    cell2  = get_empty_cells(temp_block,temp_board, blocks_all,0)
	                    if(cell2==[]):
				#print 'temp'
	                        if (temp_block.count(a)> temp_block.count(b)):
	                            heur=10000
	                        elif(temp_block.count(b)> temp_block.count(a)):
	                            heur=-10000
	                        else:
	                            heur=calculate_heuristic(temp_board,me,heuristic_arr)
	                        c=cell + (heur,)

	                    else:
				#print 'care',blocks_all
	                        t=findbestcell(temp_board,cell2,cell,level-1,1-player,temp_block,alpha,beta,me,heuristic_arr)
				#print 'swer',level
				c=cell+ (t[2],)
			    #print '12334567'
	                heuristic_arr[bl_number]=save
			temp_block[bl_number]=save1

	                temp_board[cell[0]][cell[1]]='-'
	                if(player==me):
	                    if c[2] > v[2]:
	                        v = c
	                    if v[2] > alpha:
	                       alpha = v[2]
	                    if alpha >= beta:
	                       break
	                else:
	                    if v[2] > c[2]:
	                       v=c
	                    if beta > v[2]:
	                        beta = v[2]
	                    if alpha >= beta:
	                        break

	        return v
def calculate_heuristic(temp_board,player,heuristic):

	h=0
	h += convert_heuristic(heuristic,0,1,2,3)
	h += convert_heuristic(heuristic,4,5,6,7)
	h += convert_heuristic(heuristic,8,9,10,11)
	h += convert_heuristic(heuristic,12,13,14,15)
	h += convert_heuristic(heuristic,0,4,8,12)
	h +=convert_heuristic(heuristic,1,5,9,13)
	h += convert_heuristic(heuristic,2,6,10,14)
	h +=convert_heuristic(heuristic,3,7,11,15)
	h +=convert_heuristic(heuristic,0,5,10,15)
	h +=convert_heuristic(heuristic,3,6,9,12)
	return h
def convert_heuristic(heuristic,i,j,k,l):

	h=0
	temp = heuristic[i] + heuristic[j] + heuristic[k] + heuristic[l]
	flag=0
	if(temp<0):
	    flag=1
	p_80=0
	p_20=0
	lose=0
	p_0=0
	n_0=0
	n_20=0
	n_80=0
	win=0
	temp = heuristic[i] + heuristic[j] + heuristic[k] + heuristic[l]
	a=[i,j,k,l]
	b=[]
	for q in a:
	    b.append(heuristic[q])
	pos=0
	for i in b:
#            if(i>=0):
#               pos+=1
	    if i ==-1:
	        lose+=1
	    elif i==1:
	        win+=1
	    elif i > 0.15:
	        p_80+=1
	    elif i >= 0.08:
	        p_20+=1
	    elif i > 0:
	        p_0 += 1
	    elif i < -0.15:
	        n_80 += 1
	    elif i <= -0.08:
	        n_20 += 1
	    elif i< 0:
	        n_0 += 1
	if(p_80==3 and n_20==1):
	    temp=temp*0.8
	if(p_80==3 and n_80==1):
	    temp=temp*0.9
	if(p_80==3 and lose==1):
	    temp=temp*0.5
	if(p_20==3 and n_80==1):
	        temp=temp*0.9
	if(p_20==3 and lose==1):
	    temp=temp*0.3


	if(win==3 and n_80==1):
	    temp=temp*0.3
	if(win==3 and lose==1):
	    temp=0

	if(n_80==3 and p_80==1):
	    temp=temp*1
	if(n_80==3 and win==1):
	    temp=temp*0.4

	if(n_20==3 and p_80==1):

	        temp=temp*0.8
	if(n_20==3 and win==1):
	    temp=temp*0.6

	if(lose==3 and win==1):
	    temp=0
	if(lose==3 and p_80==1):
	    temp=temp*0.3


	if(win==1 and p_0==3):
	    temp=temp*0.4
	elif (p_80==1 and p_0==3):
	    temp=temp*0.7
    #    elif(p_80==1 and p_20==2):


	if(lose==1 and n_0==3):
	    temp=temp*0.4
	elif (n_80==1 and n_0==3):
	    temp=temp*0.7

	if(flag==1):
	    temp=-temp
	if temp < 0.32:
	    h += temp
	elif temp >= 0.32 and temp <= 0.79:
	    h += ( (temp -0.24) *12) + 1
	elif temp >= 0.79 and temp <4:
	    h = (temp-0.79)*90 + 10
	elif temp>=4:
	    h +=1000
	if(flag==1):
	    return -h
	else:
	    return h
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
			heuristic_value += 80
		elif countr==4:
			heuristic_value+=500
	        if countc == 1:
			heuristic_value += 1
		elif countc == 2:
			heuristic_value += 10
		elif countc == 3:
			heuristic_value += 80
		elif countc==4:
			heuristic_value+=500
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
		heuristic_value += 80
	elif count == 4:
		heuristic_value += 500



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
		heuristic_value += 80
	elif count == 4:
		heuristic_value += 500
	if heuristic_value > 500:
		heuristic_value = 500
	return  (heuristic_value*1.0)/500
def determine_allowed_blocks(old_move, temp_block):
	blocks_allowed = []

	if old_move[0]%4==0:
	    if old_move[1]%4==0:
		blocks_allowed.append(0)

	    elif old_move[1]%4==1:
	        blocks_allowed.append(1)

	    elif old_move[1]%4==2:

	        blocks_allowed.append(2)
	    else:
		blocks_allowed.append(3)
       	elif old_move[0]%4==1:
	    if old_move[1]%4==0:
		blocks_allowed.append(4)

	    elif old_move[1]%4==1:
		#print 'wenrt'
	        blocks_allowed.append(5)
		#print 'dfbvvz'

	    elif old_move[1]%4==2:

	        blocks_allowed.append(6)
	    else:
		blocks_allowed.append(7)
 	elif old_move[0]%4==2:
	    if old_move[1]%4==0:
		blocks_allowed.append(8)

	    elif old_move[1]%4==1:
	        blocks_allowed.append(9)

	    elif old_move[1]%4==2:

	        blocks_allowed.append(10)
	    else:
		blocks_allowed.append(11)
 	elif old_move[0]%4==3:
	    if old_move[1]%4==0:
		blocks_allowed.append(12)

	    elif old_move[1]%4==1:
 		blocks_allowed.append(13)

	    elif old_move[1]%4==2:
	        blocks_allowed.append(14)
	    else:
		blocks_allowed.append(15)
	else:
	    sys.exit(1)
	#print 'sadfsddfasdfasdf'
	#print 'asdfsdf'
	final_blocks_allowed = []
	for i in blocks_allowed:
		if temp_block[i] == '-':
			final_blocks_allowed.append(i)
	if final_blocks_allowed == []:
		#print 'U entered'
		#print temp_block
		for i in range(0,16):
			if temp_block[i] == '-':
				final_blocks_allowed.append(i)
				#break;
	return final_blocks_allowed
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
def get_empty_out_of(gameb, blal,block_stat):
	cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	for idb in blal:
		id1 = idb/4
		id2 = idb%4
		for i in range(id1*4,id1*4+4):
			for j in range(id2*4,id2*4+4):
				if gameb[i][j] == '-':
					cells.append((i,j))

	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		new_blal = []
		all_blal = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
		for i in all_blal:
			if block_stat[i]=='-':
				new_blal.append(i)

		for idb in new_blal:
			id1 = idb/4
			id2 = idb%4
			for i in range(id1*4,id1*4+4):
				for j in range(id2*4,id2*4+4):
					if gameb[i][j] == '-':
						cells.append((i,j))
	return cells

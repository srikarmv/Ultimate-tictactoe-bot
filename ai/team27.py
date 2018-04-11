from operator import itemgetter
import copy
import time
gamwo=0
temp = 0
cccc = 0
moves=0
heuristic_arr1=[]
block_list=[]
temp_block=[]
class Player27:
	def __init__(self):
                global moves
                moves=0
		blocwo=0
                global heuristic_arr1
                global block_list
		gmewo=0
		global temp_block
		temp_block=['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
                heuristic_arr1=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
               
		i=0		
		while i<16:
                    block_list.append([])
		    i=i+1
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
		gamewo=0
		play=1            
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
                
                if(old_move==(-1,-1)):

                    temp_board[3][3]='x'
		    rrt=temp_board[3][3]
                    heuristic_arr1[0]=assign_heuristic(temp_board,5,temp)
                    temp_board[3][3]='-'
		    rrt=temp_board[3][3]
		else:
		#if(old_move!=(-1,-1)):
 		    #print 'sdfasf'
                    block_number=find_block_from_move(old_move)
		    #print 'sdf12asf'
	            told_mov=old_move
                    heuristic_arr1[block_number]=assign_heuristic(temp_board,block_number,temp)
		    #print 'sdsrf12asf'

                if(flag=='x'):
			if(old_move[0]==-1):
				if(old_move[1]==-1):
					r15fla=1					
					return (3,3)
		
		#	return (3,3)
                #print temp_block,old_move
                blocks_allowed = determine_allowed_blocks(old_move, temp_block)
		#print 'asdfasdfasdfasdf'
		intiadep=4
		cells  = get_empty_cells(temp_block,temp_board, blocks_allowed,0)
		
                if(moves>=60):
                        ply=3
			intiadep=intiadep-1
                elif(moves>=30):
                        ply=4
			intiadep=ply
                else:		                        
			ply=4
			intiadep=ply

                best_cell = findbestcell(temp_board,cells,old_move,ply,temp,temp_block,-10e6,10e6,temp,heuristic_arr1)
                block_number=find_block_from_move(f(best_cell))
		savee3=best_cell[0]
		savee4=best_cell[1]
                temp_board[best_cell[0]][best_cell[1]]=flag
		#print '12312345fsdfasfasf'
		temp_block = update(temp_board,temp_block,best_cell,flag)
		#	print '123456789'
		rafg3=heuristic_arr1[block_number]
		heuristic_arr1[block_number]=assign_heuristic(temp_board,block_number,temp)
		savee3=best_cell[0]
		savee4=best_cell[1]
                temp_board[best_cell[0]][best_cell[1]]='-'
                moves+=1
		#print blocks_allowed
		#print temp_block
		print 'Hello',best_cell[0],best_cell[1],'hello'
                return f(best_cell)
def f(t):
	rer=t[0]
	rer1=t[1]
	return (t[0],t[1])

def assign_heuristic(temp_board,block_no,me):
	h1=calculate_heuristic_block(temp_board,block_no,me)
	if(h1<-2):                             #g
		flag=2
	h2=calculate_heuristic_block(temp_board,block_no,1-me)
	#h2=1212;
	flahii=0
	if(h1==1):
	   flahii=1	
	   return flahii
	elif(h2==-1):
	   flahii=-1
	   return flahii
	else:
	   return h1-h2
def find_block_from_move(move):
	x1=(move[0]/4)*4
	y1=move[1]/4
	block_number = (move[0]/4)*4 + move[1]/4
	return block_number

def update(temp_board, block_stat, move_ret, fl):
	x1 = (move_ret[0]/4)*4
	y1 = move_ret[1]/4
	block_no = x1 + y1
	ty1=(block_no/4)*4
	tz1=(block_no%4)*4
	startx = ty1
	starty = tz1
	mflg = 0
	flag = 0
	i=startx
	
	while(i<startx+4):	
		
		j=starty
		while(j<starty+4):
			if temp_board[i][j] == '-':
				flag = 1
			else:
				flag1=-1
			j=j+1
		i=i+1
	x=move_ret[0]-startx
	y=move_ret[1]-starty
	xnw=4*x	
	bl=xnw+y

	if(block_stat[block_no]== '-'):
	    if(check_won_along_path(bl,temp_board,startx,starty)==1):
	        mflg=1
		lfaf=1
	    else:
		lfaf=-1

	if flag == 0:
		block_stat[block_no] = 'D'
		sace=block_stat[block_no]
	if flag==1:
		flag1=flag1+1
	if mflg == 1:
		block_stat[block_no] = fl
	if mflg==0:
		lfaf=-3
	return block_stat
def check_won(bl,temp_block,player):
	kent=0
	for i in block_list[bl]:
		f=temp_block[i[0]]
		mflg=1
		if(f!=player):
			kent=-1
   			continue
		else:
			j=1
			
			while(j<len(i)):
  				if(f!=temp_block[i[j]]):
       					mflg=0
       				     	break
				j=j+1
			if(mflg==1):
				kent=3
    				return 1
			else:
				kent=-1
	return 0
def check_won_along_path(bl,temp_board,startx,starty):
    global block_list
    mflg=1
    flaf=0
    for i in block_list[bl]:
            sx=i[0]/4
            sy=i[0]%4
	    m=startx+sx
	    n=starty+sy
            f=temp_board[m][n]
            if(f=='-'):
		flaf=-1
                continue
	    else:
		mflg=1
		j=1
		while(j<len(i)):
		
		    if(f!=temp_board[startx+i[j]/4][starty+i[j]%4]):
		        mflg=0
		        break
		    j = j+1 	
		if(mflg==1):
		    return 1
		else:
		    flaf=0
    return 0
def findbestcell(temp_board,cells,old_move,level,player,temp_block,alpha,beta,me,heuristic_arr):
	if(me==1):
	    a='x'
	    b='o'
	    sfl=1
	else:
	    a='o'
	    b='x'
	    sfl = 0
	#if(sfl==0):
	#	me=0
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
				sfa23=cell[0]
				sfa24=cell[1]
	                        temp_board[cell[0]][cell[1]]='x'
	                else:
				sfa23=cell[0]
				sfa24=cell[1]				
				temp_board[cell[0]][cell[1]]='o'

	                bl_number=find_block_from_move(cell)
			save1=temp_block[bl_number]
			savee2=bl_number
			save=heuristic_arr[bl_number]
			
	                if(player==1):
				sfl=1
	                        x='x'
				sfa23=cell[0]
	                        y='o'
				sfa24=cell[1]
	                else:
				sfl=0
	                        x='o'
				sfa23=cell[0]
	                        y='x'
				sfa24=cell[1]
	                temp_block=update(temp_board,temp_block,cell,x)
	                if  check_won(bl_number,temp_block,a)==1 :
	                        c=cell + (10000,)
				sfa23=cell[0]
				sfa24=cell[1]
	                        temp_board[cell[0]][cell[1]]='-'
	                        heuristic_arr[bl_number]=save
	                        temp_block[bl_number]=save1
				#print '1'
	                        return c
	                elif check_won(bl_number,temp_block,b)==1 :
				sfa23=cell[0]
				sfa24=cell[1]
	                        c=cell + (-10000,)
				#print '2'
	                else:
			    sfa23=cell[0]
			    sfa24=cell[1]
	                    heuristic_arr[bl_number]=assign_heuristic(temp_board,bl_number,me)
			    savee2=bl_number
	                    blocks_all = determine_allowed_blocks(cell,temp_block)
	                    cell2  = get_empty_cells(temp_block,temp_board, blocks_all,0)
	                    if(cell2==[]):
				#print 'temp'
	                        if (temp_block.count(a)> temp_block.count(b)):
	                            heur=10000
				    maxe = max(temp_block.count(a),temp_block.count(b))
	                        elif(temp_block.count(b)> temp_block.count(a)):
	                            heur=-10000
				    minee = min(temp_block.count(a),temp_block.count(b))
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
			savee2=bl_number
			temp_block[bl_number]=save1
			savee3 = cell[0]
			savee4 = cell[1]
	                temp_board[savee3][savee4]='-'
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
	array=[]
	array.append(5)	
	p_80=0
	p_20=0
	array.append(7)
	lose=0
	p_0=0
	array.append(1.1)
	n_0=0
	n_20=0
	array.append(1.6)
	n_80=0
	win=0
	array.append(14)
	temp = heuristic[i] + heuristic[j] + heuristic[k] + heuristic[l]
	array.append(2.2)	
	a=[i,j,k,l]
	array.append(2.2)
	b=[]
	array.append(1)
	for q in a:
	    b.append(heuristic[q])
	array.append(4.5)
	pos=0
	for i in b:
	#if(i>=0):
	#pos+=1
	    if i ==-1:
	        lose+=1
	    elif i==1:
	        win+=1
		array.append(3)
	    elif i > 0.15:
	        p_80+=1
		array.append(2)
	    elif i >= 0.08:
		array.append(2)
	        p_20+=1
	    elif i > 0:
		array.append(2)
	        p_0 += 1
	    elif i < -0.15:
		array.append(3)
	        n_80 += 1
	    elif i <= -0.08:
		array.append(1)
	        n_20 += 1
	    elif i< 0:
	        n_0 += 1
	if(p_80==3 and n_20==1):
	    array.append(13)
	    temp=temp*0.8
	if(p_80==3 and n_80==1):
            array.append(1.3)
	    temp=temp*0.9
	if(p_80==3 and lose==1):
	    array.append(2.3)
	    temp=temp*0.5
	if(p_20==3 and n_80==1):
		array.append(2.6)
	        temp=temp*0.9
	if(p_20==3 and lose==1):
	    array.append(2.6)
	    temp=temp*0.3


	if(win==3 and n_80==1):
		array.append(2.7)	    
		temp=temp*0.3
	if(win==3 and lose==1):
	    array.append(2.7)
	    temp=0

	if(n_80==3 and p_80==1):
	    array.append(2.2)
	    temp=temp*1
	if(n_80==3 and win==1):
		array.append(2.3)	    
		temp=temp*0.4

	if(n_20==3 and p_80==1):
		array.append(2.8)
	        temp=temp*0.8
	if(n_20==3 and win==1):
	    temp=temp*0.6

	if(lose==3 and win==1):
	    temp=0
	if(lose==3 and p_80==1):
	    temp=temp*0.3


	if(win==1 and p_0==3):
	    array.append(2.3)
	    temp=temp*0.4
	elif (p_80==1 and p_0==3):
	    temp=temp*0.7
	    array.append(5.4)
    #    elif(p_80==1 and p_20==2):


	if(lose==1 and n_0==3):
		array.append(2.7)	    
		temp=temp*0.4
	elif (n_80==1 and n_0==3):
	    array.append(1.6)
	    temp=temp*0.7

	if(flag==1):
	    array.append(2.6)
	    temp=-temp
	if temp < 0.32:
	    array.append(4.3)
	    h += temp
	elif temp >= 0.32 and temp <= 0.79:
	    h += ( (temp -0.24) *12) + 1
	elif temp >= 0.79 and temp <4:
	    h = (temp-0.79)*90 + 10
	    array.append(3.2)
	elif temp>=4:
	    h +=1000
	    array.append(3.1)
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

	array2=[]
	for i in range(row,row+4):
		countr = 0
		countc = 0
		for j in range(column,column+4):

	                if temp_board[i][j] == player:
				array2.append(j)                  #for row
				countr += 1
				array2.append(i)

	                if temp_board[i][j] == opponent:
				array2.append(i)				
				countr = -10
				array2.append(j)
	                if temp_board[j-column+row][i-row+column] == player:                  # for column
				array2.append(i)				
				countc += 1
				array2.append(j)


	                if temp_board[j-column+row][i-row+column] == opponent:
				array2.append(i)	
				countc = -10
				array2.append(j)
	        if countr == 1:
			array2.append(i)
			heuristic_value += 1
			array2.append(j)
		elif countr == 2:
			array2.append(i)
			heuristic_value += 10
			array2.append(j)
		elif countr == 3:
			array2.append(i)
			heuristic_value += 80
			array2.append(j)
		elif countr==4:
			array2.append(i)
			heuristic_value+=500
			array2.append(j)
	        if countc == 1:
			array2.append(i)
			heuristic_value += 1
			array2.append(j)
		elif countc == 2:
			array2.append(i)
			heuristic_value += 10
			array2.append(j)
		elif countc == 3:
			array2.append(i)
			heuristic_value += 80
			array2.append(j)
		elif countc==4:
			array2.append(i)
			heuristic_value+=500
			array2.append(j)
	count=0
	for i in range (4):                                             # first diagonal
		if temp_board[row+i][column+i] == player:
			array2.append(i)
			count += 1
			array2.append(j)
		if temp_board[row+i][column+i] == opponent:
			array2.append(i)
			count -= 10
			array2.append(j)
	fll=[]
	if count == 1:
		fll.append(count)
		heuristic_value += 1
	elif count == 2:
		fll.append(count)
		heuristic_value += 10
	elif count == 3:
		fll.append(count)
		heuristic_value += 80
	elif count == 4:
		fll.append(count)
		heuristic_value += 500



	count=0
	for i in range (4):                                             # second diagonal
		if temp_board[row+i][column+3-i] == player:
			count += 1
			fll.append(count)
		if temp_board[row+i][column+3-i] == opponent:
			fll.append(count)
			count -= 10


	if count == 1:
		fll.append(count)
		heuristic_value += 1
	elif count == 2:
		fll.append(count)
		heuristic_value += 10
	elif count == 3:
		fll.append(count)
		heuristic_value += 80
	elif count == 4:
		fll.append(count)
		heuristic_value += 500
	if heuristic_value > 500:
		fll.append(heuristic_value)
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
	array2=[]
	for idb in a_b:
		id1 = idb/4
		id2 = idb%4
		for i in range(id1*4,id1*4+4):
			for j in range(id2*4,id2*4+4):
				if game_board[i][j] == '-':
					empty_cells.append((i,j))
					array2.append(game_board[i][j])

	#    print "z"
	 #   print empty_cells

	# If all the possible blocks are full, you can move anywhere
	if empty_cells == [] and count==0:
	    new=[]
	    i=0	
	    
	    while(i<16): 	
	        if(block_stat[i]=='-'):
		    array2.append(block_stat[i])	
	            new.append(i)
		    array2.append(i)
		i=i+1

	    return get_empty_cells(block_stat,game_board,new,1)

	
	return empty_cells


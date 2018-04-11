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


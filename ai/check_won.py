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

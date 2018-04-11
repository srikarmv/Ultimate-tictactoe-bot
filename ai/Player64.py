import sys
import copy
import random
class Player64:
    def __init__(self):
        self.depth = 3
        self.count=0
        self.small_block_heuristic=[0 for i in range(16)];
        self.block_dict={};
        self.moves=0;
        self.inf = 10000000000;
        self.places = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15), (0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (0, 5 ,10, 15), (3, 6, 9, 12)]
        self.centre = [5, 6, 9, 10]
        self.corners = [0, 3, 12, 15]
        self.flag = ""
        self.smallblockscore = {
        "win":500,
        "three":80,
        "two":10,
        "one":1,
        "blockthree":0.1,
        "blocktwo":0.025,
        "blockone":0.04,
        "corners":0.005,
        "centre":1
        }
        self.totblockscore = {
        "win":10000,
        "three":250,
        "two":20,
        "one":2,
        "blockthree":10,
        "blocktwo":2.5,
        "blockone":4,
        "corners":0.5,
        "centre":100
        }
        self.storeblocksc = {
        'x': {},
        'o': {}
        }
        self.storeboardsc = {
        'x': {},
        'o': {}
        }
        self.symbols = ['x', 'o', '-']
        #self.store()

    def convert(self,block):
        return tuple(block)

    def store(self):
        for i in xrange(0, 3**16):
            #print i
            indblock = []
            var = i
            for x in xrange(0, 16):
                indblock.append(self.symbols[var % 3])
                var =var / 3

            temp_indblock=self.convert(indblock)
            # store scores for all possible positions
            self.storeblocksc['x'][temp_indblock] = self.blockheuristic(temp_indblock, 'x')
            self.storeblocksc['o'][temp_indblock] = -self.storeblocksc['x'][temp_indblock]
            self.storeboardsc['x'][temp_indblock] = self.boardheuristic(temp_indblock, 'x')
            self.storeboardsc['o'][temp_indblock] = -self.storeboardsc['x'][temp_indblock]

    def blockheuristic(self, node, curr_flag):
        '''tuple_node=tuple(node);
        if tuple_node in self.block_dict.keys():
            return self.block_dict[tuple_node];
        '''
        #print curr_flag
        utility = 0

        if curr_flag == 'x':
            ourflag = 1
            oppflag = 2
        else :
            ourflag = 1
            oppflag = 2
        #print self.centre;
        #print;
        #print node;
        for i in self.places:
            count_our = 0
            count_opp = 0
            for j in i:
                if node[j] == 1:
                    count_our=count_our+1
                elif node[j] == 2:
                    count_opp=count_opp+1
            if count_our == 4:
                utility = self.smallblockscore["win"];
                break;
                

            elif count_opp == 4:
                utility = self.smallblockscore["win"]
                break;
            elif count_our == 3 and count_opp == 0:
                utility += self.smallblockscore["three"]
                #print 3,0

            elif count_our == 0 and count_opp == 3:
                utility -= self.smallblockscore["three"]
            
            elif count_our == 2 and count_opp == 0:
                utility += self.smallblockscore["two"]
                #print 2,0

            elif count_our == 0 and count_opp == 2:
                utility -= self.smallblockscore["two"]
                #print 0,2
            
            elif count_our == 1 and count_opp == 0:
                utility += self.smallblockscore["one"]
                #print 2,0

            elif count_our == 0 and count_opp == 1:
                utility -= self.smallblockscore["one"]
                #print 0,2
        if utility>500:
            utility=500;
        utility=(utility*1.0)/500;

        #self.block_dict[tuple_node]=utility;
        return utility

    def find_value(self,some_list):
        our_score=0;
        for i in some_list:
            our_score=our_score+self.small_block_heuristic[i];
        return our_score;

    def boardheuristic(self, node, curr_flag):

        utility = 0;
        temp=0;
        for i in self.places:
            temp+=self.find_value(i);
            if temp>=0 and temp<=1:
                utility+=temp;
            elif temp>1 and temp<=2:
                utility+=1+(10-1)*(temp-1);
            elif temp>2 and temp<=3:
                utility+=10+(100-90)*(temp-2);
            elif temp>3 and temp<4 :
                utility+=80+(1000-900)*(temp-3);
            elif temp==4 :
                utility=500;
                break;
            elif temp<0 and temp>=-1 :
                utility-=temp;
            elif temp<-1 and temp>=-2:
                utility-=1+(10-1)*(temp+1);
            elif temp<-2 and temp>=-3:
                utility-=10+(100-90)*(temp+2);
            elif temp<-3 and temp>-4 :
                utility-=80+(1000-900)*(temp+3);
            elif temp==-4 :
                utility=-500;
                break;
            if utility>500:
                utility=500;
            utility=(utility*1.0)/500;

        return utility

    ## returns best move possible to the player
    def move(self, board, old_move, flag):

        self.flag = flag
        self.count=0
        curr_board = [[0 for i in range(16)]for j in range(16)]
        curr_block_status = [[0 for i in range(4)]for j in range(4)]
        # empty: 0, ourmove: 1, opponentmove: 2
        for i in range(16):
            for j in range(16):
                if board.board_status[i][j] == flag:
                    curr_board[i][j] = 1;
                elif board.board_status[i][j] == '-':
                    curr_board[i][j] = 0;
                else :
                    curr_board[i][j] = 2;

        for i in range(4):
            for j in range(4):
                if board.block_status[i][j] == flag:
                    curr_block_status[i][j] = 1;
                elif board.block_status[i][j] == '-':
                    curr_block_status[i][j] = 0;
                elif board.block_status[i][j] == 'd':
                    curr_block_status[i][j] = 3;
                else :
                    curr_block_status[i][j] = 2;

        ##ReDEFINE
        if self.moves ==100:
           self.depth=4;
        #elif self.moves == 50:
        #    self.depth=5;
        path_score=0;
        if old_move[0] == -1 or old_move[1] == -1:
            path_score, next_move = 0, (5, 5);
        else :
            path_score, next_move = self.minimax(curr_board, curr_block_status, -self.inf, self.inf, True, old_move, self.depth);
        self.moves+=1;
        return next_move;

    #finds the valid cells in which next move is to be moved
    def get_valid_cells(self, curr_board, curr_block_status, old_move):
     #returns the valid cells allowed given the last move and the current board state
        allowed_cells = []
        allowed_block = [old_move[0] % 4, old_move[1] % 4]# checksif the move is a free move or not based on the rules

        if old_move != (-1, -1) and curr_block_status[allowed_block[0]][allowed_block[1]] == 0:
            for i in range(4 * allowed_block[0], 4 * allowed_block[0] + 4):
                for j in range(4 * allowed_block[1], 4 * allowed_block[1] + 4):
                    if curr_board[i][j] == 0:
                        allowed_cells.append((i, j))
        else :
            for i in range(16):
                for j in range(16):
                    if curr_board[i][j] == 0 and curr_block_status[i / 4][j / 4] == 0:
                        allowed_cells.append((i, j))
        return allowed_cells

    ## gives the value of a 4 * 4 block
    def get_updated_block_status(self, curr_block, cell):
        x = cell[0] / 4;
        y = cell[1] / 4;
        x = 4 * x;
        y = 4 * y;
        #  diagonals1
        if curr_block[x + 0][y + 0] == curr_block[x + 1][y+1] == curr_block[x + 2][y + 2] == curr_block[x + 3][y + 3] and(curr_block[x + 0][y + 0] == 1 or curr_block[x + 0][y + 0] == 2):
            return curr_block[x + 0][y + 0];
        ##    diagonal2
        if curr_block[x + 0][y + 3] == curr_block[x + 1][y + 2] == curr_block[x + 2][y + 1] == curr_block[x + 3][y + 0] and(curr_block[x + 0][y + 3] == 1 or curr_block[x + 0][y + 3] == 2):
            return curr_block[x + 0][y + 3];

        #check rows
        for i in range(4):
            if curr_block[x + i][y + 0] == curr_block[x + i][y + 1] == curr_block[x + i][y + 2] == curr_block[x + i][y + 3] and(curr_block[x + i][y + 0] == 1 or curr_block[x + i][y + 0] == 2):
                return curr_block[x + i][y + 0];

        #check columns
        for i in range(4):
            if curr_block[x + 0][y + i] == curr_block[x + 1][y + i] == curr_block[x + 2][y + i] == curr_block[x + 3][y + i] and(curr_block[x + 0][y + i] == 1 or curr_block[x + 0][y + i] == 2):
                return curr_block[x + 0][y + i];

        ##draw check
        flag = 0;
        for i in range(4):
            for j in range(4):
                if curr_block[i][j] != 0:
                    flag = flag + 1;
        if (flag == 16):
            return 3;

        #empty block
        return 0;

    ###NEED TO COMPLETE## heuristic
    def get_utility(self, curr_board, curr_block_status,count):
        count=count+1
        utility = 0
        for i in xrange(0, 16):
            row = (i / 4) * 4
            col = (i % 4) * 4
            boardtemp = []
            for j in xrange(row, row + 4):
                for k in xrange(col, col + 4):
                    boardtemp.append(curr_board[j][k])

            #utility += self.storeblocksc[self.flag][self.convert(boardtemp)]
            temp=self.blockheuristic(boardtemp,self.flag);
            self.small_block_heuristic[i]=temp;
            utility+=temp;

        utilityblock_status = copy.deepcopy(curr_block_status)

        for i in range(0, 4):
            for j in range(0,4):
                if utilityblock_status[i][j] == 3 :
                    utilityblock_status[i][j] = 'd';
                elif utilityblock_status[i][j] == 0:
                    utilityblock_status[i][j] = '-';
                elif utilityblock_status[i][j] == 1:
                    utilityblock_status[i][j] = self.flag
                else:
                    if self.flag == 'x':
                        utilityblock_status[i][j] = 'o'
                    else :
                        utilityblock_status[i][j] = 'x'
        #block_stat_temp=[];
        #for i in range(0,4):
        #   for j in range(0,4):
        #        block_stat_temp.append(utilityblock_status[i][j]);
            #utility += self.storeboardsc[self.flag][self.convert(utilityblock_status)]
        utility+=self.boardheuristic(utilityblock_status,self.flag)
        #if count<10:
        #    print utility
        return utility

    ## checks whether game finished or not
    def final_check(self, curr_board, curr_block_status):
        game_ended = self.get_updated_block_status(curr_block_status, (0, 0));

        ###
        #1->we won the game
                # 2 - > opp won the game
        #3->game draw
                # 0 - > still game is progress
        if game_ended == 1:
            return 1, 500;
        elif game_ended == 2:
            return 1, -500;
        elif game_ended == 0:
            return 0, 0;
        elif game_ended == 3: ###!!!NEEDED TO COMPLETE
            temp1=0;
            temp2=0;
            for i in range(4):
                for j in range(4):
                    if curr_block_status[i][j]==1 :
                        temp1=temp1+1;
                    elif curr_block_status[i][j]==2:
                        temp1=temp1-1;

            if temp1 > 0:
                return 1,500;
            elif temp1 < 0:
                return 1,-500;
            temp2=0;
            for i in range(0,16,4):
                for j in range(0,16,4):
                    for z in range(1,3,1):
                        for k in range(1,3,1):
                            if curr_board[i+z][j+k] ==1:
                                temp2=temp2+1;
                            elif curr_board[i+z][j+k]==2:
                                temp2=temp2-1;

            if temp2 > 0:
                return 1,500;
            elif temp2 < 0:
                return 1,-500;
            else:
                return 1,0;

    ## Alpha - Beta pruning till depth.
    def minimax(self, curr_board, curr_block_status, alpha, beta, flag, old_move, depth):

        ##last_move
        game_ended, final_score = self.final_check(curr_board, curr_block_status);
        if game_ended:
            return final_score, ();

        ## base_case
        if depth <= 0:
            #return 1,();
            return self.get_utility(curr_board, curr_block_status,self.count), ()

        valid_cells = self.get_valid_cells(curr_board, curr_block_status, old_move);
        #print old_move;
        #print valid_cells;
        random.shuffle(valid_cells);

        temp_board = copy.deepcopy(curr_board);
        temp_block_status = copy.deepcopy(curr_block_status);
        best_cell=();
        ##our turn
        if (flag):
            best = -self.inf;
            for cell in valid_cells:
                 ##make_a_move
                temp_board[cell[0]][cell[1]] = 1;
                temp_block_status[cell[0] / 4][cell[1] / 4] = self.get_updated_block_status(temp_board, cell);
                opp = not flag;
                fake_score, fake_best = self.minimax(temp_board, temp_block_status, alpha, beta, opp, cell, depth - 1);
                if fake_score >= best:
                    best = fake_score;
                    best_cell = cell;

                ## changes overwritten
                temp_board[cell[0]][cell[1]] = 0;
                temp_block_status[cell[0] / 4][cell[1] / 4] = self.get_updated_block_status(temp_board, cell);

                alpha =max(alpha,best);

                if alpha >= beta:
                    break;

            return best, best_cell;

        else :
            best = self.inf;
            for cell in valid_cells:
                 ##make_a_move
                temp_board[cell[0]][cell[1]] = 2;
                temp_block_status[cell[0] / 4][cell[1] / 4] = self.get_updated_block_status(temp_board, cell);
                opp = not flag;
                fake_score, fake_best = self.minimax(temp_board, temp_block_status, alpha, beta, opp, cell, depth - 1);
                if fake_score <= best:
                    best = fake_score;
                    best_cell = cell;

                #changes overwritten
                temp_board[cell[0]][cell[1]] = 0;
                temp_block_status[cell[0] / 4][cell[1] / 4] = self.get_updated_block_status(temp_board, cell);

                beta=min(beta,best);

                if alpha >= beta:
                    break;

            return best, best_cell;

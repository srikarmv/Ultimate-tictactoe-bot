import random
import sys
import copy
import time


#check def get_allowed_blocks(self, block, old_move): function.

class Player18:
    """
    Class to Deal with the agent in game
    """

    def __init__(self):
        """ Default Constructor  """
        self.originaldepth=5
        self.max_ply=5
        self.ply = 5
        self.num = 0
        self.cntp = 0
        self.cnto = 0
        self.board_status = [['-' for i in range(16)] for j in range(16)]
        self.block_status =  [['-' for i in range(4)] for j in range(4)]

        pass

    def get_free_cells(self, board, blocks_allowed, block_status):
        """

        :param board:  board input
        :param blocks_allowed: list containing numbers of blocks which are allowed
        :return: list of cells which are available for a move
        """

        cells = []
        for block in blocks_allowed:
            startx = block / 4
            starty = block % 4
            for i in range(startx * 4, startx * 4 + 4):
                for j in range(starty * 4, starty * 4 + 4):

                    if board[i][j] == '-':
                        cells.append((i, j))
        if len(cells) == 0:

            new_blocks_allowed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            for block in new_blocks_allowed:
                startx = block / 4
                starty = block % 4
                for i in range(startx * 4, startx * 4 + 4):
                    for j in range(starty * 4, starty * 4 + 4):
                        if board[i][j] == '-' and block_status[block] == '-':
                            cells.append((i, j))
        return cells

    def free_move(self, block):
    	""" Function that deals with the case of a free move """	
        blocks_allowed = []
        for i in range(16):
            if block[i] == '-':
                blocks_allowed.append(i);
        return blocks_allowed

    def get_allowed_blocks(self, block, old_move):
        """

        :param block: list containg status of each block
        :param old_move: previous move
        :return: list of block numbres which are allowed
        """
        blocks_allowed = []
        if old_move == (-1, -1):
            blocks_allowed = self.free_move(block)
        else:
            if block[(old_move[0] % 4)*4 + old_move[1] % 4] == '-':
                blocks_allowed.append((old_move[0] % 4)*4 + old_move[1] % 4)
            else:
                blocks_allowed = self.free_move(block)

        return blocks_allowed

    def get_allowed_moves(self, board, block, old_move):
    	""" Function that gets the allowed moves in a particular state of game
    	:param board:  board input
    	:param block:  list containg status of each block
        :param old_move: previous move
        :return: list of block numbers which are allowed"""
        blocks_allowed = self.get_allowed_blocks(block, old_move)
        return self.get_free_cells(board, blocks_allowed, block)

    def update_block(self, local_board, block_current, block_no, fl):
        local_block = copy.deepcopy(block_current)
        id1 = block_no / 4
        id2 = block_no % 4
        mflg = 0

        flag = 0
        for i in range(id1 * 4, id1 * 4 + 4):
            for j in range(id2 * 4, id2 * 4 + 4):
                if local_board[i][j] == '-':
                    flag = 1

        if local_block[block_no] == '-':

            if local_board[id1 * 4 ][id2 * 4 ] == local_board[id1 * 4 + 1][id2 * 4 + 1] \
            and local_board[id1 * 4 + 1][id2 * 4 + 1] == local_board[id1 * 4 + 2][id2 * 4 + 2] \
            and  local_board[id1 * 4 + 2][id2 * 4 + 2] == local_board[id1 * 4 + 3][id2 * 4 + 3] \
            and local_board[id1 * 4 ][ id2 * 4 ] != '-' \
            and local_board[id1 * 4 + 1 ][id2 * 4 ] != 'D':
                    mflg = 1

            if local_board[id1 * 4 + 3][id2 * 4] == local_board[id1 * 4 + 2][id2 * 4 + 1] \
            and local_board[id1 * 4 + 2][id2 * 4 + 1] == local_board[id1 * 4+1][id2 * 4 + 2] \
            and local_board[id1 * 4 + 1][id2 * 4 + 2] == local_board[id1 * 4][id2 * 4 + 3] \
            and local_board[id1 * 4 + 3][id2 * 4] != '-' \
            and local_board[id1 * 4 + 3][id2 * 4] != 'D':
                mflg = 1
            if mflg != 1:
                for i in range(id2 * 4, id2 * 4 + 4):
                    if local_board[id1 * 4][i] == local_board[id1 * 4 + 1][i] \
                        and local_board[id1 * 4 + 1][i] == local_board[id1 * 4 + 2][i] \
                        and local_board[id1 * 4 + 2][i] == local_board[id1 * 4 + 3][i] \
                        and local_board[id1 * 4][i] != '-'  \
                        and local_board[id1 * 4][i] != 'D':
                        mflg = 1
                        break
            if mflg != 1:
                for i in range(id1 * 4, id1 * 4 + 4):
                    if local_board[i][id2 * 4] == local_board[i][id2 * 4 + 1] \
                        and local_board[i][id2 * 4 + 1] == local_board[i][id2 * 4 + 2] \
                        and local_board[i][id2 * 4 + 2] == local_board[i][id2 * 4 + 3]  \
                        and local_board[i][id2 * 4] != '-'  \
                        and local_board[i][id2 * 4] != 'D':
                        mflg = 1
                        break
        if flag == 0:
            local_block[block_no] = 'D'
        if mflg == 1:
            local_block[block_no] = fl
        return local_block


    def minimax(self, board, block, old_move, maxnode, player_flag, flag2, depth, alpha, beta, best_row, best_col):
        """
		Applies the minimax algorithm on the state of game
        :param board: board
        :param block: status of blocks
        :param old_move: previous move
        :param maxnode: flag that tells whether it is maxnode or not
        :param player_flag: players flag (x or o)
        :param flag2: opponents flag
        :param depth: depth in tree
        :param alpha: alpha value
        :param beta: beta value
        :param best_row: present best move x-cordinate
        :param best_col: present best move y-cordinate
        :return: three tuple consisting of utlity of block and best moves cordinates
        """

        if depth == self.ply:
            utility = self.get_utility(board, block, player_flag, flag2,depth)


            return (utility, best_row, best_col)
        else:
            moves = self.get_allowed_moves(board, block, old_move)
            #print moves
            #if depth==0:
                #print block

            if len(moves) == 0:
                utility = self.get_utility(board, block, player_flag, flag2,depth)
                utility = round(utility,4)
                self.ply = max(depth, self.originaldepth)
                return (utility, old_move[0], old_move[1])
            if len(moves) > 16:
                depth = max(depth, 3+self.max_ply-self.originaldepth)
            for move in moves:
                # self.isp = 0
                if maxnode:
                    board[move[0]][move[1]] = player_flag
                else:
                    board[move[0]][move[1]] = flag2
                block_no = (move[0] / 4) * 4 + move[1] / 4
                fl = flag2
                if maxnode: fl = player_flag
                temp_block = self.update_block(board, block, block_no, fl)
                if maxnode:

                    util = self.minimax(board, temp_block, move, False, player_flag, flag2, depth + 1, alpha, beta,
                                        best_row,
                                        best_col)
                    utility = round(util[0], 4)
                    if utility > alpha:
                        alpha = utility
                        best_row = move[0]
                        best_col = move[1]
                else:
                    util = self.minimax(board, temp_block, move, True, player_flag, flag2, depth + 1, alpha, beta,
                                        best_row,
                                        best_col)

                    utility = round(util[0], 4)
                    if utility < beta:
                        beta = utility
                        best_row = move[0]
                        best_col = move[1]
                board[move[0]][move[1]] = '-'
                if alpha >= beta:
                    break

            if depth == 0:
                if best_row == -1 or best_col == -1:
                    best_row = moves[0][0]
                    best_col = moves[0][1]
            #print best_col,best_row,"no"
            if maxnode:
                return (alpha, best_row, best_col, len(moves))
            else:
                return (beta, best_row, best_col, len(moves))
    def update(self, new_move, ply):
        # updating the game board and block status as per the move that has been passed in the arguements
        self.board_status[new_move[0]][new_move[1]] = ply

        x = new_move[0] / 4
        y = new_move[1] / 4
        fl = 0
        bs = self.board_status
        # checking if a block has been won or drawn or not after the current move
        for i in range(4):
            # checking for horizontal pattern(i'th row)
            if (bs[4 * x + i][4 * y] == bs[4 * x + i][4 * y + 1] == bs[4 * x + i][4 * y + 2] == bs[4 * x + i][
                        4 * y + 3]) and (bs[4 * x + i][4 * y] == ply):
                self.block_status[x][y] = ply
                return 'SUCCESSFUL'
            # checking for vertical pattern(i'th column)
            if (bs[4 * x][4 * y + i] == bs[4 * x + 1][4 * y + i] == bs[4 * x + 2][4 * y + i] == bs[4 * x + 3][
                        4 * y + i]) and (bs[4 * x][4 * y + i] == ply):
                self.block_status[x][y] = ply
                return 'SUCCESSFUL'

        # checking for diagnol pattern
        if (bs[4 * x][4 * y] == bs[4 * x + 1][4 * y + 1] == bs[4 * x + 2][4 * y + 2] == bs[4 * x + 3][4 * y + 3]) and (
            bs[4 * x][4 * y] == ply):
            self.block_status[x][y] = ply
            return 'SUCCESSFUL'
        if (bs[4 * x + 3][4 * y] == bs[4 * x + 2][4 * y + 1] == bs[4 * x + 1][4 * y + 2] == bs[4 * x][4 * y + 3]) and (
            bs[4 * x + 3][4 * y] == ply):
            self.block_status[x][y] = ply
            return 'SUCCESSFUL'

        # checking if a block has any more cells left or has it been drawn
        for i in range(4):
            for j in range(4):
                if bs[4 * x + i][4 * y + j] == '-':
                    return 'SUCCESSFUL'
        self.block_status[x][y] = 'd'
        return 'SUCCESSFUL'

    def move(self, board, old_move, player_flag):
        """
        :param board: is the list of lists that represents the 9x9 grid
        :param block: is a list that represents if a block is won or available to play in
        :param old_move: is a tuple of integers representing co-ordintates of the last move made
        :param flag: is player marker. it can be 'x' or 'o'.
        board[i] can be 'x' or 'o'. block[i] can be 'x' or 'o'
        Chooses a move based on minimax and alphabeta-pruning algorithm and returns it
        :rtype tuple: the co-ordinates in 9X9 board
        """
        self.ply=self.originaldepth
        self.board_status=copy.deepcopy(board.board_status)

        block_no = (old_move[0] / 4) * 4 + old_move[1] / 4

        if player_flag == 'o':
            flag2 = 'x'
        else:
            flag2 = 'o'

        fl = flag2
        self.update(old_move,  fl)

        block= [self.block_status[block_no/4][block_no%4] for block_no in range(16)]
        self.isp = 0
        if old_move == (-1, -1):
            return (5, 5)
        startt = time.clock()
        if player_flag == 'o':
            flag2 = 'x'
        else:
            flag2 = 'o'
        self.num += 1
        #print num
        max_ply = self.max_ply
        self.cntp = block.count(player_flag)
        self.cnto = block.count(flag2)
        if  self.num > 50:
            self.ply = max_ply
        temp_board = copy.deepcopy(board.board_status)
        temp_block = copy.deepcopy(block)

        next_move = self.minimax(temp_board, temp_block, old_move, True, player_flag, flag2, 0, -100000.0, 100000.0, -1,
                                 -1)
        elapsed = (time.clock() - startt)

        block_no = (next_move[1] / 4) * 4 + next_move[2] / 4
        self.board_status[next_move[1]][next_move[2]]=player_flag
        #self.block_status = self.update_block(temp_board, self.block_status, block_no, player_flag)
        self.update((next_move[1], next_move[2]), player_flag)
        print self.num
        print (next_move[1], next_move[2],"yes")
        return (next_move[1], next_move[2])


    def heuristic(self, board, blockx,blocky, player):
        x_start = blockx*4
        y_start = blocky*4
        heuristic_value = 0
        # for i in range(3):
        # 	for j in range(3):
        # 		board[x_start+i][y_start+j]=raw_input()

        # for i in range(3):
        # 	for j in range(3):

        # horizontal check
        for i in range(4):
            x = x_start + i
            y = y_start
            count_of_empty_cells = 0
            for j in range(4):
                y = y_start + j
                if board[x][y] == '-':
                    count_of_empty_cells += 1
            x = x_start + i
            y = y_start
            if count_of_empty_cells == 0:
                if board[x][y] == player and (
                        board[x][y] == board[x][y + 1] and board[x][y + 2] == board[x][y + 1] and board[x][y + 2] == board[x][y + 3]):
                    return 1000
                elif board[x][y] != player and (
                        board[x][y] == board[x][y + 1] and board[x][y + 2] == board[x][y + 1] and board[x][y + 2] == board[x][y + 3]):
                    return -1000
            elif count_of_empty_cells == 1:
                if (board[x][y] == board[x][y + 1] and board[x][y+2] == board[x][y + 1] and board[x][y] == player) or (
                        board[x][y + 1] == board[x][y + 2] and board[x][y+3] == board[x][y + 1] and board[x][y + 1] == player) or (
                        board[x][y+2] == board[x][y + 3] and board[x][y+2] == board[x][y] and board[x][y] == player) or (
                        board[x][y+3] == board[x][y + 1] and board[x][y+1] == board[x][y] and board[x][y] == player):
                    heuristic_value += 100
                elif (board[x][y] == board[x][y + 1] and board[x][y+2] == board[x][y + 1] and board[x][y] != player) or (
                        board[x][y + 1] == board[x][y + 2] and board[x][y+3] == board[x][y + 1] and board[x][y + 1] != player) or (
                        board[x][y+2] == board[x][y + 3] and board[x][y+2] == board[x][y] and board[x][y] != player) or (
                        board[x][y+3] == board[x][y + 1] and board[x][y+1] == board[x][y] and board[x][y] != player):
                    heuristic_value -= 100


            elif count_of_empty_cells == 2:
                if ((board[x][y] == board[x][y + 1]  and board[x][y]==player) or
                        (board[x][y] == board[x][y + 2] and board[x][y] == player) or
                        (board[x][y] == board[x][y + 3] and board[x][y] == player) or
                        (board[x][y+2] == board[x][y + 1] and board[x][y + 1] == player) or
                        (board[x][y+3] == board[x][y + 1] and board[x][y + 1] == player) or
                        (board[x][y+2] == board[x][y + 3] and board[x][y + 2] == player)):
                    heuristic_value += 10
                if ((board[x][y] == board[x][y + 1]  and board[x][y]!=player) or
                        (board[x][y] == board[x][y + 2] and board[x][y] != player) or
                        (board[x][y] == board[x][y + 3] and board[x][y] != player) or
                        (board[x][y+2] == board[x][y + 1] and board[x][y + 1] != player) or
                        (board[x][y+3] == board[x][y + 1] and board[x][y + 1] != player) or
                        (board[x][y+2] == board[x][y + 3] and board[x][y + 2] != player)):
                    heuristic_value -= 10
            elif count_of_empty_cells ==3:
                if board[x][y] == player or board[x][y + 1] == player or board[x][y + 2] == player or board[x][y + 3] == player:
                    heuristic_value += 1
                else:
                    heuristic_value -= 1
        # vertical check
        for i in range(4):
            x = x_start
            y = y_start + i
            count_of_empty_cells = 0
            for j in range(4):
                x = x_start + j
                if board[x][y] == '-':
                    count_of_empty_cells += 1
            x = x_start
            y = y_start + i
            if count_of_empty_cells == 0:
                if board[x][y] == player and (
                        board[x][y] == board[x + 1][y] and board[x + 2][y] == board[x + 1][y] and board[x + 2][y] == board[x + 3][y]):
                    return 1000
                elif board[x][y] != player and (
                        board[x][y] == board[x+1][y] and board[x +2][y ] == board[x+1 ][y ] and board[x+ 2][y ] == board[x + 3][y]):
                    return -1000
            elif count_of_empty_cells == 1:
                if (board[x][y] == board[x +1][y] and board[x +2][y] == board[x +1][y ] and board[x][y] == player) or (
                        board[x +1][y ] == board[x+2][y] and board[x+3][y] == board[x+1][y] and board[x+1][y] == player) or (
                        board[x+2][y] == board[x+3][y] and board[x+2][y] == board[x][y] and board[x][y] == player) or (
                        board[x+3][y] == board[x+1][y] and board[x+1][y] == board[x][y] and board[x][y] == player):
                    heuristic_value += 100
                elif (board[x][y] == board[x+1][y] and board[x+2][y] == board[x+1][y] and board[x][y] != player) or (
                        board[x+1][y ] == board[x+2][y] and board[x+3][y] == board[x+1][y] and board[x+1][y ] != player) or (
                        board[x+2][y] == board[x+3][y ] and board[x+2][y] == board[x][y] and board[x][y] != player) or (
                        board[x+3][y] == board[x+1][y ] and board[x+1][y] == board[x][y] and board[x][y] != player):
                    heuristic_value -= 100
                    #print heuristic_value,x,y
                    #print board[x][y],board[x+1][y],board[x+2][y],board[x+3][y]


            elif count_of_empty_cells == 2:
                if ((board[x][y] == board[x+1][y ]  and board[x+1][y ]==player) or
                        (board[x][y] == board[x+2][y] and board[x+2][y] == player) or
                        (board[x][y] == board[x+3][y ] and board[x+3][y ] == player) or
                        (board[x+2][y] == board[x+1][y ] and board[x+1][y ] == player) or
                        (board[x+3][y] == board[x+1][y ] and board[x+1][y] == player) or
                        (board[x+2][y] == board[x+3][y] and board[x+3][y] == player)):
                    heuristic_value += 10
                if ((board[x][y] == board[x+1][y ]  and board[x+1][y]!=player) or
                        (board[x][y] == board[x+2][y] and board[x+2][y] != player) or
                        (board[x][y] == board[x+3][y] and board[x+3][y] != player) or
                        (board[x+2][y] == board[x+1][y] and board[x+1][y] != player) or
                        (board[x+3][y] == board[x+1][y ] and board[x+1][y] != player) or
                        (board[x+2][y] == board[x+3][y ] and board[x+3][y ] != player)):
                    heuristic_value -= 10
            elif count_of_empty_cells == 3:
                if board[x][y] == player or board[x+1][y] == player or board[x+2][y] == player or board[x+3][y] == player:
                    heuristic_value += 1
                else:
                    heuristic_value -= 1
        # diagonal check 1
        flag = 0
        count_of_empty_cells = 0
        x = x_start
        y = y_start
        if board[x_start][y_start] == '-':
            count_of_empty_cells += 1
        if board[x_start + 1][y_start + 1] == '-':
            count_of_empty_cells += 1
        if board[x_start + 2][y_start + 2] == '-':
            count_of_empty_cells += 1
        if board[x_start + 3][y_start + 3] == '-':
            count_of_empty_cells += 1

        if count_of_empty_cells == 0:
            if board[x_start][y_start] == player and (
                    board[x][y] == board[x + 1][y + 1] and board[x + 2][y + 2] == board[x + 1][y + 1] and board[x + 3][y + 3] == board[x + 1][y + 1]):
                return 1000
            elif board[x_start][y_start] != player and (
                    board[x][y] == board[x + 1][y + 1] and board[x + 2][y + 2] == board[x + 1][y + 1] and board[x + 3][y + 3] == board[x + 1][y + 1]):
                return -1000
        elif count_of_empty_cells == 1:
            if (board[x][y] == board[x + 1][y + 1] and board[x][y] == board[x + 2][y + 2] and board[x][y] == player) or (
                            board[x + 1][y + 1] == board[x + 2][y + 2] and board[x+3][y +3] == board[x + 1][y + 1] and board[x + 1][y + 1] == player) or (
                            board[x][y] == board[x + 2][y + 2] and board[x][y] == board[x + 3][y + 3] and board[x][y] == player) or (
                            board[x][y] == board[x + 1][y + 1] and board[x][y] == board[x + 3][y + 3] and board[x][y] == player):
                heuristic_value += 100
            elif (board[x][y] == board[x + 1][y + 1] and board[x][y] == board[x + 2][y + 2] and board[x][
                y] != player) or (
                                board[x + 1][y + 1] == board[x + 2][y + 2] and board[x + 3][y + 3] == board[x + 1][
                                y + 1] and board[x + 1][y + 1] != player) or (
                                board[x][y] == board[x + 2][y + 2] and board[x][y] == board[x + 3][y + 3] and
                            board[x][y] != player) or (
                                board[x][y] == board[x + 1][y + 1] and board[x][y] == board[x + 3][y + 3] and
                            board[x][y] != player):
                heuristic_value -= 100

        elif count_of_empty_cells == 2:
            if ((board[x][y] == board[x + 1][y + 1]  and board[x][y] == player) or
                (board[x][y] == board[x + 2][y + 2] and board[x][y] == player) or
                (board[x][y] == board[x + 3][y + 3] and board[x][y] == player) or
                (board[x+2][y+2] == board[x + 1][y + 1] and board[x+1][y+1] == player) or
                (board[x+3][y+3] == board[x + 1][y + 1] and board[x+1][y+1] == player) or
                (board[x+2][y+2] == board[x + 3][y + 3] and board[x+2][y+2] == player)):
                heuristic_value += 10
            if ((board[x][y] == board[x + 1][y + 1]  and board[x][y] != player) or
                (board[x][y] == board[x + 2][y + 2] and board[x][y] != player) or
                (board[x][y] == board[x + 3][y + 3] and board[x][y] != player) or
                (board[x+2][y+2] == board[x + 1][y + 1] and board[x+1][y+1] != player) or
                (board[x+3][y+3] == board[x + 1][y + 1] and board[x+1][y+1] != player) or
                (board[x+2][y+2] == board[x + 3][y + 3] and board[x+2][y+2] != player)):
                heuristic_value -= 10

        elif count_of_empty_cells == 3:
            if board[x_start][y_start] == player or board[x_start + 1][y_start + 1] == player or \
                            board[x_start + 2][y_start + 2] == player or board[x_start + 3][y_start + 3] == player:
                heuristic_value += 1
            else:
                heuristic_value -= 1
            flag = 1

        # diagonal check 2
        count_of_empty_cells = 0
        x = x_start + 3
        y = y_start
        if board[x][y] == '-':
            count_of_empty_cells += 1
        if board[x - 1][y + 1] == '-':
            count_of_empty_cells += 1
        if board[x - 2][y + 2] == '-':
            count_of_empty_cells += 1
        if board[x-3][y + 3] == '-':
            count_of_empty_cells += 1

        if count_of_empty_cells == 0:
            if board[x][y] == player and (
                    board[x][y] == board[x - 1][y + 1] and board[x - 2][y + 2] == board[x - 1][y + 1] and board[x - 3][y + 3] == board[x - 1][y + 1]):
                return 1000
            elif board[x][y] != player and (
                    board[x][y] == board[x - 1][y + 1] and board[x - 2][y + 2] == board[x - 1][y + 1] and board[x - 3][y + 3] == board[x - 1][y + 1]):
                return -1000
        elif count_of_empty_cells == 1:
            if (board[x][y] == board[x - 1][y + 1] and board[x][y] == board[x - 2][y + 2] and board[x][y] == player) or (
                            board[x - 1][y + 1] == board[x - 2][y + 2] and board[x-3][y +3] == board[x - 1][y + 1] and board[x - 1][y + 1] == player) or (
                            board[x][y] == board[x - 2][y + 2] and board[x][y] == board[x - 3][y + 3] and board[x][y] == player) or (
                            board[x][y] == board[x - 1][y + 1] and board[x][y] == board[x - 3][y + 3] and board[x][y] == player):
                heuristic_value += 100
            elif (board[x][y] == board[x - 1][y + 1] and board[x][y] == board[x - 2][y + 2] and board[x][
                y] != player) or (
                                board[x - 1][y + 1] == board[x - 2][y + 2] and board[x - 3][y + 3] == board[x - 1][
                                y + 1] and board[x - 1][y + 1] != player) or (
                                board[x][y] == board[x - 2][y + 2] and board[x][y] == board[x - 3][y + 3] and
                            board[x][y] != player) or (
                                board[x][y] == board[x - 1][y + 1] and board[x][y] == board[x - 3][y + 3] and
                            board[x][y] != player):
                heuristic_value -= 100
                #print heuristic_value,x_start,y_start,count_of_empty_cells,x,y
                #print board[x][y], board[x - 1][y + 1], board[x - 2][y + 2], board[x - 3][y + 3]

        elif count_of_empty_cells == 2:
            if ((board[x][y] == board[x - 1][y + 1]  and board[x][y] == player) or
                (board[x][y] == board[x - 2][y + 2] and board[x][y] == player) or
                (board[x][y] == board[x - 3][y + 3] and board[x][y] == player) or
                (board[x-2][y+2] == board[x - 1][y + 1] and board[x-1][y+1] == player) or
                (board[x-3][y+3] == board[x - 1][y + 1] and board[x-1][y+1] == player) or
                (board[x-2][y+2] == board[x - 3][y + 3] and board[x-2][y+2] == player)):
                heuristic_value += 10
            if ((board[x][y] == board[x - 1][y + 1]  and board[x][y] != player) or
                (board[x][y] == board[x - 2][y + 2] and board[x][y] != player) or
                (board[x][y] == board[x - 3][y + 3] and board[x][y] != player) or
                (board[x-2][y+2] == board[x - 1][y + 1] and board[x-1][y+1] != player) or
                (board[x-3][y+3] == board[x - 1][y + 1] and board[x-1][y+1] != player) or
                (board[x-2][y+2] == board[x - 3][y + 3] and board[x-2][y+2] != player)):
                heuristic_value -= 10

        elif count_of_empty_cells == 3:
            if board[x][y] == player or board[x - 1][y + 1] == player or \
                            board[x - 2][y + 2] == player or board[x - 3][y + 3] == player:
                heuristic_value += 1
            else:
                heuristic_value -= 1
            flag = 1


        return heuristic_value

    def eval_board(self,blockvalues):
        overall_sum = 0
        # horizontal
        lsum = 0
        for i in range(4):
            rowsum = 0
            for j in range(4):
                rowsum += blockvalues[i][j]
            x = 1
            flag = 0
            #print rowsum,"rowsum"
            if rowsum < 0:
                flag = 1
                rowsum = -rowsum
            while rowsum > 0:
                if rowsum >= 1:
                    lsum += 1 * (x - (x / 10))
                else:
                    lsum += rowsum * (x - (x / 10))
                x *= 10
                rowsum -= 1
            if flag == 1:
                lsum = -lsum*2
            overall_sum += lsum
            #print lsum,"lsum"

        # vertical
        lsum = 0
        for i in range(4):
            colsum = 0
            for j in range(4):
                colsum += blockvalues[j][i]
            x = 1
            flag = 0
            if colsum < 0:
                flag = 1
                colsum = -colsum
            while colsum > 0:
                if colsum >= 1:
                    lsum += 1 * (x - (x / 10))
                else:
                    lsum += colsum * (x - (x / 10))
                x *= 10
                colsum -= 1
            if flag == 1:
                lsum = -lsum*2
            overall_sum += lsum

        # diagonal
        diasum = 0
        diasum += blockvalues[0][0]
        diasum += blockvalues[1][1]
        diasum += blockvalues[2][2]
        diasum += blockvalues[3][3]
        x = 1
        flag = 0
        if diasum < 0:
            flag = 1
            diasum = -diasum
        lsum = 0
        while diasum > 0:
            if diasum >= 1:
                lsum += 1 * (x - (x / 10))
            else:
                lsum += diasum * (x - (x / 10))
            x *= 10
            diasum -= 1
        if flag == 1:
            lsum = -lsum*2
        overall_sum += lsum

        diasum = 0
        diasum += blockvalues[3][0]
        diasum += blockvalues[2][1]
        diasum += blockvalues[1][2]
        diasum += blockvalues[0][3]
        x = 1
        flag = 0
        if diasum < 0:
            flag = 1
            diasum = -diasum
        lsum = 0
        while diasum > 0:
            if diasum >= 1:
                lsum += 1 * (x - (x / 10))
            else:
                lsum += diasum * (x - (x / 10))
            x *= 10
            diasum -= 1
        if flag == 1:
            lsum = -lsum*2
        overall_sum += lsum

        # for i in range(3):
        # 	for j in range(3):
        #print overall_sum
        return overall_sum

    def get_utility(self, board, block, playerFlag, opFlag,depth):
    	"""
    	Function to find and return utility of a block
    	:param board: is the list of lists that represents the 16x16 grid
        :param block: is a list that represents if a block is won or available to play in
        :param playerFlag: player marker
        :param opFlag: Opponent Marker
    	"""
        block_heuristic = [[0 for i in range(4)] for j in range(4)]
        cntp=0
        cnto=0
        if depth%2 == 0:
            for i in range(4):
                for j in range(4):
                    y=self.heuristic(board, i,j, playerFlag)
                    if y > 100:
                        y=y
                    if y == 1000:
                        cntp+=1
                    elif y == -1000:
                        cnto+=1
                    block_heuristic[i][j] = (y)/1000.0
        if depth%2==1:
            for i in range(4):
                for j in range(4):
                    y = self.heuristic(board, i, j, playerFlag)
                    if y > 100:
                        y = y
                    if y == 1000:
                        cntp += 1
                    elif y == -1000:
                        cnto += 1

                    block_heuristic[i][j] = (y) / 1000.0

        #print block_heuristic
        #print self.eval_board(block_heuristic)
        x=self.eval_board(block_heuristic)
        #print x
        #print block_heuristic
        #if cntp>1 or cnto >1:
            #print cnto,cntp

        if depth%2 == 0:
            if x>100:
                x=x
        if depth%2 == 1:
            if x>100:
                x=x
        if depth ==0:
            print block_heuristic
        return x


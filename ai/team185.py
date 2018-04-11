import random
import sys
import copy
import time




class Player18:


    def __init__(self):

        self.originaldepth=4
        self.ply = 4
        self.max_ply = 4
        self.num = 0
        self.cntp = 0
        self.cnto = 0
        self.board_status = [['-' for i in range(16)] for j in range(16)]
        self.block_status =  [['-' for i in range(4)] for j in range(4)]

        pass

    def get_free_cells(self, board, blocks_allowed, block_status):


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

        blocks_allowed = []
        for i in range(16):
            if block[i] == '-':
                blocks_allowed.append(i);
        return blocks_allowed

    def get_allowed_blocks(self, block, old_move):

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


        if depth == self.ply:
            utility = self.get_utility(board, block, player_flag, flag2,depth)


            return (utility, best_row, best_col)
        else:
            moves = self.get_allowed_moves(board, block, old_move)


            if len(moves) == 0:
                utility = self.get_utility(board, block, player_flag, flag2,depth)
                utility = round(utility,4)
                self.ply = max(depth, self.originaldepth)
                return (utility, old_move[0], old_move[1])
            if len(moves) > 16:
                depth = max(depth, self.ply-2)
            for move in moves:

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

            if maxnode:
                return (alpha, best_row, best_col, len(moves))
            else:
                return (beta, best_row, best_col, len(moves))


    def update(self, new_move, ply):

        self.board_status[new_move[0]][new_move[1]] = ply

        x = new_move[0] / 4
        y = new_move[1] / 4
        fl = 0
        bs = self.board_status

        for i in range(4):

            if (bs[4 * x + i][4 * y] == bs[4 * x + i][4 * y + 1] == bs[4 * x + i][4 * y + 2] == bs[4 * x + i][
                4 * y + 3]) and (bs[4 * x + i][4 * y] == ply):
                self.block_status[x][y] = ply
                return 'SUCCESSFUL'

            if (bs[4 * x][4 * y + i] == bs[4 * x + 1][4 * y + i] == bs[4 * x + 2][4 * y + i] == bs[4 * x + 3][
                4 * y + i]) and (bs[4 * x][4 * y + i] == ply):
                self.block_status[x][y] = ply
                return 'SUCCESSFUL'


        if (bs[4 * x][4 * y] == bs[4 * x + 1][4 * y + 1] == bs[4 * x + 2][4 * y + 2] == bs[4 * x + 3][4 * y + 3]) and (
                bs[4 * x][4 * y] == ply):
            self.block_status[x][y] = ply
            return 'SUCCESSFUL'
        if (bs[4 * x + 3][4 * y] == bs[4 * x + 2][4 * y + 1] == bs[4 * x + 1][4 * y + 2] == bs[4 * x][4 * y + 3]) and (
                bs[4 * x + 3][4 * y] == ply):
            self.block_status[x][y] = ply
            return 'SUCCESSFUL'


        for i in range(4):
            for j in range(4):
                if bs[4 * x + i][4 * y + j] == '-':
                    return 'SUCCESSFUL'
        self.block_status[x][y] = 'd'
        return 'SUCCESSFUL'

    def move(self, board, old_move, player_flag):

        self.ply=self.originaldepth
        self.board_status=copy.deepcopy(board.board_status)
        if player_flag == 'x':
            self.max_ply=5
        else:
            self.max_ply=4

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

        self.update((next_move[1], next_move[2]), player_flag)
        print self.num
        print (next_move[1], next_move[2],"yes")
        return (next_move[1], next_move[2])


    def heuristic(self, board, blockx,blocky, player):
        x_start = blockx*4
        y_start = blocky*4
        heuristic_value = 0

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

        lsum = 0
        for i in range(4):
            rowsum = 0
            for j in range(4):
                rowsum += blockvalues[i][j]
            x = 1
            flag = 0

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


        return overall_sum

    def get_utility(self, board, block, playerFlag, opFlag,depth):

        block_finalheuristic=[0 for i in range(16)]
        for i in range(16):
            block_finalheuristic[i]=block_heuristic_calculation(board, i, playerFlag)-block_heuristic_calculation(board, i, opFlag)

        x = calculate_heuristic(board, playerFlag, block_finalheuristic)
        return x

def calculate_heuristic(temp_board,player,similarity):
    #changed
        h=0
        h+=1
        h +=similarity_change(similarity,3,6,9,12)
        h += similarity_change(similarity,4,5,6,7)
        h +=similarity_change(similarity,0,5,10,15)
        h-=1
        h +=similarity_change(similarity,3,7,11,15)
        h += similarity_change(similarity,0,1,2,3)
        h += similarity_change(similarity,2,6,10,14)
        h+=1
        h += similarity_change(similarity,1,5,9,13)
        h +=similarity_change(similarity,0,4,8,12)
        h += similarity_change(similarity,12,13,14,15)
        h-=1
        h+= similarity_change(similarity,8,9,10,11)


        return h

def similarity_change(heuristic,i,j,k,l):

        h=0
        dummy = heuristic[i] + heuristic[j] + heuristic[k] + heuristic[l]
        flag=0
        if(dummy<0):
            flag=1
        eighty_p=0
        twenty_p=0
        lose=0
        zero_p=0
        zero_n=0
        twenty_n=0
        eighty_n=0
        win=0
        dummy = heuristic[i] + heuristic[j] + heuristic[k] + heuristic[l]
        dummy2=-heuristic[i] - heuristic[j] - heuristic[k] - heuristic[l]
        a=[i,j,k,l]
        b=[]
        for q in a:
            b.append(heuristic[q])
        pos=0
        for i in b:
            if i ==-1:
                lose+=1
            elif i==1:
                win+=1
            elif i > 0.15:
                eighty_p+=1
            elif i >= 0.08:
                twenty_p+=1
            elif i > 0:
                zero_p += 1
            elif i < -0.15:
                eighty_n+= 1
            elif i <= -0.08:
                twenty_n += 1
            elif i< 0:
                zero_n += 1
        if(eighty_p==3 and twenty_n==1):
            dummy=dummy*0.8
            dummy2 = dummy2 * 0.8
        if(eighty_p==3 and eighty_n==1):
            dummy=dummy*0.9
            dummy2 = dummy2 * 0.8
        if(eighty_p==3 and lose==1):
            dummy=dummy*0.5
            dummy2 = dummy2 * 0.8
        if(twenty_p==3 and eighty_n==1):
            dummy=dummy*0.9
            dummy2 = dummy2 * 0.8
        if(twenty_p==3 and lose==1):
            dummy=dummy*0.3
            dummy2 = dummy2 * 0.8


        if(win==3 and eighty_n==1):
            dummy=dummy*0.3
            dummy2 = dummy2 * 0.8
        if(win==3 and lose==1):
            dummy=0
            dummy2 = dummy2 * 0.8
        if(eighty_n==3 and eighty_p==1):
            dummy=dummy*1
            dummy2 = dummy2 * 0.8
        if(eighty_n==3 and win==1):
            dummy=dummy*0.4
            dummy2 = dummy2 * 0.8
        if(twenty_n==3 and eighty_p==1):
            dummy2 = dummy2 * 0.8
            dummy=dummy*0.8
        if(twenty_n==3 and win==1):
            dummy=dummy*0.6
            dummy2 = dummy2 * 0.8
        if(lose==3 and win==1):
            dummy=0
            dummy2 = dummy2 * 0.8
        if(lose==3 and eighty_p==1):
            dummy=dummy*0.3
            dummy2 = dummy2 * 0.8

        if(win==1 and zero_p==3):
            dummy=dummy*0.4
            dummy2 = dummy2 * 0.8
        elif (eighty_p==1 and zero_p==3):
            dummy=dummy*0.7
            dummy2 = dummy2 * 0.8

        if(lose==1 and zero_n==3):
            dummy=dummy*0.4

        elif (eighty_n==1 and zero_n==3):
            dummy=dummy*0.7
            dummy2 = dummy2 * 0.8
#changed
        if(flag==1):
            dummy=-dummy
            dummy2 = dummy2 * 0.8
#changed
        if dummy < 0.32:
            h += dummy
            dummy2 = dummy2 * 0.8
        elif dummy >= 0.32 and dummy <= 0.79:
            h += ( (dummy -0.24) *12)+1
            dummy2 = dummy2 * 0.8
        elif dummy >= 0.79 and dummy <4:
            h = (dummy-0.79)*90+10
            dummy2 = dummy2 * 0.8
        elif dummy>=4:
            h +=1000
            dummy2 = dummy2 * 0.8
#changed
        if(flag==1):
            return -h
        else:
            return (h)

def block_heuristic_calculation(temp_board,block_no,player_flag):
    #changed
        blockfinalheuristic=10
        block_x=(block_no/4)*4
        blockfinalheuristic+=5
        block_y=(block_no%4)*4
        if player_flag == 'x':
            player_flag = 'x'
            opp_flag = 'o'
            blockfinalheuristic-=5
        else:
            player_flag = 'o'
            opp_flag = 'x'
            blockfinalheuristic += 5
        return heuristic_calculation(temp_board,player_flag,opp_flag,block_x,block_y)
def heuristic_calculation(temp_board,player,opponent,row,column):
    noofsteps=0
    heuristic_value = 0
    noofsteps+=1

    for i in range(row,row+4):
        noofsteps += 1
        countr = 0
        noofsteps += 1
        countc = 0
        noofsteps += 1
        for j in range(column,column+4):
            noofsteps += 1
            if temp_board[i][j] == player:
                noofsteps += 1#for row
                countr += 1
                noofsteps += 1

            if temp_board[i][j] == opponent:
                noofsteps += 1
                countr = -10
                noofsteps += 1

            if temp_board[j-column+row][i-row+column] == player:
                noofsteps += 1# for column
                countc += 1
                noofsteps += 1


            if temp_board[j-column+row][i-row+column] == opponent:
                noofsteps += 1
                countc = -10
                noofsteps += 1

        if countr == 1:
            noofsteps += 1
            heuristic_value += 1
            noofsteps += 1
        elif countr == 2:
            noofsteps += 1
            heuristic_value += 10
            noofsteps += 1
        elif countr == 3:
            noofsteps += 1
            heuristic_value += 80
            noofsteps += 1
        elif countr==4:
            noofsteps += 1
            heuristic_value+=500
            noofsteps += 1
        if countc == 1:
            noofsteps += 1
            heuristic_value += 1
            noofsteps += 1
        elif countc == 2:
            noofsteps += 1
            heuristic_value += 10
            noofsteps += 1
        elif countc == 3:
            noofsteps += 1
            heuristic_value += 80
            noofsteps += 1
        elif countc==4:
            noofsteps += 1
            heuristic_value+=500
            noofsteps += 1
    count=0
    noofsteps += 1
    for i in range (4):
        noofsteps += 1# first diagonal
        if temp_board[row+i][column+i] == player:
            noofsteps += 1
            count += 1
            noofsteps += 1
        if temp_board[row+i][column+i] == opponent:
            noofsteps += 1
            count -= 10
            noofsteps += 1
    if count == 1:
        noofsteps += 1
        heuristic_value += 1
        noofsteps += 1
    elif count == 2:
        noofsteps += 1
        heuristic_value += 10
        noofsteps += 1
    elif count == 3:
        noofsteps += 1
        heuristic_value += 80
        noofsteps += 1
    elif count == 4:
        noofsteps += 1
        heuristic_value += 500
        noofsteps += 1


    count=0
    noofsteps += 1
    for i in range (4):
        noofsteps += 1# second diagonal
        if temp_board[row+i][column+3-i] == player:
            noofsteps += 1
            count += 1
            noofsteps += 1
        if temp_board[row+i][column+3-i] == opponent:
            noofsteps += 1
            count -= 10
            noofsteps += 1


    if count == 1:
        noofsteps += 1
        heuristic_value += 1
        noofsteps += 1
    elif count == 2:
        noofsteps += 1
        heuristic_value += 10
        noofsteps += 1
    elif count == 3:
        noofsteps += 1
        heuristic_value += 80
        noofsteps += 1
    elif count == 4:
        noofsteps += 1
        heuristic_value += 500
        noofsteps += 1
    if heuristic_value > 500:
        noofsteps += 1
        heuristic_value = 500
        noofsteps += 1
    return  (heuristic_value*1.0)/500

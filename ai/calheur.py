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

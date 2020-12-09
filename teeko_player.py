import random
import copy


class TeekoPlayer:
    """ An object representation for an AI game player for the game Teeko.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']
    counter = 0
    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.
            
        Args:
            state (list of lists): should be the current state of the game as saved in
                this TeekoPlayer object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.
                
                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).
        
        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """
        def heuristic_game_value(state):
            return self.score_board(state, self.my_piece)
                
        def possible_locations(state):
            valid_locations = []
            for r in range(5):
                for c in range(5):
                    if state[r][c] == ' ':
                        valid_locations.append([r,c])
            return valid_locations
    
        def test_place_piece(board, move, piece):
            if len(move) > 1:
                board[move[1][0]][move[1][1]] = ' '
            board[move[0][0]][move[0][1]] = piece
            return board
        
        def minimax(board, depth, alpha, beta, max_player):
           source_row = 0
           source_col = 0
           drop_phase = True
           temp_board = copy.deepcopy(board)
           for i in range(5):
               for j in range(5):
                   if temp_board[i][j] == self.my_piece:
                       self.counter = self.counter + 1
           if self.counter < 4:
               drop_phase = True
           else:
               drop_phase = False
               
           if not drop_phase:
            # choose a piece to move and remove it from the board
            # (You may move this condition anywhere, just be sure to handle it)
            #
            # Until this part is implemented and the move list is updated
            # accordingly, the AI will not follow the rules after the drop phase!
            #is valid location board[row][col] == 0
                valid_locations = possible_locations(temp_board)
                if depth == 0:
                   return (None, None, heuristic_game_value(temp_board), False)
                elif (self.game_value(temp_board)) == 1 or (self.game_value(temp_board) == -1):
                   if self.game_value(temp_board) == 1 or self.game_value(temp_board) == -1:
                       if heuristic_game_value(temp_board) == -1:
                           return (None, None, -1, False)
                       elif heuristic_game_value(temp_board) == 1:
                           return (None, None, 1, False)
                if max_player:
                    value = -1
                    row,col = random.choice(valid_locations)[0],[1]
                    for i in range(5):
                       for j in range(5):
                           if temp_board[i][j] == ' ':
                                r = i
                                c = j
                                temp_board_copy = copy.deepcopy(temp_board)
                                for i in range(5):
                                    for j in range(5):
                                        if temp_board[i][j] == self.my_piece:
                                            source_row = i
                                            source_col = j
                                            break
                                        break
                                move = [(r, c), (source_row, source_col)]
                                temp_board_copy = test_place_piece(temp_board, move, self.my_piece)
                                temp = minimax(temp_board_copy, depth-1, alpha, beta, False)
                                updated_score = temp[2]
                                if updated_score >= value:
                                    value = updated_score
                                    row = r
                                    col = c
                                alpha = max(alpha, value)
                                if alpha >= beta:
                                    break
                    return row, col, value, drop_phase, source_row, source_col
               
                else: #Min Player
                    value = 1
                    row,col = random.choice(valid_locations)[0],[1]
                    for i in range(5):
                       for j in range(5):
                           if temp_board[i][j] == ' ':
                               r = i
                               c = j
                               temp_board_copy = copy.deepcopy(temp_board)
                               for i in range(5):
                                   for j in range(5):
                                       if temp_board[i][j] == self.opp:
                                           source_row = i
                                           source_col = j
                                           break
                                       break
                               move = [(r, c), (source_row, source_col)]
                               temp_board_copy = test_place_piece(temp_board, move, self.opp)
                               temp = minimax(temp_board_copy, depth-1, alpha, beta, True)
                               updated_score = temp[2]
                               if updated_score <= value:
                                   value = updated_score
                                   row = r
                                   col = c
                               beta = min(beta, value)
                               if alpha >= beta:
                                   break
                    return row, col, value, drop_phase, source_row, source_col
                
           if drop_phase:     
               valid_locations = possible_locations(temp_board)
               if depth == 0:
                   return (None, None, heuristic_game_value(temp_board), False)
               elif (self.game_value(temp_board)) == 1 or (self.game_value(temp_board) == -1):
                   if self.game_value(temp_board) == 1 or self.game_value(temp_board) == -1:
                       if heuristic_game_value(temp_board) == -1:
                           return (None, None, -1, False)
                       elif heuristic_game_value(temp_board) == 1:
                           return (None, None, 1, False)
               if max_player:
                   value = -1
                   row,col = random.choice(valid_locations)[0],[1]
                   r = 0
                   c = 0
                   for i in range(5):
                       for j in range(5):
                           if temp_board[i][j] == ' ':
                               r = i
                               c = j
                               temp_board_copy = copy.deepcopy(temp_board)
                               move = [(r, c)]
                               temp_board_copy = test_place_piece(temp_board, move, self.my_piece)
                               temp = minimax(temp_board_copy, depth-1, alpha, beta, False)
                               updated_score = temp[2]
                               if updated_score >= value:
                                   value = updated_score
                                   row = r
                                   col = c
                               alpha = max(alpha, value)
                               if alpha >= beta:
                                   break
                   return row, col, value, drop_phase
               
               else: #Min Player
                   value = 1
                   row,col = random.choice(valid_locations)[0],[1]
                   r = 0
                   c = 0
                   for i in range(5):
                       for j in range(5):
                           if temp_board[i][j] == ' ':
                               r = i
                               c = j
                               temp_board_copy = copy.deepcopy(temp_board)
                               move = [(r, c)]
                               temp_board_copy = test_place_piece(temp_board, move, self.opp)
                               temp = minimax(temp_board_copy, depth-1, alpha, beta, True)
                               updated_score = temp[2]
                               if updated_score <= value:
                                   value = updated_score
                                   row = r
                                   col = c
                               beta = min(beta, value)
                               if alpha >= beta:
                                   break
                   return row, col, value, drop_phase

          
        move = []             
        if (minimax(state, 3, 1, -1, True)[3]):
             resulting_state = minimax(state, 3, 1, -1, True)
             row = resulting_state[0]
             col = resulting_state[1]
             move.insert(0, (row,col))
        else:
            source_row = minimax(state, 3, 1, -1, True)[4]
            source_col = minimax(state, 3, 1, -1, True)[5]
            row = minimax(state, 3, 1, -1, True)[0]
            col = minimax(state, 3, 1, -1, True)[1]
            move.insert(0, (row,col))
            move.insert(1, (source_row, source_col))

        return move

    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                raise Exception("You don't have a piece there!")
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)
        
    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece
        
        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
                
                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece
        
    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")
  
    def game_value(self, state):
        """ Checks the current board status for a win condition
        
        Args:
        state (list of lists): either the current state of the game as saved in
            this TeekoPlayer object, or a generated successor state.

        Returns:
            int: 1 if this TeekoPlayer wins, -1 if the opponent wins, 0 if no winner

        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    return 1 if state[i][col]==self.my_piece else -1
        # checks ascending diagonal 
        for row in range(2):
            for col in range(3,5):
                if state[row][col] != ' ' and state[row][col] == state[row+1][col-1] == state[row+2][col-2] and state[row+3][col-3]:
                    return 1 if state[row][col]==self.my_piece else -1
        #checks descending diagonal
        for row in range(2):
            for col in range(2):
                if state[row][col] != ' ' and state[row][col] == state[row+1][col+1] == state[row+2][col+2] and state[row+3][col+3]:
                    return 1 if state[row][col]==self.my_piece else -1
        #check 2x2 box wins
        for row in range(4):
            for col in range(4):
                if state[row][col] != ' ' and state[row][col] == state[row + 1][col] == state[row][col + 1] == state [row + 1][col + 1]:
                    return 1 if state[row][col]==self.my_piece else -1
        # no winner yet
        return 0 

    def check_array_value(self, check_array, check_array1, piece):
        score = 0
        opp_piece = self.my_piece
        if piece == self.my_piece:
            opp_piece == self.opp
        if len(check_array1) == 0:    
            if check_array.count(piece) == 4:
                score += 1
            elif check_array.count(piece) == 3 and check_array.count(None) == 1:
                score += 0.75
            elif check_array.count(piece) == 2 and check_array.count(None) == 2:
                score += 0.5
            if check_array.count(opp_piece) == 3 and check_array.count(None) == 1:
                score -= 0.75
    
        else:
            if check_array.count(piece) + check_array1.count(piece) == 3:
                score += 0.5
            elif check_array.count(self.opp) + check_array1.count(self.opp) == 3:
                score -= 0.5
        return score
        

    def score_board(self, state, piece):
        score = 0
        check_array = []
        check_array1 = []
            
        #Score 2x2 box
        row_array1 = []
        col_array1 = []
        check_array = []
        check_array1 = []
        for r in range(5):
            for i in range(2):
                row_array1.append(state[r][i])
            for c in range(5):
                for i in range(2):
                    col_array1.append(state[i][c])
                check_array.append(row_array1[r])
                check_array.append(row_array1[r+1])
                check_array1.append(col_array1[c])
                check_array1.append(col_array1[c+1])
                score += self.check_array_value(check_array, check_array1, piece)
    
        #Score ascending diagonal
        check_array = []
        for r in range(2):
            for c in range(2):
                check_array = [state[r+i][c+i] for i in range (4)]
                score += self.check_array_value(check_array, check_array1, piece)
        
        #Score descending diagonal
        check_array= []
        for r in range(2):
            for c in range(2):
                check_array = [state[r+3-i][c+i] for i in range (4)]
                score += self.check_array_value(check_array, check_array1, piece)
                
        #Score Horizontal
        check_array = []
        temp_array = []
        for r in range(5):
            for i in range(5):
                temp_array.append(state[r][i])
            for c in range(2):
                check_array.append(temp_array[c])
                check_array.append(temp_array[c+1])
                check_array.append(temp_array[c+2])
                check_array.append(temp_array[c+3])
                score += self.check_array_value(check_array, check_array1, piece)
        
        #Score Vertical
        check_array = []
        col_array = []
        for c in range(5):
            for i in range(5):
                col_array.append(state[i][c])
            for r in range(2):
                check_array.append(col_array[r])
                check_array.append(col_array[r+1])
                check_array.append(col_array[r+2])
                check_array.append(col_array[r+3])
                score += self.check_array_value(check_array, check_array1, piece)
                            
        return score/10
        
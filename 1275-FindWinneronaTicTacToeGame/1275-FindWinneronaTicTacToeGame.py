# Last updated: 8/21/2025, 9:29:34 AM
class Solution(object):

    def check_diagonal(self, moves):
        diagonal_1 = [[0,0],[1,1],[2,2]]
        diagonal_2 = [[0,2], [1,1], [2,0]]

        count_diagonal_1 = 0
        count_diagonal_2 = 0

        for move in moves:
            if move in diagonal_1:
                count_diagonal_1 += 1
            
            if move in diagonal_2:
                count_diagonal_2 += 1
            
        if count_diagonal_1 == 3 or count_diagonal_2 == 3:
            return True
        
        return False

    def check_row(self, moves):
        row_counts = [0, 0, 0]

        for row, col in moves:
            row_counts[row] += 1

        return 3 in row_counts

    def check_column(self, moves):
        col_counts = [0, 0, 0]

        for row, col in moves:
            col_counts[col] += 1

        return 3 in col_counts
    
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """

        '''
        - every other move corresponds to each player
        - can have functions check for diagonal, row, or column
        -   pass in a list of all the moves each player made
        '''
        # print(moves)

        player_a_moves = [move for move in moves if moves.index(move) % 2 == 0]
        player_b_moves = [move for move in moves if moves.index(move) % 2 == 1]


        result = self.check_diagonal(player_a_moves)
        print(result)

        moves_list = [player_a_moves, player_b_moves]

        won = False
        winning_player = None

        for i in moves_list:
            if self.check_diagonal(i) or self.check_row(i) or self.check_column(i):
                won = True
                winning_player = moves_list.index(i)
        
        if won != True:
            if len(moves) == 9:
                return 'Draw'
            else:
                return 'Pending'

        if winning_player == 0:
            return 'A'
        else:
            return 'B'
        


        
        



        
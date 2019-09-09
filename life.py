from scipy import ndimage
import numpy as np

from generators import GOLBoardGenerator

class GOL:
    
    def __init__(self, size, board_generator: GOLBoardGenerator):
        self.__board_generator = board_generator
        self.cols = size
        self.rows = size
        self.reset_board() #create new board
        #prepare kernel, defines rules
        self.kernel = np.ones((3,3))
        self.kernel[1][1] = 0

        self.ressurect_rule = [3]
        self.die_rule = [0, 1, 4, 5, 6, 7, 8]

    def reset_board(self):
        self.board = self.__board_generator.generate(self.cols, self.rows)

    def next_tick(self):
        
        tmp = ndimage.convolve(self.board, self.kernel, mode='constant', cval=0.0)
    
        for r in range(self.rows):
            for c, x in enumerate(self.board[r]):        
                y = tmp[r][c] #conv value number of allive cells around
                if x == 0 and y in self.ressurect_rule:
                    self.board[r][c] = 1
                elif x == 1 and y in self.die_rule:
                    self.board[r][c] = 0
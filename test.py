class GOLTestBoard:
    
    def generate(self, cols: int, rows: int):
        t = (np.zeros((cols, rows))).astype(int)
        #oscilator
        t[1][1] = 1
        t[2][1] = 1
        t[3][1] = 1
        # Staw
        t[1][6] = 1
        t[1][7] = 1
        t[2][5] = 1
        t[2][8] = 1
        t[3][5] = 1
        t[3][8] = 1
        t[4][6] = 1
        t[4][7] = 1
    
        t[7][2] =1
        return t

#@TODO finish it - fatality 
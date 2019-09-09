import numpy as np

class GOLBoardGenerator:
    def generate(self, cols: int, rows: int):
        raise NotImplementedError("Implementation needed")

class GOLBoardGeneratorRandom:

    def generate(self, cols: int, rows: int):
        return (np.random.random((cols, rows)) < 0.5).astype(int)
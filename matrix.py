from array import array as _

class matrix:
    def __init__(self, array):
        array = _("f", array)
        self.__check_matrix(array)
        self.__init_matrix(array)
        self.__matrix = array

    def __check_matrix(self, array):
        if len(array) <= 0:
            raise self.InitializationException("Matrix empty")

    def __init_matrix(self, array):
        rows = len(array)
        cols = len(array[0])
        for r in array[1:]:
            if cols != len(r):
                raise self.InitializationException("Matrix must be square")
        self.shape = (rows, cols)
        self.size = self.shape[0] * self.shape[1]
    
    def __getitem__(self, pos):
        r,c = pos
        return self.__matrix[r][c]
    
    def __setitem__(self, pos, data):
        r,c = pos
        self.__matrix[r][c] = data
    
    def __str__(self):
        string = "matrix("
        m = [[str(c) for c in r] for r in self.__matrix]
        m = [str(r) for r in self.__matrix]
        string += "\n       ".join(m)
        string += ")"
        return string
    
    def __add__(self, y):
        return matrix.add(self, y)
    
    def __sub__(self, y):
        return matrix.subtract(self, y)
    
    def __mul__(self, y):
        if isinstance(y, matrix):
            return matrix.dot(self, y)
        else:
            return matrix.multiply(self, y)
    
    def __rmul__(self, y):
        return self.__mul__(y)

    def copy(self):
        new = matrix.zeros(*self.shape)
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                new[r,c] = self[r,c]
        return new

    def map(self, f):
        new = matrix.zeros(*self.shape)
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                new[r,c] = f(self[r,c])
        return new
    
    def tolist(self):
        return self.__matrix.tolist()
    
    @staticmethod
    def transpose(x):
        new = matrix.zeros(x.shape[1], x.shape[0])
        for r in range(new.shape[0]):
            for c in range(new.shape[1]):
                new[r,c] = x[c,r]
        return new

    @staticmethod
    def add(x, y):
        if x.shape != y.shape:
            raise matrix.OperationException("x and y must have the same shape")
        shape = x.shape
        new = matrix.zeros(*shape)
        for r in range(shape[0]):
            for c in range(shape[1]):
                s = x[r,c] + y[r,c]
                new[r,c] = s
        return new
    
    @staticmethod
    def subtract(x, y):
        if x.shape != y.shape:
            raise matrix.OperationException("X and Y must have the same shape")
        shape = x.shape
        new = matrix.zeros(*shape)
        for r in range(shape[0]):
            for c in range(shape[1]):
                s = x[r,c] - y[r,c]
                new[r,c] = s
        return new
    
    @staticmethod
    def dot(x, y):
        if x.shape[1] != y.shape[0]:
            raise matrix.OperationException("The number of columns in X must be equal to the number of rows in Y")
        shape = (x.shape[0], y.shape[1])
        new = matrix.zeros(*shape)
        for r in range(x.shape[0]):
            for c in range(y.shape[1]):
                s = 0.0
                times = x.shape[1]
                for i in range(times):
                    s += x[r,i] * y[i,c]
                new[r,c] = s
        return new

    @staticmethod
    def entrywise(x, y):
        if x.shape != y.shape:
            raise matrix.OperationException("X and Y must have the same shape")
        shape = x.shape
        new = matrix.zeros(*shape)
        for r in range(shape[0]):
            for c in range(shape[1]):
                s = x[r,c] * y[r,c]
                new[r,c] = s
        return new
    
    @staticmethod
    def multiply(m, i):
        new = m.copy()
        for r in range(new.shape[0]):
            for c in range(new.shape[1]):
                new[r,c] *= i
        return new
    
    @staticmethod
    def zeros(rows, cols):
        return matrix([[0.0] * cols] * rows)

    class InitializationException(Exception):
        pass
    
    class OperationException(Exception):
        pass
        

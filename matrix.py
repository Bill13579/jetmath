from array import array as _

class matrix:
    def __init__(self, array):
        self.__check_matrix(array)
        self.__init_matrix(array)
        self.__matrix = _("f", [c for r in array for c in r])

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
        if r >= self.shape[0] or c >= self.shape[1]:
            raise IndexError("matrix index out of bound")
        return self.__matrix[c+r*self.shape[1]]
    
    def __setitem__(self, pos, data):
        r,c = pos
        if r >= self.shape[0] or c >= self.shape[1]:
            raise IndexError("matrix index out of bound")
        self.__matrix[c+r*self.shape[1]] = data
    
    def __str__(self):
        string = "matrix( "
        m = [str(i) for i in self.__matrix]
        length = max([len(i) for i in m])
        space = 2
        m = []
        for i in range(0, len(self.__matrix), self.shape[1]):
            r = self.__matrix[i:i+self.shape[1]]
            tmp = [str(i)+(length-len(str(i))+space)*" " for i in r[:-1]]
            tmp.append(str(r[-1]))
            m.append("".join(tmp))
        string += "\n        ".join(m)
        string += " )"
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
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                self[r,c] = f(self[r,c])
    
    def tolist(self):
        l = []
        for i in range(0, len(self.__matrix), self.shape[1]):
            r = self.__matrix[i:i+self.shape[1]]
            l.append(r.tolist())
        return l
    
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
        

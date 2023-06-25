class Matrix:
    def __init__(self, matrix:list) -> None:
        if self.validate(matrix=matrix):
            self.columns = len(matrix[0])
            self.rows = len(matrix)
            self.matrix = matrix
        else:
            raise Exception


    def validate(self, matrix) -> bool:
        self.columns = len(matrix[0])
        try:
            for row in matrix:
                if self.columns != len(row):
                    raise Exception
        except:
            return False
        return True


    def add(self, entry_matrix):
        if self.rows == entry_matrix.rows and self.columns == entry_matrix.columns:
            result = [[0 for i in range(self.columns)] for j in range(self.rows)]
            # print(result)
            for i in range(self.rows):
                for j in range(self.columns):
                    result[i][j] = self.matrix[i][j] +  entry_matrix.matrix[i][j]
                    # print(entry_matrix.matrix[i][j])
                    # print(self.matrix[i][j])
            return Matrix(result)
        print("Your entry matrix is not valid!")
    

    def multiple(self, entry_matrix):
        if self.columns == entry_matrix.rows:
            result = [[0 for i in range(self.rows)] for j in range(entry_matrix.columns)]
            for i in range(self.rows):
                for j in range(entry_matrix.columns):
                    for k in range(entry_matrix.rows):
                        result[i][j] += self.matrix[i][k] * entry_matrix.matrix[k][j]
            return Matrix(result)
        print("Your entry matrix is not valid!")


m1 = Matrix([[1,2],[3,4],[5,6]])
m2 = Matrix([[1,2],[3,4],[5,6]])
m3 = Matrix([[1,2,3],[3,4,5]])
print(m1.add(m2).matrix)
print(m1.multiple(m3).matrix)
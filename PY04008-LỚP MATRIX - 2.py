class Matrix:
    def __init__(self, n, m, data=None):
        self.n = n
        self.m = m
        self.data = data if data else [[0]*m for _ in range(n)]

    def transpose(self):
        transposed = [[self.data[i][j] for i in range(self.n)] for j in range(self.m)]
        return Matrix(self.m, self.n, transposed)

    def multiply(self, other):
        result = [[0]*other.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(self.n, other.m, result)

    def print_matrix(self):
        for row in self.data:
            print(' '.join(map(str, row)))

# Đọc dữ liệu
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    a = Matrix(n, m, data)
    aT = a.transpose()
    product = a.multiply(aT)
    product.print_matrix()

def createMatrix():
    fileira = 10
    coluna = 10
    matrix = [[0 for x in range(fileira)] for y in range(coluna)]
    matrix[0][1] = matrix[1][0] = 17
    matrix[0][2] = matrix[2][0] = 3
    matrix[0][3] = matrix[3][0] = 35
    matrix[0][4] = matrix[4][0] = 43
    matrix[0][5] = matrix[5][0] = 26
    matrix[0][6] = matrix[6][0] = 44
    matrix[0][7] = matrix[7][0] = 5
    matrix[0][8] = matrix[8][0] = 8
    matrix[0][9] = matrix[9][0] = 9
    matrix[1][2] = matrix[2][1] = 20
    matrix[1][3] = matrix[3][1] = 31
    matrix[1][4] = matrix[4][1] = 47
    matrix[1][5] = matrix[5][1] = 11
    matrix[1][6] = matrix[6][1] = 51
    matrix[1][7] = matrix[7][1] = 22
    matrix[1][8] = matrix[8][1] = 8
    matrix[1][9] = matrix[9][1] = 23
    matrix[2][3] = matrix[3][2] = 38
    matrix[2][4] = matrix[4][2] = 45
    matrix[2][5] = matrix[5][2] = 29
    matrix[2][6] = matrix[6][2] = 45
    matrix[2][7] = matrix[7][2] = 3
    matrix[2][8] = matrix[8][2] = 11
    matrix[2][9] = matrix[9][2] = 9
    matrix[3][4] = matrix[4][3] = 19
    matrix[3][5] = matrix[5][3] = 25
    matrix[3][6] = matrix[6][3] = 27
    matrix[3][7] = matrix[7][3] = 36
    matrix[3][8] = matrix[8][3] = 33
    matrix[3][9] = matrix[9][3] = 32
    matrix[4][5] = matrix[5][4] = 43
    matrix[4][6] = matrix[6][4] = 10
    matrix[4][7] = matrix[7][4] = 43
    matrix[4][8] = matrix[8][4] = 46
    matrix[4][9] = matrix[9][4] = 37
    matrix[5][6] = matrix[6][5] = 49
    matrix[5][7] = matrix[7][5] = 30
    matrix[5][8] = matrix[8][5] = 19
    matrix[5][9] = matrix[9][5] = 30
    matrix[6][7] = matrix[7][6] = 42
    matrix[6][8] = matrix[8][6] = 48
    matrix[6][9] = matrix[9][6] = 35
    matrix[7][8] = matrix[8][7] = 13
    matrix[7][9] = matrix[9][7] = 6
    matrix[8][9] = matrix[9][8] = 16

def main():
    createMatrix()
    print("funfa")
main()
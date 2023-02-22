# conwert array to chessboard position (0,0) = (a,1)
def conwert(bord):
    all = []
    for i in range(8):
        for j in range(8):
            if bord[i][j] == 1:
                all.append(str(i+1)+str(i+1)+"w")
            elif bord[i][j] == 2:
                all.append(str(i+1)+str(i+1)+"b")
            elif bord[i][j] == 3:
                all.append(str(i+1)+str(i+1)+"W")
            elif bord[i][j] == 4:
                all.append(str(i+1)+str(i+1)+"B")
    return all


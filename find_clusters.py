def find_neighbors(matrix,length,width,x,y):
    matrix[x][y]=0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if x+dx !=-1 and x+dx<length and y+dy!=-1 and y+dy<width:
                if matrix[x+dx][y+dy]:
                    find_neighbors(matrix,length,width,x+dx,y+dy)

def find_clusters(matrix):
    length = len(matrix)
    width = len(matrix[0])
    clusters=0
    for l in range(length):
      for w in range(width):
        if matrix[l][w]:
            find_neighbors(matrix,length,width,l,w)
            clusters+=1
    print "clusters: ",clusters
#


if __name__ == "__main__":
    matrix = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    matrix1 = [[1, 1, 0], [0, 0, 0], [0, 1, 0]]
    matrix2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    matrix3 = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    print "Matrix"
    find_clusters(matrix)
    print "Matrix1"
    find_clusters(matrix1)
    print "Matrix2"
    find_clusters(matrix2)
    print "Matrix3"
    find_clusters(matrix3)
def find_holes(holes):
    row=len(holes)
    column=len(holes[0])
    #print(row,column)
    for_row=[]
    for_column=[]
    for i in range(row-1):#for row holes
        for j in range(column):
            for_row.append(not(int(holes[i][j])|int(holes[i+1][j])))
    #print(for_row)
    for i in range(row):#for column holes
        for j in range(column-1):
            for_column.append(not(int(holes[i][j])|int(holes[i][j+1])))
    #print(for_column)
    count=0
    count+=for_row.count(True)
    count+=for_column.count(True)
    return count


def bithole(a):
    holes=[]
    for i in a:
        holes.append(str(i))
    return find_holes(holes)

a= list(map(str,input().split(",")))
print(bithole(a))

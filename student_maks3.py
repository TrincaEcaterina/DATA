

# name  |  s1  |  s2  |  ge  |  avr
#------------------------------------
# John  |  9.0 |  8.0 | 10.0 |      |
# Mary  |  8.0 |  9.0 |  9.0 |      |
# Peter |  8.0 |  8.0 | 10.0 |      |
#------------------------------------

col_header = [ 'name', 's1', 's2', 'ge', 'avg']


col_marks = [
    [ "John",  9.0, 8.0, 10.0 ],
    [ "Mary",  8.0, 9.0,  9.0 ],
    [ "Peter", 8.0, 8.0, 10.0 ]
]

for ci in range(len(col_header)):  
    print(f"|{col_header[ci]:^8}|", end=" ")
print()

for y in range(len(col_marks)):
    s=col_marks[y][1] + col_marks[y][2] + col_marks[y][3] 
    a= s/3
    col_marks[y].append(a)





for ri in range(len(col_marks)):
    for ci in range(len(col_marks[0])):    
        print (f"|{col_marks[ri][ci]:<8.3}|", end=" ")
    print()



    
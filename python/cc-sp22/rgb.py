t = input()

out = []

for i in range (int(t)):
    rowcol = input()
    row = int(rowcol[0])
    col = int(rowcol[2])

    o = []
    
    for r in range (row):
        rowstr = str()
        
        for c in range (col):
            if r % 2 == False:
                if c % 2 == False:
                    rowstr = rowstr + "B"
                
                else:
                    rowstr = rowstr + "G"
            
            else:
                if c % 2 == False:
                    rowstr = rowstr + "G"
                
                else:
                    rowstr = rowstr + "R"
                
            
        o.append(rowstr)
    
    out.append(o)

for x in range (len(out)):
    for y in range (len(out[x])):
        print(out[x][y])
    print()


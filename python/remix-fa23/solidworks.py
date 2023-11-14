def solve(sw, h, w, d):
    new = [[' ' for i in range(w + d + 1)] for x in range(h + d + 1)]
    edges = []
    

    # transpose the original shape on the new list
    for row in range(h):
        for col in range(w):
            new[row + d + 1][col + d + 1] = sw[row][col]

            if sw[row][col] == '+':
                edges.append((row + d + 1, col + d + 1))
    
    # extend edges
    for edge in edges:
        for i in range(1, d + 1):
            if new[edge[0] - i][edge[1] - i] not in ('-', '|', '+'):
                new[edge[0] - i][edge[1] - i] = '\\'
    
    # place back side of shape
    for row in range(h):
        for col in range(w):
            if new[row][col] == ' ':   
                new[row][col] = sw[row][col]            
    
    return new


def main():
    for _ in range(int(input())):
        h, w, d = map(int, input().split())
        sw = []
        
        for _ in range(h):
            sw.append(list(input()))
        
        sol = solve(sw, h, w, d)
        print("\n".join(["".join(x) for x in sol]))    

main()

def solve(cypher, steps):
    for step in steps:
        if 'C' in step:
            pass
        elif 'A' in step:
            pass
        else:
            cypher.reverse()
    
    return cypher


def main():
    for _ in range(int(input())):
        cypher = input()
        input()
        steps = input.split()
        
        print(solve(cypher, steps))
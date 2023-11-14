def solve(powers, distances, towers):
    hours = list()
    
    for x in range(towers):
        time = 0
        power = 0
        
        for y in range(towers):
            towPow = powers[(x + y) % len(powers)]
            
            # If Herry must wait
            if towPow > power:
                time += towPow - power
                power = towPow
        
            elif towPow <= power:
                pass
            
            # If Herry isn't at the last tower, add travel distance to time and power
            if y != towers - 1:
                d = distances[(x + y) % len(distances)]
                time += d
                power += d
            
        hours.append(time)
    
    return min(hours)


for _ in range(int(input())):
    towers = int(input())
    powers = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    
    print(solve(powers, distances, towers))
    
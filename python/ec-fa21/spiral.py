def solve(loops: int) -> list[list[str]]:
	dims = loops * 4 + 1
	x, y = 0, 0
	offset = 0
	center = dims // 2
	spiral = [[' ' for _ in range(dims)] for _ in range(dims)]
	
	while True:
		while x < dims - offset:
			spiral[y][x] = '@'
			x += 1
		x -= 1
		
		if x == center and y == center:
			break
		
		while y < dims - offset:
			spiral[y][x] = '@'
			y += 1
		y -= 1
		
		while x > 0 + offset:
			spiral[y][x] = '@'
			x -= 1
		
		offset += 2
		
		while y > 0 + offset:
			spiral[y][x] = '@'
			y -= 1
		
	return spiral
	

def main():
	for _ in range(int(input())):
		print("\n".join(map(lambda l: "".join(l), solve(int(input())))))
		print()
	
	
main()

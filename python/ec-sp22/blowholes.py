# Sliding Window approach; find the longest sequence of wales within k of each other.
def solve(n: list[int], k: int, l: int) -> int:
	p1, p2 = 0, 0
	longest = 0
	n.sort()
	
	while p2 < l:
		if n[p2] - n[p1] > k:
			p1 += 1
		else:
			p2 += 1
		
		longest = max((longest, p2 - p1))

	return l - longest


def main():
	for _ in range(int(input())):
		l, k = list(map(int, input().split()))
		n = list(map(int, input().split()))
		
		print(solve(n, k, l))
		input()
		
		
main()

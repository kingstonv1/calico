def solve(inv, chest):
	return " ".join(sorted(inv + chest))


for _ in range(int(input())):
	input()
	playerInventory = input().split()
	chestInventory = input().split()
	print(solve(playerInventory, chestInventory))
	
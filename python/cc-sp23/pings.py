def solve_test_case(Q, N, M, actions):
    roles = [[] for i in range(N)]  # list of lists to store which users have which roles
    pings = [0] * M  # list to store the number of times each user has been pinged

    for i in range(Q):
        action = actions[i].split()
        if action[0] == "A":
            role = int(action[1]) - 1
            user = int(action[2]) - 1
            roles[role].append(user)
        elif action[0] == "R":
            role = int(action[1]) - 1
            user = int(action[2]) - 1
            roles[role].remove(user)
        elif action[0] == "P":
            role = int(action[1]) - 1
            for user in roles[role]:
                pings[user] += 1

    return pings


for _ in range(int(input())):
    Q, N, M = map(int, input().split())
    actions = list()

    for i in range(Q):
        actions.append(input())

    pings = solve_test_case(Q, N, M, actions)
    print(" ".join(map(str, pings)))

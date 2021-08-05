# THIS IS DP! :D

n = int(input())
wd = {}
sol = {}
for i in range(n):
    d = input()
    wd[d[:3]] = d[-3:]
    if d[:3] == d[-3:]:
        sol[d[:3]] = 'Draw'

def solve(player, end, visited):
    # Solve for player 'player' with starting end 'end'
    if end in visited:
        sol[end] = 'Draw'
        return 'Draw'
    visited.append(end)

    if end in sol:
        return sol[end]
    
    if not end in wd:
        sol[end] = player
        return player
    
    for e in wd[end]:
        if e in sol:
            if sol[e] == player:
                sol[end] = player
                return player
        else:
            solve(player == 'Takahashi' ? 'Aoki' : 'Takahashi', e, visited)

for i in range(n):
    print(solve('Takahashi', n[i][-3:], list()))
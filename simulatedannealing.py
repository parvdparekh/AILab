import math, random

def solve_nqueens(n, s):
    def conf(b):
        return sum(b[i] == b[j] or abs(b[i] - b[j]) == (j - i) for i in range(n) for j in range(i + 1, n))

    curr, c_cost, T = list(s), conf(s), 100.0
    while c_cost > 0 and T > 1e-4:
        col, row = random.randint(0, n - 1), random.randint(0, n - 1)
        if row == curr[col]: continue
        nxt = list(curr)
        nxt[col] = row
        n_cost = conf(nxt)
        delta = n_cost - c_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            curr, c_cost = nxt, n_cost
        T *= 0.99
    return curr

if __name__ == "__main__":
    n = int(input('Enter n: '))
    print("Enter queen positions:")
    s = [int(input()) for _ in range(n)]
    x=solve_nqueens(n, s)
    print(x)
    board=['.'*i+'Q'+'.'*(n-i-1) for i in x]
    for i in board: print(i)
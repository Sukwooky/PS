#BOJ 9663 N-Queen(G5)
#Backtracking
#시간초과
n = int(input())
cnt = 0
chess = [0 for _ in range(n)]
visited = [False for _ in range(n)]  # 시간초과 막아줌


def promise(row, n):
    for i in range(row):
        if abs(chess[i] - n) == abs(i - row):
            return False
        # 여기에서 맨 처음에는 대각선 뿐만 아니라 i == n 을 비교하니까 시간 초과!!
        # 심지어 pypy인데도 초과
    return True


def back(row):
    global cnt

    if row == n:
        cnt += 1
        return

    for i in range(0, n):
        if visited[i]:
            continue
        if promise(row, i) is True:
            visited[i] = True
            chess[row] = i
            back(row + 1)
            visited[i] = False
            # 백트레킹 기본 구조
            # 시간 초과 방지 위해 항상 visited를 사용해주는 걸로 ...


back(0)
print(cnt)
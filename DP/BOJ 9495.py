# BOJ 9495 스티커 (S1)
# 읽어보니 dp, 끝점을 기준으로 생각해야 한다.
# 고민한 점: dp배열을 불필요하게 많이 만들 필요가 있나 싶었음. (6개만 있어도 되지 않나)
import sys

input = sys.stdin.readline

T = int(input())
for time in range(T):
    n = int(input())

    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    #예외 빠짐 ,n을 포문으로 한번에 구현하면 예외 안 만들어도 될듯.

    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[0][1] = sticker[0][1] + sticker[1][0]
    dp[1][0] = sticker[1][0]
    dp[1][1] = sticker[1][1] + sticker[0][0]

    for i in range(2, n):
        dp[0][i] = sticker[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = sticker[1][i] + max(dp[0][i - 1], dp[0][i - 2])
        #점화식

    print(max(dp[0][n - 1], dp[1][n - 1]))

# dp는 뒤에서부터 보는게 편함
# 끝처리 하기.(n == 1일때)
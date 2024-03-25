import sys

input = sys.stdin.readline

# 입력받는거 1줄에 2개의 int니까 map, split 해줘야함
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 방문했는지 확인을 위해 입력받은 배열과 같은 크기의 False 기본값인 배열 생성
check = [[False] * M for _ in range(N)]

dy = [0, 1, 0, -1]  # 상하좌우 이동을 위한 (세로)
dx = [1, 0, -1, 0]  # 상하좌우 이동을 위한 (가로)


def bfs(y, x):
    # bfs 함수에 진입한 위치에는 그림이 무조건 있다는 거니까, 기본 사이즈는 1로 설정함
    result = 1
    # Queue 구조 (먼저 들어온 순서대로 나감) 만들어주기 / 함수 진입 위치로
    q = [(y, x)]
    # Queue가 없다는 건 모든 배열 다 돌았다는거니까, 종료 조건을 queue의 False로 잡는 것
    while q:
        # queue에 들어있는 값을 새로운 변수에 넣어준다. (y, x 위치를 가져오는거)
        ey, ex = q.pop()
        # 동서남북 4 방향으로 탐색하는 거니까 range(4)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            # 입력 배열을 초과하면 안되니까, 배열의 세로 가로 크기 미만까지로 기준 잡아줌
            if 0 <= ny < N and 0 <= nx < M:
                # 탐색을 할지 말지에 대한 기준 1. 해당 위치의 값이 1인가? 2. 해당 위치에 방문하지 않았는가?
                if board[ny][nx] == 1 and check[ny][nx] == False:
                    # 조건을 통과한다면, 맨 처음 함수에 입력한 위치와 연결된 위치에 그림이 있다는 거니까 그림 사이즈 1 올려줌
                    result += 1
                    # 해당 위치에 방문했다고 체크해줌
                    check[ny][nx] = True
                    # 또 해당 위치에 대한 bfs 함수를 실행해야 하니까, 현재 위치를 queue에 저장해둠
                    q.append((ny, nx))
    return result

    
# 출력 요소인 그림의 개수 / 그림의 크기 0으로 기본설정
cnt = 0
maxv = 0

# 입력받은 배열의 세로, 가로만큼 돌아야 함
for j in range(N):
    for i in range(M):
        # 탐색을 할지 말지에 대한 기준 1. 해당 위치의 값이 1인가? 2. 해당 위치에 방문하지 않았는가?
        if board[j][i] == 1 and check[j][i] == False:
            # 탐색 조건을 통과했다면, 탐색한다는 뜻이니까 / 해당 위치에 방문 찍고 / 그림을 확인했으니 cnt 올리고 / 그림 사이즈 구하게 bfs로 해당 위치 돌려보기
            check[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)

# 알고리즘 스터디

# 1주차

> 2020.1.7 - 1.13 백준

[1월 7일 17822 원판 돌리기](./baek/17822.py)
[1월 8일 17837 새로운 게임 2](./baek/17837.py)

* 문제 풀이시 주의점

  * 말 4개여야만 한다.(x)

  * 4개 이상

  * 또한, 파란색일 때 반대방향으로 이동하게 되는데 만약 그 부분이 빨간색이면,

    빨간색으로 이동할 때 동작이 적용된다. 

* 틀렸습니다 (3%)

  * 함수의 중요성을 깨달았다.
  * 파란색과 경계선을 벗어날 때 같은 동작을 한다.
  * 함수 구현 대신 복붙으로 코딩했더니 실수를 하게 되었다.

* 5000줄의 코드가 나왔는데, 함수를 사용해서 줄여볼 수 있을 것 같다.

* 코드 리뷰

  * 다른사람 방식

1월 9일 게리맨더링 2
[1월 10일 주사위 윷놀이](./baek/17825.py)

* 실수

  ```python
  # 수정전
  visit[tmp]
  # 수정후
  visit[score[tmp]]
  ```

  * 직관적으로 생각하지 않기!
    * 항상 인덱스와 그 배열의 값이 무엇을 의미하는지 생각하면서 코딩하기
    * 이 실수로 30분 넘게 삽질하였다.

[1월 11일 연구소 3](./baek/17142.py)
[1월 12일 이차원 배열과 연산](./baek/17140.py)

* 정렬 조건

  * 1) 숫자 오름차순
  * 2) 횟수 오름차순

* 예시

  ```
  [3, 1, 1]
  정렬 [1, 1, 3]
  세기 (2, 1), (1, 3)
  정렬 (1, 3), (2, 1)
  바꾸기 [3, 1, 1, 2]
  ```

  ```
  [2, 1, 3, 1]
  정렬 [1, 1, 2, 3]
  세기 (2, 1), (1, 2), (1, 3)
  정렬 (1, 2), (1, 3), (2, 1)
  바꾸기 [2, 1, 3, 1, 1, 2]
  ```

* 풀이

  * 처음부터 100*100 리스트 선언하였다.
  
* 지영 방법

  ```python
  # BFS 부분
  		while tmp: # tmp Queue
              sec += 1 # sec 경과 시간
              if sec >= MIN: # 가지치기
                  return
              # ======== tmp 길이만큼 ========
              for _ in range(len(tmp)):
                  x, y = tmp.popleft()
                  for k in range(4):
                      tx, ty = x + dx[k], y + dy[k]
                      if -1 < tx < N and -1 < ty < N and board[tx][ty] != 1 and not visit[tx][ty]:
                          tmp.append((tx, ty))
                          visit[tx][ty] = 1
                          # cnt에 바이러스가 퍼진 방 개수 세기
                          if not board[tx][ty]:
                              cnt += 1
              # 빈 방의 개수와 바이러스가 퍼진 방 개수가 같으면 return
              if room == cnt: # room 초기 빈방 개수
                  MIN = min(MIN, sec)
                  return
          return
  ```

  * D 거리 배열을 사용하지 않고 sec 시간 단위로 BFS를 수행한다.
  * 또한 가지치기를 수행하였다.

# 2주차

> 2020.01.14 - 2020.01.20

* [1860. 진기의 최고급 붕어빵](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc)
  * [소스](./swea/1860.py)

* [17144. 미세먼지 안녕! ](https://www.acmicpc.net/problem/17144)
  * [소스](./baek/17144.py)

* [6808. 규영이와 인영이의 카드게임](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0&categoryId=AWgv9va6HnkDFAW0&categoryType=CODE)
  * [소스](./swea/6808.py)
  * 파이썬 불가
* [16985 Maaaaaaaaaze](https://www.acmicpc.net/problem/16985)
  * [소스](./baek/16985.py)

* [17143. 낚시왕](https://www.acmicpc.net/problem/17143)
  * [소스](./beak/17143.py)

다리 2 반례(https://www.acmicpc.net/board/view/41802)

무연이 방법

반례1 어떻게서든 연결되지 않는 경우 - 조건추가

```python
        if picked == sumCnt - 1:
            MIN = total
            break
```

반례2 같은 섬 연결하는 다리 만들어진경우

```python
[(2, 1, 1), (2, 1, 4), (2, 3, 5), (2, 4, 5), (2, 5, 5), (2, 5, 6), (3, 1, 5)]
[[0, 0, 1, 1, 1, 1, 1, 0],
 [1, 1, 1, 1, 1, 1, 0, 2],
 [0, 0, 0, 1, 0, 1, 0, 0],
 [3, 3, 0, 1, 1, 0, 4, 4],
 [0, 0, 1, 1, 0, 4, 4, 0],
 [0, 5, 0, 0, 0, 0, 0, 0],
 [5, 5, 5, 5, 0, 0, 6, 0],
 [5, 0, 0, 5, 5, 5, 0, 0],
 [5, 5, 0, 0, 0, 5, 5, 5],
 [5, 5, 5, 0, 0, 5, 0, 5]]
output: 10
correct answer: -1

```



다리 연결하는 부분 인접행렬로도 만들어보기





### 2105. [모의 SW 역량테스트] 디저트 카페

함수를 만들지 않아 복붙하다보니 생긴 실수로 1시간 이상 지체되었음

수정전 수정후

```python
if isPossible(nx, ny):
    tmp.append(board[nx][ny])
    visit[board[nx][ny]] = True
    
if isPossible(nx, ny):
    tmp.append(board[nx][ny])
    visit[board[nx][ny]] = True
```

1)결과값을 출력해보았을 때 `visit`에 False 표시가 잘 안된 것을 확인할 수 있었는데,

바로 False를 하는 부분을 중점적으로 보았다면 오래걸리지 않았을 것이다.

또한, 함수를 사용하는 습관을 길러야겠다...

2)복붙해서 쓴 함수 유의해서 보기!



디저트 카페 다른방법

up, down을 미리 정해두고 하는 방법을 해보자!

# 4주차

![:heavy_check_mark:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/google-medium/2714-fe0f@2x.png)백준

1. [Puyo Puyo](./baek/11559.py) [문제](https://www.acmicpc.net/problem/11559)

2. [두 동전](./baek/16197.py) [문제](https://www.acmicpc.net/problem/16197)

   * 백트래킹으로 보드를 전으로 돌리기가 힘들듯하다. ([백트래킹 미완성코드](./baek/16197_fail.py))
   * 백트래킹 풀기 전에 백트래킹 전후 처리가 간단한지 생각해보고 풀자!
   * 또한, 문제 크기를 보고 작으면 더 간단한 방법으로 풀 수 있을거라고 생각하자!
   * 총 10번 => 4^10 순열로 풀어보자
   * 시간이 너무 오래 걸린다
     * 갔던 자리를 한번 더 같다면 무한 반복 될 것이다.
     * visit 체크!
     * visit 체크하려니 처음부터 다시 풀어야할듯...

   * 해결
     * 답은 BFS 였다.
     * 

3. [탈출] [문제](https://www.acmicpc.net/problem/3055)

![:heavy_check_mark:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/google-medium/2714-fe0f@2x.png)SWEA

4. 2212 [모의 SW 역량테스트] 보호 필름
5. 5650 [모의 SW 역량테스트] 핀볼 게임
6. 2117 [모의 SW 역량테스트] 홈 방범 서비스
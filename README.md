# 알고리즘 스터디

## 1주차

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

## 2주차

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
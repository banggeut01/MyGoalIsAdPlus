# 알고리즘 스터디

# :star: ​1주차

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

[1월 9일 게리맨더링 2](./baek/17779.py) 다시 풀어보기!
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

# :star: 2주차

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
  
* [다리 만들기 2](https://www.acmicpc.net/problem/17472)

  * [소스](./baek/17472.py)

  * 다리 2 반례(https://www.acmicpc.net/board/view/41802)

    * 반례 1

      * 어떻게서든 연결되지 않는 경우 - 조건추가

      ```python
      if picked == sumCnt - 1:
          MIN = total
          break
      ```

    * 반례 2

      * 같은 섬 연결하는 다리 만들어진경우

      ```
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

      

  * 무연이 방법 :100: (**엄청나게 쉬운 최소신장트리**)

    * Prim

      * 제일 최소 가중치를 가진 다리를 선택한다.
      * 현재 선택된 간선 중 제일 작은 가중치 다리를 선택한다.
      * 싸이클을 만들지 않도록 위를 반복한다.
      * 싸이클을 판별하는 방법이 신박하였다. 

      ```
      정점 1 2 3 4 5
      선택 0 0 0 0 0
      
      (초기)
      정점 5개중 정점 3, 4를 잇는 최소가중치 간선을 선택하였다.
      선택한 정점은 1로 바뀐다.
      정점 1 2 3 4 5
      선택 0 0 1 1 0
      
      (반복)
      3, 4에 연결된 간선 중 최소 간선(정점 1-3)을 선택한다.
      정점 1 2 3 4 5
      선택 1 0 1 1 0
      이때 싸이클인지 아닌지 구별하는 방법은
      간선을 선택할 때 선택 0/ 선택 1 조합을 선택해야한다.
      선택 1을 두개 선택한다면 싸이클이 되기 때문이다.
      정말 신박하다
      
      모두 다 선택하고 끝!
      ```

      

반례1 

```python
        if picked == sumCnt - 1:
            MIN = total
            break
```

# :star: 3주차

* [1953. [모의 SW 역량테스트] 탈주범 검거](./swea/1953.py) / [문제](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

* [2105. [모의 SW 역량테스트] 디저트 카페](./swea/2105.py) / [문제](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

  * 함수를 만들지 않아 복붙하다보니 생긴 실수로 1시간 이상 지체되었음 

    * 실수를 줄이려면! :eyes: 

      ```python
      if isPossible(nx, ny):
          tmp.append(board[nx][ny])
          visit[board[ny][ny]] = True
          
      if isPossible(nx, ny):
          tmp.append(board[nx][ny])
          visit[board[nx][ny]] = True
      ```

    * 결과값을 출력해보았을 때 `visit`에 False 표시가 잘 안된 것을 확인할 수 있었는데,

      바로 False 처리 부분을 중점적으로 보았다면 오래걸리지 않았을 것이다.

      또한, 함수를 사용하는 습관을 길러야겠다!

    * **복붙해서 쓴 함수 유의해서 보기!**

  * 다른 정답에 비해 시간이 더 걸리는 편이다.

    * 한개씩 옮겨가며 백트래킹을 하였다.
    * 백트래킹 코드를 짤 때 어려움을 많이 느끼는 편이다.
    * 따라서 백트래킹을 하기 전에 이전 상태로 되돌려야 하는 과정이 까다로운지 따져보고 코딩하자!
    * 또한 백트래킹 진행시 너무 작은 크기로 진행한다면 미리 정할 수 있는 값이 있는지 찾아보고, 백트래킹이 아닌 한꺼번에 처리하도록 한다.
    * 이 문제에서는 두 변의 길이(up, down)를 먼저 정할 수 있다.
    * 이 때, 백트래킹을 쓰지 않아도 된다.



# :star: 4주차

![:heavy_check_mark:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/google-medium/2714-fe0f@2x.png)백준

1. [Puyo Puyo](./baek/11559.py) [문제](https://www.acmicpc.net/problem/11559)

   * 겨레 방법

     * move() 할 때

       ```
       1 1 , , 2 , 3 , , 1 일때
       tmp = [1, 1, 2, 3, 1]로 값 넣어두고
       board => 1 1 2 3 1 , , , , 로 업데이트
       ```

       

2. [두 동전](./baek/16197.py) [문제](https://www.acmicpc.net/problem/16197)

   * 백트래킹
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
     * 최단거리, 최단시간 문제
     * 현재에서 인접 4방향으로 이동을 한다.
     * 두 동전 좌표 조합이 갔던 곳이면 더 이상 갈 필요가 없다.
     * 4차원 `visit`

   * 만약 `백트래킹`으로 푸려면 백트래킹 함수의 인자로 두 동전의 좌표값을 함께 넘겨주면 된다.(나머지 사람들은 다 이렇게 풀었다.)

3. [탈출](./baek/3055.py) [문제](https://www.acmicpc.net/problem/3055)

   ```python
   # 1번시도 170
   elif w: # 물
       if board[nx][ny] == '.':
   # 2번 시도 180
   elif w: # 물
       # 비버가 이미 간곳은 가지 않아도 된다.
       if board[nx][ny] == '.' and not visit[nx][ny]:
   ```

   * 조건을 한번 더 걸러주었지만 시간이 조금 더 오래걸렸다.
   * 하지만 비버가 이미 간 곳은 물이 다시 갈 필요가 없다.
   * 물 먼저 이동하기 때문이다.

   

![:heavy_check_mark:](https://a.slack-edge.com/production-standard-emoji-assets/10.2/google-medium/2714-fe0f@2x.png)SWEA

4. [2112 [모의 SW 역량테스트] 보호 필름](./swea/2112.py)

   * 틀렸습니다 42/50
     * 문제를 잘못 읽었다. :cry:
     * 따라서 성능검사를 통과하기 위한 최소 약품투입 횟수는 2가 된다.  => 문제 전체에서 최소가 아닌 예제 [Fig.3]의 경우에 2라는 뜻이다.... 
   * 리턴 순서! 주의
   * 이러한 백트래킹 문제를 풀 때 가끔 순서가 헷갈릴 때가 있다.
   * 그땐 그래프를 그려보고 수행되는 명령문을 표시하면 순서를 정할 때 도움이 된다.

5. [5650 [모의 SW 역량테스트] 핀볼 게임](./swea/5650.py)
   
   * 지영 방법
     
     * 왔다 가는 것 모두 할 필요 없이 visit 체크를 한뒤 가기만 하면 왔던 길은 *2로 구할 수 있다.
     
   * 문제
     * board 값
       * 블록 1 ~5 일 때 진행 방향이 바뀐다.
       * 6~10일 때 웜홀로 빠지며 다른 웜홀로 나온다.
       * -1 블랙홀
     * 블록, 웜홀, 블랙홀 위치를 제외한 임의 위치에서 출발 (0에서)
     * 진행방향 임의
     * 최대 점수 구하기
       * 벽이나 블록에 부딪힌 횟수(진행방향이 바뀔 때)
       * 웜홀 통과는 포함 x
     * 게임은 출발위치로 돌아오거나 블랙홀에 빠질 때 끝나게 된다
       * 최초 위치 (visit로 시간 단축 가능)
         * 일단은 그냥 해본다. visit 체크시 반대방향을 체크해주어야한다.
       * 블랙홀
     
   * 풀이
     * 진행방향을 바꿀 때 dictionary를 이용하였다.
     * 진행방향과 블록에 따라 반대방향으로 바꿔주는 딕셔너리
     * 경계를 만났을 때도 역방향을 만들어주었다.
     * 딕셔너리 key는 튜플형태 (진행방향, 블록 번호)
     
* 틀렸습니다.
  
  * 가장자리에서 시작할 때 범위를 넘어서는 방향부터 시작하는 것은 답이 될 수 없다.
  
     * <del>board에서 0이 아닌 가장자리를 블록 5로 바꿔준다.</del>
  * 출발할 때 경계를 넘어가는 지점이면 go()함수를 실행하지 않았다.
  
* 제한시간 초과 28/50
  
     * board 숫자 조건 검사 if문의 순서를 바꿔봐도 같다.
     
     * 게임은 반드시 종료된다 => **처음으로 돌아오지 않고 무한루프를 도는 경우는 없다**
     
       * `visit` 삭제 후 확인 결과, 무한루프를 돌고 있었다.
       * 경계에서 d 갱신 후, 그 위치가 웜홀 또는 또는 블럭일 때 또 한번 처리해야한다. 
     
     * 또 다른 무한루프가 돌았다.
     
       * 웜홀이 분명 한쌍이라고 했는데
     
         ```
         {(6, 9, 2): (4, 8), 
         (6, 4, 8): (6, 6), 
         6: (4, 8), 
         7: (0, 8), 
         (7, 7, 6): (0, 8), 
         (6, 2, 4): (4, 8), 
         (7, 0, 8): (7, 6), 
         (6, 6, 6): (4, 8)}
         ```
     
         6인 웜홀이 무려 네개..
     
       * 확인해보니 `hall` 변수 선언을 `for tc in range(T)` 밖에서 해주었다....
     
       * 이런 실수는 다시 하지 말자!!!:angry:
     
* 틀렸습니다. 47/50
  
  * 경계에서 이동할 때 문제가 있는 것 같다.
  
  * 모범 답안에서는 경계를 5로 바꾸라고 했지만,
  
    나는 그 방법이 잘 이해가지 않는다. 지금도.
  
  * **경계를 벗어날 때 다시 돌아가므로 cnt 값은 (현재 cnt*2 + 1)개가 된다.**
  
  * 코드가 더러워질 때 그 길이 아닌 것 같다는 생각이 들면 다시 생각해보아야 한다. 
  
6. [2117 [모의 SW 역량테스트] 홈 방범 서비스](./swea/2117.py)

   * 승열 방법
     * 범위 안에 있는지 없는지 검사할 때는 중심 좌표 x, y와 k값만 알면 알 수 있다.
     * **집과 중심과의 거리**를 구하면 된다.

# :star: 5주차

> 02.04 ~ 02.10 

:heavy_check_mark: 백준

* [2529. 부등호](./baek/2529.py) / [문제](https://www.acmicpc.net/problem/2529)

  * 틀렸습니다.

    * MIN 값 초기화를 잘못했다.

      ```python
      >>> 0xffffff
      16777215 # 98765432보다 작다.
      ```

      아래와 같이 초기화

      ```python
      MAX, MIN = 0, 9999999999
      ```

  * **python** 으로 제출하면 **시간초과**

    * 10개 순열을 다 구해준 후 답이 되는지 확인하였다.
    * **백트래킹**으로 다시 풀어보기!

  * 승열, 겨레 방법

    * 작은 값부터 하면 min 값 정답 찾고 끝!
    * 큰 값부터 하면 max 값 정답 찾고 끝!

  * 새로운 팁)

    * 문자열이더라도 숫자로만 된 string 형이면 대소 비교 된다.

    * 주의!

      ```python
      >>> a = '9'
      >>> b = '10'
      >>> a < b
      False
      ```

      * 길이가 다를 땐 쓰면 안된다!

* [3987. 보이저 1호](./baek/3987.py) / [문제](https://www.acmicpc.net/problem/3987)

* [2174. 로봇 시뮬레이션](./baek/2174.py) / [문제](https://www.acmicpc.net/problem/2174)

  * test case

    ```
    Input
    5 4
    2 2
    1 4 E
    5 4 W
    1 F 3
    2 F 1
    
    output
    Robot 2 crashes into robot 1
    
    3 3
    1 9
    2 2 W
    1 F 1
    1 L 1
    1 F 1
    1 L 1
    1 F 2
    1 L 5
    1 F 2
    1 R 3
    1 F 2
    
    정답 : OK
    ```

    

:heavy_check_mark: SWEA

* [5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션](./swea/5648.py) 
  
  * bfs로 풀어보겠다
  * 지영이 방법
    * dictionary 사용
    * x, y좌표 키, 방향, 에너지는 value
    * for문 4000번만 돌렸다.
    * dict은 for문을 통해 key, value 값 사용할 수 있다.
    * 업데이트 되는 것은 tmp에 담아둔다음!
  * 어려웠던 이유
    * x, y가 반대로 주어짐
    * 상, 하 방향 주의! 하 방향은 x값이 증가하는 것이 아닌 감소하는 방향
    * 하: (-1, 0), 상: (1, 0)
  
* [2382. [모의 SW 역량테스트] 미생물 격리](./swea/2382.py)  지영이 방법으로 **다시** 풀어보기!

  * 틀렸습니다.

    ```python
    # 수정전
    for i in board[x][y]:
        if maxM != micro[i]:
            die[i] = True
            liveCnt -= 1
            board[x][y].remove(i)
            else:
                micro[i] = tmp   
    
    # 수정후
    dieTmp = []
    for i in board[x][y]:
        if maxM != micro[i]:
            die[i] = True
            liveCnt -= 1
            dieTmp.append(i)
            else:
                micro[i] = tmp
                for i in dieTmp:
                    board[x][y].remove(i)
    ```

    * `board[x][y].remove(i)` 이런 명령어를 실행할 때 `for문` 에 영향을 미치지 않는지 꼭 확인하기!
    
  * 지영이 방법

    * 원자 풀 때랑 비슷
    * dictionary 이용
    * key = > 좌표, value => 미생물수랑 방향

* [5644. [모의 SW 역량테스트] 무선 충전](./swea/5644.py) 

  * 틀렸습니다.

    ```python
    # 수정전
    if len(board[ax][ay]) and len(board[bx][by]):
        for a in board[ax][ay]:
            for b in board[bx][by]:
                if a == b:
                    tmp = max(tmp, P[a] // 2) # 실수
                else:
                    tmp = max(tmp, P[a] + P[b])
                        # 수정후
    if len(board[ax][ay]) and len(board[bx][by]):
        for a in board[ax][ay]:
            for b in board[bx][by]:
                if a == b:
                    tmp = max(tmp, P[a])
                else:
                    tmp = max(tmp, P[a] + P[b])
    ```

  * 무선충전이 가능한지 검사할 때,
  
    홈 방범 서비스처럼 거리만 구해서 검사할 수 있음!

#  :star: 6주차

:heavy_check_mark: SWEA

[2383. [모의 SW 역량테스트] 점심 식사시간](./swea/2383.py)

* 학생을 두 그룹으로 나눔(계단 1그룹, 계단 2그룹)

* 계단 내려갈 수 있는 시간을 먼저 계산

  * |학생 위치 ~ 계단 위치 | + 1

* 도착시간을 계산

  * 현재 학생의 출발시간이 세번 전에 출발한 학생의 도착시간보다 같거나 클때 출발 가능하다.
  * 만약 작을 경우 `세번 전에 출발한 학생의 도착시간 - 현재 학생 출발시간` 만큼 기다렸다가 출발해야한다.

* 예시

  ```
  계단을 내려갈 수 있는 시간
  g1 = [3, 4, 5, 6, 7, 9]
  g2 = [3, 4, 4, 8, 8, 8]
  
  도착시간 (계단 내려가는데 걸리는 시간 g1 => 3, g2 => 5 일 때)
  g1 = [6, 7, 8, 9, 10, 12]
  g2 = [8, 9, 9, 13, 13 + 1, 13 + 1, 13 + 5]
  ```

  * g2 그룹의 다섯번째 학생은 두번째 학생이 도착해야 출발할 수 있다.
  * 출발시간 + 계단 내려가는데 걸리는 시간 + **기다리는 시간(10 - 9 = 1초)**

[5658. [모의 SW 역량테스트] 보물상자 비밀번호](./swea/5658.py)
[5656. [모의 SW 역량테스트] 벽돌 깨기](./swea/5656.py)

* 틀렸습니다!

  * 실수 그만하자!
  * 답이 계속 크게 나온 것을 확인 -> 보드를 직접 찍어보니 벽돌이 깨지긴 깨지나 너무 적게 깨지는 것을 발견!
  * 1보다 큰 값을 가진 벽돌이 안깨진지 의심
  * dq안에 제대로 값이 안들어간 것을 확인!
  * 그 주변 코드를 봐야했다.
  * 하지만 디버깅을 30분이나 하였다.
  * 밑에와 같은 실수로....

  ```python
  # 수정전
  x, y, val = dq.popleft()
  for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1): # 네 방향에 대해
      idx = 1
      # 벽돌의 숫자만큼 벽돌을 없앰
      while idx < val:
          nx, ny = x + dx, y + dy
          ...
  
  # 수정후
  x, y, val = dq.popleft()
  for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1): # 네 방향에 대해
      idx = 1
      nx, ny = x, y # -> 수정
      # 벽돌의 숫자만큼 벽돌을 없앰
      while idx < val:
          nx, ny = nx + dx, ny + dy # -> 수정
          ...
  ```

  * x, y값은 고정이기 때문에 nx, ny값을 계속 업데이트 해주어야 했다.
  * 다신 이런 실수 하지 않기!
  * 하더라도 얼른 찾아내기!

[4130. [모의 SW 역량테스트] 특이한 자석](./swea/4130.py)
[4131. [모의 SW 역량테스트] 활주로 건설](./swea/4131.py)

* 현재 지형이 전보다 1개 높아졌거나 낮아졌을 경우에 그 위치만 검사하면 된다.

* 틀렸습니다. (43/50)

  * visit 체크하는 부분에서 빠뜨린 부분이 있었다.

    ```python
    def isPossible(x, y, d, prev):
        dx, dy = d
        visit[x][y] = True # --> 이 부분 추가하였음
        for _ in range(X - 1):
            x, y = x + dx, y + dy
            if -1 < x < N and -1 < y < N and board[x][y] == prev and not visit[x][y]:
                visit[x][y] = True
            else: return False
        return True
    ```

  * 활주로 건설 길이는 `X`인데 `X-1`길이만 검사하게 하였다.

  * 이때 visit 체크를 `X`만큼 해야하는데 `X-1`만큼해서 오답이 되었다.

  * visit 변수 사용시 이점을 주의하자!

  * 어느 부분을 체크해야하는지 빠뜨린 부분은 없는지!

[5653. [모의 SW 역량테스트] 줄기세포 배양](./swea/5653.py)



# :star: 7주차

> 출제 : 무무

[백준 1062. 가르침](./baek/1062.py) / [문제](https://www.acmicpc.net/problem/1062)

[백준 1038. 감소하는 수](./baek/1038.py) / [문제](https://www.acmicpc.net/problem/1038)

* 틀렸습니다.
  * 반례 input: 1022 / answer: 9876543210 / output: -1
  * **N은 1,000,000보다 작거나 같은 자연수 또는 0이다.**
    * 감소하는 수가 1,000,000 이하라는 뜻이 아니다.
    * `comp()`에서 재귀 종료 조건을 재귀깊이가 6일 때로 해주었다. # <- 잘못된 점
    * 위 조건 빼주는 것으로 해결!

[백준 17281. 야구공](./baek/17281.py) / [문제](https://www.acmicpc.net/problem/17281)

* 시간초과
* 해결 놉!

[백준 17136. 색종이 붙이기](./baek/17136.py) / [문제](https://www.acmicpc.net/problem/17136)

* 시간초과

  * 안써도 되는 `visit`를 썼음
  * `board`값을 0(visit True) / 1(visit False) 로 바꾸는 것으로 업데이트 하였다.

* 옛날 코드를 보면 속도가 훨씬 빠르다.

  * `board`를 순회할 때 한칸씩 가면서 재귀를 호출하는게 아니라 for문으로 현재행부터 1인 `board[i][j]`값을 만나면 재귀를 호출하게 짰었다.

  * [다시 짠 코드](./baek/17136_2.py) --> 시간 더 걸림... Why?? 

    * flag의 역할

      ```python
      # 한 자리에 색종이 1 ~ 5 크기를 두고 난 후, for문을 계속 돌리면 안된다.
      # 바로 return 시켜야함!
      flag = False
      for i in range(r, 10):
          for j in range(10):
              if board[i][j]:
              #    ...
              if flag: return
      ```

      

  * [옛날 코드](https://github.com/banggeut01/algorithm/blob/master/code/A/17136.py)

[프로그래머스 올바른 괄호] / [문제](https://programmers.co.kr/learn/courses/30/lessons/12929)

[프로그래머스 [2020카카오공채] 가사 검색] / [문제](https://programmers.co.kr/learn/courses/30/lessons/60060)

# :star: 8주차

:heavy_check_mark: SWEA Python A 대비반

[4008. [모의 SW 역량테스트] 숫자 만들기](./swea/4008.py)

[1952. [모의 SW 역량테스트] 수영장](./swea/1952.py)

[1861. 정사각형 방](./swea/1861.py) [선생님 풀이](./swea/1861_teacher.py)

* 한번 갔던 블럭은 더 갈 필요가 없음

* 블럭의 이동 개수를 저장하는 2차원 리스트 `D`사용

* 제한시간 초과

  * `visit` 리스트를 매번 새로 선언해서 사용했으나, 백트래킹이기 때문에 그럴 필요가 없다.

  * :rainbow: 새로 변수를 할당하는 것만으로도 시간초과가 날 수 있다는 것을 배우게 되었다.

  * 해결

    ```python
    # 수정전
    for i in range(N):
        for j in range(N):
            visit = [[False] * N for _ in range(N)]
            visit[i][j] = True
            initX, initY = i, j
            back(i, j, 1)
    
    # 수정후
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            visit[i][j] = True
            initX, initY = i, j
            back(i, j, 1)
            visit[i][j] = False
    ```

  * 선생님 풀이

    * visit를 1 ~ N*N 만큼 선언해주고,

    * 새로운 좌표를 방문할 때 그 숫자에 1을 넣어준다.

    * 만약 2, 3, 4를 방문한다면

      ```
      N = 3
      visit (0 ~ 9)
      0, 0, 0, 1, 1, 0, ..., 0
      ```

    * 만약 5, 6을 방문한다면

      ```
      visit (0 ~ 9)
      0, 0, 0, 0, 0, 0, 1, 0, ..., 0
      ```

    * 결과적으로

      ```
      visit (0 ~ 9)
      0, 0, 0, 1, 1, 0, 1, 0, ..., 0
      ```

      위와 같은 visit가 된다.

    * 이 때 연속한 1의 개수 + 1이 제일 긴 값이 답이된다.

[2819. 격자판의 숫자 이어 붙이기](./swea/2819.py)

[3752. 가능한 시험 점수](./swea/3752.py)

:heavy_check_mark: SWEA Python A+ 대비반

[5658. [모의 SW 역량테스트] 보물상자 비밀번호](./swea/5658_2.py)

[1953. [모의 SW 역량테스트] 탈주범 검거](./swea/1953_2.py)

[4012. [모의 SW 역량테스트] 요리사](./swea/4012.py)

[5656. [모의 SW 역량테스트] 벽돌 깨기](./swea/5656_2.py)

[1949. [모의 SW 역량테스트] 등산로 조성](./swea/1949_2.py)



:heavy_check_mark: 백준

[2589. 보물섬](./baek/2589.py) / [문제](https://www.acmicpc.net/problem/2589)

* 재채점 결과 틀렸습니다.
* 

dictionary 알아둘 점!

```python
a = {1: 1, 2: 2}
for x in a:
...    print(a.pop(x)) 
...    
1
Traceback (most recent call last):
  File "<input>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
```

* 딕셔너리 키로 접근시 딕셔너리 원소 값을 빼거나 삽입할 수 없다.
* 따라서 queue로서 사용시에 새로운 dictionary를 선언해서 업데이트하는 것이 낫다.

* deque나 list는 아래와 같이 가능하다.

```python
for _ in range(len(dq)): # for문 시작될 때 길이가 정해진다. => 고정
    dq.popleft()
    if isPossible():
        dq.append(example)
```



# :star: 9주차

> 2020-03-30 ~ 

:heavy_check_mark: Line Plus 대비 

[배열합치기](https://level.goorm.io/exam/43250/%EB%B0%B0%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0/quiz/1)

[다익스트라 알고리즘(Dijkstra's Algorithm)](https://level.goorm.io/exam/43211/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-dijkstra-s-algorithm/quiz/1) [코드](./goorm/dijkstra.py)

* [유튜브 - 다익스트라 알고리즘](https://www.youtube.com/watch?v=611B-9zk2o4)

* 방법

  * 무무 프림 방법(2주차 다리 만들기 2)으로 풀어보자!

  * 양방향 그래프

  * 같은 두 노드를 잇는 간선이 두개 이상 존재할 수도 있다.

    -> 입력으로 받으면서 최소값으로 업데이트!

[2개의 계란](https://level.goorm.io/exam/43260/2%EA%B0%9C%EC%9D%98-%EA%B3%84%EB%9E%80/quiz/1) 아직 못품!!!

* 복잡하게 생각하지 말아보자
* 밑에 층에서부터 차례대로 올라가며 답 갱신!
* 만약 깨졌을 경우 or 깨지지 않았을 경우
* 재귀 호출해보기
* 2개 다 깨졌을 경우 return!

:heavy_check_mark: 백준

* [스티커 붙이기](https://www.acmicpc.net/problem/18808) [코드](./baek/18808.py)

* [Gaaaaaaaaaarden](https://www.acmicpc.net/problem/18809) [코드](./baek/18809.py) 꼭 한번 다시 풀어보기!!! :rainbow_flag:

# :star: 10주차

:heavy_check_mark: 프로그래머스 2019 카카오 개발자 겨울 인턴십

* [64062. 징검다리 건너기](./prog/64062.py)

* [42841. 문자열 압축](./js/42841.js)

  * 5번 테스트케이스 틀림

    ```JS
    var answer = 0xffffff // 수정전
    var answer = s.length; // 수정후
        for (var i = 1; i <= parseInt(s.length / 2); i++) {
            ...
        }
    ```

    * 문제점 ) 수정 전 s값을 길이가 1인 문자열로 주게되면 답이 0xffffff이 나오게 된다.
    * 원인 ) for문에서 `s.length / 2` 이기 때문이다.
    * 해결법 ) 초기값을 `s.length`로 준다.

:heavy_check_mark: 백준

[1932. 정수 삼각형](./baek/1932.py)

[2151. 거울 설치](./baek/2151.py) :100:

* 풀이
  * BFS
  * 3차원 배열 선언 `dist[x][y][d]` : x, y좌표에서 설치한 거울의 갯수
  * `visit` 배열은 따로 선언해주었음

* 예제)

  [테스트케이스](https://www.acmicpc.net/board/view/34260)

```
7
!!..!.#
*.....*
.!..!..
!!*.!.!
.*!!.*!
...!!..
!*#****
Answer: 5
```

* 문제 원인
  * 한번 갔던 곳 다시 못가게 했음
  * 하지만 거울로 갔던곳 직진으로 다시 갈 수 있음
  * 조건을 추가해주어야 한다.
  * (`not visit[x][y][d]` or `dist[nx][ny][d] > dist[x][y][d]`) 

[2579. 계단 오르기](./baek/2579.py)

* [실패 코드](./baek/2579_fail.py)
  * `memoization` 방식 사용하였음
  * 계단을 오르면서 `memo` 갱신
  * 두번 연속 올랐을 때 두칸을 오르게 하였음
  * 문제점 
    * `연속으로 한칸씩 오른 횟수`를 고려하지 않음
    * 한번 연속으로 올랐을 때 `memo`, 연속으로 오르지 않았을 때 `memo`를 구분하지 않았음!
  * 해결)
    * `memo`를 이차원으로 선언
    * `memo[k][cnt]` : k계단에서 최대합(cnt:1이면 한칸 가능!, 0이면 두칸만!)

[1938. 통나무 옮기기](./baek/1938.py) :imp::imp::imp:

* dfs 실패 
* 최소거리 -> BFS
* `한번 갔던 좌표와 방향` 다시 안가도 된다! **왜?**
* 거울 설치랑 다른것이 무엇인가??
  * 거울 설치는 최소거리 문제가 아니었음
  * 설치 거울 개수 최소화.. 
  * 따라서 같은 좌표, 방향이더라도 거울 설치 개수에 따라 다시 갈 수 있었음..
  * 예를 들어 거울을 설치하여 빛이 지나가게 한 자리를 거울을 설치하지 않고도 다시 올 수 있음!!!! 그래서 `dist`갱신을 했음
  * 하지만 여기선 `dist`가 `-1`인 좌표, 방향(아직 방문하지 않은 곳)만 방문하면 되는거임  

```
4
000E
BBBE
000E
0000
answer: 3

4
0B00
EB00
EB00
E000
answer: 2

4
BBB0
0E00
0E00
0E00
answer: 3

5
B0011
B0000
B0000
11000
EEE00

답 : 9

5
B0011
B0000
B0000
01000
EEE10

답 : 0


7 
0001000 
0001000 
B00100E 
B00000E
B00100E 
0001000 
0001000

답 : 8

13
0000000000BBB
0000000000000
0000000000000
0000000000000
0000000000000
0000000000000
0000000000000
0000000000000
0000000000000
0000000000000
EEE0000000000
0000000000000
0000000000000
answer: 20
```



[6087. 레이저 통신](./baek/6087)

[9019. DSLR](./baek/9019.py)

* [DFS](./baek/9019_fail.py) -> 실패 
* BFS로 풀어본다



# :star: 11주차 

:heavy_check_mark: 백준

[2468. 안전 영역](./baek/2468.py)

* 런타임 에러

  ```python
  import sys
  sys.setrecursionlimit(10000)
  ```

  위를 추가해주니 통과

  `recursion error`의 경우에도 `런타임 에러`가 뜸

[9328. 열쇠](./baek/9328.py)

* 풀이
  * 초기 큐
    * 경계값에서 `.`, `키(a~z)`, `문서($)`, `문(A~Z)`인 경우 초기 큐에 넣기
    * 만약 키를 만나면 키에 해당하는 문열기
    * 문을 만나는 경우 일단 큐에 넣기
    * 문이 빠져나가는 경우는 문이 열려 그 자리가 `.`이 되었을 때

# :star: 12주차 

:heavy_check_mark: 백준 - 삼성 SW 역량 테스트 기출

[15684. 사다리 조작](./gogoss/15684.py)

*  문제 제대로 이해하기

  * i번에서 출발하여 i번에서 도착해야한다.
  * 이때 i번은 모든 세로줄을 의미함
  * 사다리를 갱신하면서 답이 되는지 안되는지 확인해본다.

* 시간초과!

  * 모든 사다리를 다 놓은 다음에 답인지 확인하였음
* 그렇게 하지말고 지금 상태에서 답이 아니면
  * 다음 사다리 업데이트해가면서 답 확인해본다.
* 현 상태에서 사다리를 놓고 안놓는다 => x
  * 현 상태에서 답이 아니면 사다리를 놓아본다!

  * x, y 변경때마다 답인지 확인하지말고,
* board에 변화가 있을때만 답인지 확인하기!

[15685. 드래곤 커브](./gogoss/15685.py)

[17837. 새로운 게임 2](./gogoss/17837.py)

[17779. 게리맨더링 2](./gogoss/17779.py)

* 각각의 선거구 수를 다 구해주었는데 5는 구하기 힘들다.
* 1~4 선거구까지 구한 후 전체로부터 5를 구한다.

[17142. 연구소 3](./gogoss/17142.py)

* 답 틀릴때 조건문 제대로 썼는지 확인하기

```python
# 0이거나 2이다. 1과 3이 아니다.
# 수정전
not B[nx][ny] and B[nx][ny] != 3
# 수정후
B[nx][ny] != 1 and B[nx][ny] != 3
not B[nx][ny] or B[nx][ny] != 3
```

[17140. 이차원 배열과 연산](./17140.py)

[17143. 낚시왕](./gogoss/17143.py)

* dictionary 꺼낼때 pop, for key, val 접근시 items()잊기 말기

[17144. 미세먼지 안녕!](./gogoss/17144.py)

[16236. 아기 상어](./gogoss/16236.py)

[16235. 나무 재테크](./gogoss/16235.py)

* 실수 ) 선후 관계 조심하기

```python
# 수정전
board[i][j][idx] += 1
food[i][j] -= board[i][j][idx]

# 수정후
food[i][j] -= board[i][j][idx]
board[i][j][idx] += 1
```



[16234. 인구 이동](./gogoss/16234.py)



# :star: 13주차 

:heavy_check_mark: 프로그래머스

> DFS / BFS

[43165. 타겟 넘버](./prog/43165.py) / [문제](https://programmers.co.kr/learn/courses/30/lessons/43165)

[43162. 네트워크](./prog/43162.py) / [문제](https://programmers.co.kr/learn/courses/30/lessons/43162)

[43163. 단어 변환](./prog/43163.py) / [문제](https://programmers.co.kr/learn/courses/30/lessons/43163)

:heavy_check_mark: 백준

[19238. 스타트택시](./baek/19238.py)

* 런타임 에러

  `collections`를 `_collections`로 잘못 씀

* 틀렸습니다.

  * 문제를 잘 읽자!
    * 같은 거리인 경우, 행, 열 작은 순위!
  * 목적지로 도착하지 못하는 경우를 처리해주지 않음
    * 조건 추가

  ```python
  # 전
  if dist > G: break
  # 후
  if dist2 == -1 or dist > G: break
  ```

  
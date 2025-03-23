# INSIGHT
### 10951
- 어떻게 랜덤으로 정해진 갯수를 입력받을 수 있는가?
    - 내 풀이
        - While문 + try-except문
    - 다른 풀이
        - sys.stdin으로 입력이 끝날 때까지 받기
            - 덧붙여, readlines()로 전체 한번에 받기
        - open(0)으로 입력이 끝날 때까지 받기
        - sys.stdin == open(0)
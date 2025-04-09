## INSIGHT
### [2751](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/2751.py)
- Python 속도가 느릴 때 해결 방법
    - Pypy3로 바꿔본다.
    - input 대신 sys.stdin.readline을 사용한다.

### [2164](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/2164.py)
- Deque
    - 앞, 뒤에서 자유롭게 빼고 쓸 수 있는 자료구조!

### [18110](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/18110.py)
- python의 round 함수 특징
    - 오사오입임
        - 5미만은 버림, 5초과에서 올림.
        - 5의 경우 앞자리가 짝수면 버리고, 홀수면 올림
        - 소수점 자리가 2개이상이면 그거 따라감
        - ex) round(2.5) = 2, round(3.5) = 4
        - ex) round(2.55) = 3
    - 그럼 사사오입의 특징은?
        - 4이하는 버림, 5이상은 올림
- 실제로 수학적인 반올림은?
    - math.floor(x + 0.5)

### [10816](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/10816.py)
- 뭔가를 찾을 때, Dictionary를 이용하면 O(1)이다!
    - 굳이 이분탐색 안하고 Dictionary를 사용하면 되었다...
    - Key-Value 쌍을 잘 기억하자!

### [1929](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/1929.py)
- 소수를 판단하는 방법?
    - 에라토스테네스의 체
        - 루트값까지의 수를 하나씩 체크하면서 거른다!
    - 어쨌든 핵심은 루트값을 생각해보자는 것!

### [1654](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/1654.py)
- 나무 자르기 문제!
    - 최소, 최대 중 이진 탐색으로 max값 찾기!

### [2108](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/2108.py)
- Dictionary 활용
    - items(), keys(), values() 잘 사용하기!

### [1463](https://github.com/lxxhanx/study/blob/main/codetest/boj/2_silver/1463.py)
- DP 만들 때, 굳이 append 쓸려고 하지 말자... 헷갈린다.
    - 그냥 리스트를 1-n까지 사용하자... ㅎㅎ
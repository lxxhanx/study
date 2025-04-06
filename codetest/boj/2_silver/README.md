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
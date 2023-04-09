### input 파일 만들어서 불러오기
import sys
sys.stdin = open('input', 'r')


### collections.Counter() 모듈 사용
string에 있는 알파벳 개수 딕셔너리로 세어줌

```
import collections
c = collections.Counter(string)
```

### ord(문자)
하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
ord('a')를 넣으면 정수 97을 반환

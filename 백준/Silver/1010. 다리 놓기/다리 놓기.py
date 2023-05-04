def factorial(num):
    answer = 1
    if num == 1:
        return answer
    else:
        for i in range(2, num+1):
            answer *= i
        return answer

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(int(factorial(m)/(factorial(m-n)*factorial(n))))
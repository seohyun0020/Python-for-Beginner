print("하하하")
print(200 + 100)
print("200 + 100")
print(int("200") + 100)


var1 = input()
var2 = input()
result = var1 + var2
print(var1, "+", var2, "=", result)


var1 = int(input())
var2 = int(input())
result = var1 + var2
print(var1, "+", var2, "=", result)

var1 = int(input())
var2 = int(input())
result = var1 * var2
print(var1, "*", var2, "=", result)

# 7 정수 2개를 입력받아서 더하기, 곱하기, 제곱 연산을 하는 프로그램을 작성하시오

print(int(input("숫자 1 입력 : ")))
print(int(input("숫자 2 입력 : ")))

var1 = int(input("숫자 1 입력 : "))
var2 = int(input("숫자 2 입력 : "))
result1 = var1 + var2
result2 = var1 * var2
result3 = pow(var1, var2)
print(var1, "+", var2, "=", result1)
print(var1, "*", var2, "=", result2)
print(var1, "^", var2, "=", result3)

var1 = int(input("숫자 1 입력 : "))
var2 = int(input("숫자 2 입력 : "))
print(var1, "+", var2, "=", var1 + var2)
print(var1, "*", var2, "=", var1 * var2)
print(var1, "^", var2, "=", pow(var1, var2))

# 변수의 선언과 사용

boolVar = True
intVar = 0
floatVar = 0.0
strVar = ""


boolVar, intVar, floatVar, strVar = True, 0, 0.0, ""

type(boolVar), type(intVar), type(floatVar), type(strVar)

# 2 변수의 사용

boolVar = False
intVar = 100
floatVar = 123.45
strVar = "안녕?"

var2 = 200
var1 = var2

var1 = 100 + 100

var1 = var2 + 100

var1 = var2 = var3 = var4 = 100
var4 = 100
var3 = var4
var2 = var3
var1 = var2

var1 = var1 + 200

noVar = 0
noVar = noVar + 200


myVar = 100 #정수형 변수를 생성(국 그릇 생성)
type(myVar) #<class 'int'>출력
myVar = 100.0 #이 순간에 실수형 변수로 변경(밥 그릇으로 변경)
type(myVar) #<class 'float'>출력

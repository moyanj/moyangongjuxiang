#库导入
import turtle as t
t.left(90)
#伞面
t.pensize(4)
i = 0
t.pencolor("steelblue")
t.fillcolor("skyblue")
t.begin_fill()
x = t.xcor()
while i < 180:
    t.forward(2)
    t.right(1)
    i = i+1
x2 = t.xcor()
t.end_fill()
t.goto(0,0)
#伞边
yuan_num = 6
yuan_bj = x2/yuan_num/2
i = 1
while i < yuan_num*2:
    t.goto(yuan_bj*i,0)
    t.pencolor("steelblue")
    t.dot(yuan_bj*2)
    t.forward(5)
    t.pencolor("white")
    t.dot(yuan_bj*2)
    i = i+2
#伞兵
t.goto(x2/2,0)
t.pencolor("steelblue")
t.forward(110)
t.pensize(10)
t.forward(20)
#结尾
t.done()

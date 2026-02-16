import turtle,time,random
delay=0.1
wn=turtle.Screen()
wn.title("Snake Xania by Ramani")
wn.bgcolor('light green')
wn.setup(width=600,height=600)
wn.tracer(0)
#Create Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.goto(0,0)
head.penup()
head.direction='stop'
#set up food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('white')
food.penup()
food.goto(random.randint(-290,290),random.randint(-290,290))
#Score
score=0
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(160,250)
pen.shape('square')
pen.write(f"SCORE:{score}",align='center',font=('courier',24,'normal'))#we can take bold also
def up():
    if head.direction!='down':
        head.direction='up'
def down():
    if head.direction!='up':
        head.direction='down'
def right():
    if head.direction!='left':
        head.direction='right'
def left():
    if head.direction!='right':
        head.direction='left'
wn.listen()
wn.onkeypress(up,'Up')
wn.onkeypress(down,'Down')
wn.onkeypress(right,'Right')
wn.onkeypress(left,'Left')

body=[]
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
while True:
    wn.update()
    pen.hideturtle()
    if head.xcor()>290 or head.ycor()>290 or head.xcor()<-290 or head.ycor()<-290:
        time.sleep(2)
        head.direction='stop'
        head.goto(0,0)
        for i in body:
            i.goto(1000,1000)
        body.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write(f"SCORE:{score}",align='center',font=('courier',24,'normal'))
    if head.distance(food)<20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        new_body=turtle.Turtle()
        new_body.speed(0)
        new_body.shape('square')
        new_body.color('black')
        new_body.penup()
        body.append(new_body)
        score+=1
        delay-=0.01
        pen.clear()
        pen.write(f"SCORE:{score}",align='center',font=('courier',24,'normal'))
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()
    for i in body:
        if i.distance(head)<20:
            time.sleep(2)
            head.direction='stop'
            head.goto(0,0)
            for i in body:
                i.goto(1000,1000)
            body.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write(f"SCORE:{score}",align='center',font=('courier',24,'normal')) 
            
    time.sleep(delay)

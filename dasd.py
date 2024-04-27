from flask import Flask, render_template_string, request
import turtle
import time
app = Flask(__name__)





def heart1(h):
    return 15 * math.sin(h) ** 3

def heart2(h):
    return 12 * math.cos(h) - 5 * math.cos(2 * h) - 2 * math.cos(3 * h) - math.cos(4 * h)


import math
import turtle
def  draw_birthday_card():
    turtle.shape("turtle")
    turtle.setup(width=900, height=700)
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.color('red')

    turtle.hideturtle()
    # Draw large heart shape
    turtle.penup()
    turtle.goto(heart1(0) * 20, heart2(0) * 20)
    turtle.pendown()

    for i in range(400):
        x, y = heart1(i) * 20, heart2(i) * 20
        turtle.goto(x, y)

    # Draw "name"
    turtle.penup()
    turtle.goto(0, 35)
    turtle.pendown()
    turtle.write("chadolf", align='center', font=('Arial', 30, 'bold'))

    # Draw small heart inside the large heart
    turtle.penup()
    turtle.goto(heart1(0) * 20, heart2(0) * 20 - 100)
    turtle.pendown()


    for i in range(300):
        x, y = heart1(i) * 10, heart2(i) * 10 - 100
        turtle.goto(x, y)

    # Draw even smaller heart inside the small heart
    turtle.penup()
    turtle.goto(heart1(0) * 20, heart2(0) * 20 - 150)
    turtle.pendown()

    for i in range(200):
        x, y = heart1(i) * 5, heart2(i) * 5 - 150
        turtle.goto(x, y)

    # Draw nano heart inside the even smaller heart
    turtle.penup()
    turtle.goto(heart1(0) * 20, heart2(0) * 20 - 180)
    turtle.pendown()

    for i in range(150):
        x, y = heart1(i) * 2, heart2(i) * 2 - 180
        turtle.goto(x, y)

    # Draw "I Love You"
    turtle.penup()
    turtle.goto(0, 243)
    turtle.pendown()
    turtle.write("tavalodet mobark", align='center', font=('Arial', 40, 'bold'))

    turtle.done()
    turtle.exitonclick()

@app.route('/')
def index():
    return render_template_string('<html><head><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script></head><body><h1> <a href="#" id="startDrawing">here tavalodet mobarak !</a> </h1><script>$(document).ready(function() { $("#startDrawing").click(function(event) { event.preventDefault(); $.ajax({url: "/draw", method: "POST"}); }); });</script></body></html>')

@app.route('/draw', methods=['POST'])
def draw():
    draw_birthday_card()
    return ''

if __name__ == '__main__':
    app.run(debug=True)

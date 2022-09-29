import turtle
import pandas
screen = turtle.Screen()
screen.title("Morocco Map Game")
image = "Map-of-Morocco.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("list_of_morocco_cities.csv")
all_cities = data.city.to_list()
print(len(all_cities))
guessed_city = []
while len(guessed_city) < 50:
    answer_city = screen.textinput(title=f"{len(guessed_city)}/50 City correct",
                                   prompt="What's another city's name? ").title()
    if answer_city == "Exit":
        missing_data = [city for city in all_cities if city not in guessed_city]
        new_data = pandas.DataFrame(missing_data)
        new_data.to_csv("City to learn.csv")
        break

    if answer_city in all_cities:
        guessed_city.append(answer_city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == answer_city]
        t.goto(int(city_data.x), int(city_data.y))
        t.write(answer_city)
        t.write(city_data.city.item())


screen.exitonclick()

"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return 'Hi there!'


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Based off of yes or no answer- show madlib"""
    answer = request.args.get("game")
    # print(answer)

    if answer == "yes":
        return render_template("game.html")
    elif answer == "no":
        return render_template('goodbye.html')

@app.route("/madlib")
def show_madlib():
    color = request.args.get("color")
    noun1 = request.args.get("noun1")
    place = request.args.get("place")
    noun2 = request.args.get("noun2")
    person = request.args.get("person-name")
    verb1 = request.args.get("verb1")
    verb2 = request.args.get("verb2")
    adjective = request.args.get("adjective")
    return render_template("madlib.html", color=color, noun1=noun1, person=person, noun2=noun2, place=place, verb1=verb1, verb2=verb2, adjective=adjective,)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")

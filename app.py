from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
#the function name is the page name
def start():
    title = "A beary risky situation..."

    #three quotations = multi-line string
    text = """You are on an outing with your friends at a national park. 
    After a brisk walk, you finally make it to the start of the trailhead.
    Your neck creaks as your head turns, noticing a sign that says: BEWARE OF BEARS
    """

    #tuples inside a list
    choices = [
        #the first string refers to the page name
        ('go_in', "Go down the trail."),
        ('leave', "Turn back.")
        ]

    img_url = url_for('static', filename='beware.jpg')
    
    return render_template('adventure.html', title=title, text=text, choices=choices, img_url=img_url)

@app.route("/trail")
def go_in():
    title = "You enter the trail."

    text = """You walk half a mile down the trail and pull out a granola bar to snack on.
    You suddenly spot a bear dashing down the trail. It's coming...straight...at...YOU!!!"""

    choices = [
        ('taunt', "Taunt the bear."),
        ('leave', "Run away!")
    ]

    img_url = url_for('static', filename='trail.jpg')

    return render_template('adventure.html', title=title, text=text, choices=choices, img_url=img_url)

@app.route("/taunt")
def taunt():
    title = "You taunt the bear."

    text = """The bear is not phased.
    It's running at you now faster than ever.
    You offer your granola bar to the bear, but it's too late.
    It's already decided to have you for dinner.
    Its claws pierce peirce through your skin as it bites down on your flesh.
    You've just become bear food.
    """
    choices = []

    img_url = url_for('static', filename='nsfw.jpg')

    return render_template('adventure.html', title=title, text=text, choices=choices, img_url=img_url)

@app.route("/leave")
def leave():
    title = "You leave."

    text = """You decide that running into a bear is not worth the risk.
    You turn back and leave the trail with your friends.
    It's probably for the best."""

    choices = []

    img_url = url_for('static', filename='leave.jpg')

    return render_template('adventure.html', title=title, text=text, choices=choices, img_url=img_url)
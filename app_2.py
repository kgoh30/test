from flask_cors import CORS
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    send_from_directory,
    jsonify,
    Blueprint, 
    flash,
    url_for, 
    session
)
from preprocess import processdata
from findroute import get_route

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    # files = os.listdir(app_root)
    # return render_template('index.html',files=files)
    return render_template("index.html",longitude=[],latitude=[])

# @app.route("/input", methods=["POST", "GET"])
# def input():
#     if request.method == "POST":
#         content1 = request.form["contentt"]
#         choice1 = request.form["first_choice"]
#         choice2 = request.form["second_choice"]
#         session["content1"] = content1
#         session["choice1"] = choice1
#         session["choice2"] = choice2
#         return redirect(url_for("index"))
#     else:
#         return render_template("input.html")

# @app.route("/user")
# def user():
#     if "content1" in session:
#         content1 = session["content1"]
#         choice1 = session["choice1"]
#         choice2 = session["choice2"]
#         user_preference = [choice1, choice2, content1]
#         return f"<h1>{user_preference}</h1>"
#     else:
#         return redirect(url_for("index.html"))

@app.route("/show_route", methods=["POST","GET"])
def show_route():
    if request.method == "POST":
        content1 = session["content1"]
        choice1 = session["choice1"]
        choice2 = session["choice2"]
        user_preference = [choice1, choice2, content1]
        
        route = get_route()
        names = route["name"].to_list()
        longitude = route["longitude"].to_list()
        longitude = [float(val) for val in longitude]
        latitude = route["latitude"].to_list()
        latitude = [float(val) for val in latitude]
        return render_template("index.html", locations = names, route = route,longitude=longitude,latitude=latitude)
    else:
        return redirect(url_for('index'))

@app.route("/recommendations", methods=["POST","GET"])
def get_itinerary():
    route = get_route()
    return route

# @app.route("/map", methods=["POST","GET"])
# def get_route():

#     return render_template("map.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)

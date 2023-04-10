from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def home():
    return "<h1>This is my movie list!</h1> <a href='/favorite5'> Check out my favorite movies! </a>" 

@app.route("/favorite5")
def favorite5():
    movies = ["Harry Potter", "Godfather", "Greenbook", "Pulp Fiction", "Spiderman"]
    return render_template("favorite5.html", movies=movies)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    
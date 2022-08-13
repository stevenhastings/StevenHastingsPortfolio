from flask import Flask, render_template, request, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "portfolio\static\Pink Purple Geometric Music Youtube Thumbnail.png",
        "hero": "portfolio\static\Pink Purple Geometric Music Youtube Thumbnail.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
    },
    {
        "name": "Movie Watchlist App",
        "thumb": "portfolio\static\Pink Purple Geometric Music Youtube Thumbnail (1).png",
        "hero": "portfolio\static\Pink Purple Geometric Music Youtube Thumbnail (1).png",
        "categories": ["react", "javascript"],
        "slug": "movie-watchlist",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "portfolio\static\Pink Purple Geometric Music Youtube Thumbnail (2).png",
        "hero": "portfolio\static\Pink Purple Geometric Music Youtube Thumbnail (2).png",
        "categories": ["writing"],
        "slug": "api-docs",
    }
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html", 
        project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
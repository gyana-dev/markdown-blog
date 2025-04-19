from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

POSTS_DIR = "posts"

@app.route("/")
def home():
    posts = [f[:-3] for f in os.listdir(POSTS_DIR) if f.endswith(".md")]
    return render_template("home.html", posts=posts)

@app.route("/post/<title>")
def post(title):
    path = os.path.join(POSTS_DIR, f"{title}.md")
    if not os.path.exists(path):
        return "Post not found", 404
    with open(path, "r") as file:
        content = markdown.markdown(file.read())
    return render_template("post.html", title=title, content=content)

if __name__ == "__main__":
    app.run(debug=True)

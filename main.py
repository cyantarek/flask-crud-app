from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

db_path = "database.sqlite"
db = sqlite3.connect(db_path, check_same_thread=False)

db.execute("CREATE TABLE IF NOT EXISTS tb (id INTEGER PRIMARY KEY AUTOINCREMENT, book_title TEXT, book_price TEXT)")

@app.route("/", methods=["GET", "POST"])
def index():
    all = db.execute("SELECT * FROM tb").fetchall()

    if request.method == "POST":
        title = request.form["btitle"]
        price = request.form["bprice"]
        if title and price:
            db.execute("INSERT INTO tb (book_title, book_price) VALUES (?, ?)", (title, price,))
            db.commit()
            return redirect(url_for("index"))
    return render_template("index.html", all=all)

@app.route("/delete/<int:id>")
def delete(id):
    db.execute("DELETE FROM tb WHERE id=?", (str(id),))
    db.commit()
    return redirect(url_for("index"))

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        new_title = request.form["ntitle"]
        old_title = request.form["otitle"]
        db.execute("UPDATE tb SET book_title=? WHERE book_title=?", (new_title, old_title,))
        return redirect(url_for("update"))
    return render_template("update.html")
app.run(debug=True)
db.close()
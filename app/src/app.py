from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def tela_inicial():
    return render_template('home.html')


@app.route("/", methods=["POST"])
def main_page():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
        alltodos = Todo.query.all()
    return render_template("home.html", todos=alltodos)


@app.route('/get-all-todo', methods=['GET'])
def get_all():
    todos = Todo.query.all()
    return render_template("home.html", todos=todos)


@app.route("/delete/<int:sno>")
def delete(sno):
    deletetodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(deletetodo)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:sno>', methods=['GET'])
def vai_kct(sno):
    updatetodo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html",
                           updatetodo=updatetodo)


@app.route("/updatetodo/<int:sno>", methods=["POST"])
def update_todo(sno):
    if request.method == "POST":
        updatetodo = Todo.query.filter_by(sno=sno).first()
        title = request.form["title"]
        description = request.form["description"]
        todo = Todo(title=title, description=description)
        updatetodo.title = title
        updatetodo.description = description
        db.session.commit()
        return redirect("/")
    updatetodo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html",
                           updatetodo=updatetodo)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "{} is the title and {} is the description".format(self.title, self.description)


if __name__ == "__main__":
    app.run(debug=True)

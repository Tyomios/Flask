from flask import Flask, render_template, url_for

app = Flask(__name__) # указывает основной файл


# главная страница и home
@app.route('/')
@app.route('/home')
def index():
    return render_template("index1.html")


@app.route('/about')
def about():
     return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
     return "User page " + name + " - " + str(id)


#проверяем при запуске имя файла
if __name__ == "__main__":
    # метод запуска локального сервера
    app.run(debug = True)
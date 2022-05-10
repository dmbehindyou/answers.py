from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/galery')
def image():
    count = 5
    if request.method == 'POST':
        f = request.files['file'].read()
        fd = open(f"static/img/{count}.jpg", "wb")
        fd.write(f)
        fd.close()
        count += 1

    return render_template("index.html", count=count)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    print("Headers: ")
    print(request.headers)

    print("body: " + request.data )
    return "Hello World!"


@app.route('/test')
def hello():
    return "You contacted archiehub"


@app.route('/memory')
def hello():
    return "TODO: reroute to archiememory"


if __name__ == '__main__':
    app.run()

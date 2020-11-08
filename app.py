from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    print("Headers: ")
    print(request.headers)

    print("Body: " + str(request.data))
    return "Hello World!"


@app.route('/test')
def test():
    return "You contacted archiehub"


@app.route('/memory')
def memory():
    return "TODO: reroute to archiememory"


if __name__ == '__main__':
    app.run()

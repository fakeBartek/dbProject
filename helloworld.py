from flask import Flask, Response
import time

app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello World!"

@app.route("/clock")
def get_time_for_web():
    def eventStream():
        while True:
            yield get_time() + "\n"
    return Response(eventStream(), status=200, mimetype="text/event-stream")

def get_time():
    time.sleep(1)
    tt = time.ctime(time.time())
    return tt

def bootapp():
    app.run(port=8080, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()
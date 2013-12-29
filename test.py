from flask import Flask, send_file
import piggyphoto
app = Flask(__name__)
#app.debug = True

image = 'test.jpg'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/snap")
def snap():
    C.capture_preview(image)
    return send_file(image)

if __name__ == "__main__":
    C = piggyphoto.camera()
    C.leave_locked()
    C.capture_preview(image)
    app.run(host='0.0.0.0')



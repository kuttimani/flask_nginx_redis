from flask import Flask
import redis
app = Flask(__name__)

# set redis counter
r = redis.StrictRedis()

@app.route("/")
def hello():
    cntr = r.incr("conuter")
    return "simple flask app - counter %d " % cntr

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5555)

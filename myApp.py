from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "data":{
            "regno": 1847207,
            "namne": "ALWIN",
            "email": "alwin.joseph@mca.christunivers.in"
        }
    }

# TODO: create CRUD apis for this app

if __name__ == "__main__":
    app.run(debug=True)


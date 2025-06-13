from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["fakenews_db"]
collection = db["predictions"]

@app.route("/")
def index():
    results = collection.find().sort("_id", -1).limit(10)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

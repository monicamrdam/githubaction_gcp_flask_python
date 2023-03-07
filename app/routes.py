from flask import Flask
from flask import jsonify
from config import Config
from app.RickAndMortySpotify.artist.artist_controller import artist_page

app = Flask(__name__)

app.register_blueprint(artist_page)


@app.route('/')
def home():
    message = {
        "Home": Config.URL_PORT,
        "Artist": Config.URL_PORT + 'artist?name=',
    }
    return jsonify(message)
"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    playlist = db.relationship('Playlist', backref='playlists_songs', cascade='all')


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    song = db.relationship('Song', backref='playlists_songs', cascade='all')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    playlist_id= db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.Integer, nullable=False)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

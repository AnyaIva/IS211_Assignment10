DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS songs;


CREATE TABLE artists (
	  artist_id INTEGER PRIMARY KEY, 
	  artist_name TEXT
);

CREATE TABLE albums (
	  album_id INTEGER PRIMARY KEY, 
	  album_name TEXT,	
    artist_id INTEGER
);

CREATE TABLE songs (
	  song_id INTEGER PRIMARY KEY, 
 	  song_name TEXT,
	  artist_id INTEGER,
    album_id INTEGER, 
	  track_number INTEGER, 
	  duration INTEGER
);

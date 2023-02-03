/*1 Basic inserting function.*/
INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu') ;
INSERT INTO Users (name, email) VALUES ('Sally', 'sally@umich.edu') ;


/*2 Basic table creation function.*/
CREATE TABLE ___ ( attribute1 VARCHAR(128), attribute2 VARCHAR(128) );
user_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
PRIMARY KEY(user_id),


/*3 Distinct selection with groupping */
SELECT DISTINCT Artist.name, COUNT(DISTINCT Genre.name)
FROM Track JOIN Album JOIN Artist JOIN Genre
ON Album.artist_id = Artist.artist_id AND Track.album_id = Album.album_id AND Track.genre_id = Genre.genre_id
GROUP BY Artist.name;


/*4 Establishing a foreign key.*/
CREATE TABLE Artist (
    artist_id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    PRIMARY KEY(artist_id)
) ENGINE = INNODB;

CREATE TABLE Album (
    album_id INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(255),
    artist_id INTEGER,
    PRIMARY KEY(album_id),
    INDEX USING BTREE(title),
    
    CONSTRAINT FOREIGN KEY(artist_id)
    	REFERENCES Artist(artist_id)
    	ON DELETE CASCADE ON UPDATE CASCADE
    ) ENGINE = InnoDB;


/*5 Creating slightly more complex tables and establishing a foreign key in a hierarchical order */
CREATE TABLE Genre (
     genre_id INTEGER NOT NULL AUTO_INCREMENT,
     name VARCHAR(255),
     PRIMARY KEY(genre_id),
     INDEX USING BTREE(name)
) ENGINE = InnoDB;

CREATE TABLE Track (
    track_id INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(255)
    len INTEGER,
    rating INTEGER,
    count INTEGER,
    album_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY(track_id),
    INDEX USING BTREE(title),
    
    CONSTRAINT FOREIGN KEY (album_id) REFERENCES Album(album_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FOREIGN KEY (genre_id) REFERENCES Genre(genre_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;

# Скрин в телеге
# https://sqliteonline.com/#fiddle=cd1c80ff0734daec3ad455f662d296369c04e4bb2dda07748502731edc3b40f3


# CREATE TABLE sportsman(
#   ID INT PRIMARY KEY NOT NULL,
#   NAME TEXT NOT NULL,
#   RANK TEXT NOT NULL,
#   YEAR_BD INT NOT NULL,
#   RECORD TEXT NOT NULL,
#   COUNTRY TEXT NOT NULL
#   );

# CREATE TABLE competition(
#   ID INT PRIMARY KEY NOT NULL,
#   NAME TEXT NOT NULL,
#   RECORD TEXT NOT NULL,
#   DATE_R TEXT NOT NULL
#   );


# CREATE TABLE result(
#   COMPETITION_ID INT NOT NULL,
#   SPORTSMAN_ID INT NOT NULL,
#   RESULT TEXT NOT NULL,
#   CITY TEXT NOT NULL,
#   HOLD_DATE NOT NULL,
#   FOREIGN KEY (COMPETITION_ID) REFERENCES competition(id),
#   FOREIGN KEY (SPORTSMAN_ID) REFERENCES sportsman(id)
#   );


# INSERT INTO competition VALUES(1, "Легкая атлетика - бег 100 м", "00:9.58", "16.08.2009")
# INSERT INTO competition VALUES(2, "Биатлон 20 км", "49:13.9", "10.03.2016")
# INSERT INTO competition VALUES(3, "Плавание 50 м", "00:20.91", "18.11.2009")


# INSERT INTO sportsman VALUES(1, "David Rudisha", "Master", 1988, "00:11.23", "Kenya")
# INSERT INTO sportsman VALUES(2, "Usain Bolt", "Master", 1986, "00:9.58", "Jamaica")

# INSERT INTO sportsman VALUES(3, "Martin Fourcade", "Master", 1988, "49:13.9", "France")
# INSERT INTO sportsman VALUES(4, "Ole Einar Bjorndalen", "Master", 1974, "49:50.3", "Norway")

# INSERT INTO sportsman VALUES(5, "Cesar Cielu", "Master", 1987, "00:20.91", "Brazil")
# INSERT INTO sportsman VALUES(6, "Clement Kolesnikov", "Master", 2000, "00:24.00", "Russia")


# INSERT INTO result VALUES(1, 1, "1 место", "New-York", "2013-08-12");
# INSERT INTO result VALUES(1, 2, "2 место", "New-York", "2013-08-12");
# INSERT INTO result VALUES(2, 3, "2 место", "Paris", "2009-08-12");
# INSERT INTO result VALUES(2, 4, "2 место", "Paris", "2009-08-12");
# INSERT INTO result VALUES(3, 5, "5 место", "Russia", "2015-12-12");
# INSERT INTO result VALUES(3, 6, "12 место", "Russia", "2015-12-12");

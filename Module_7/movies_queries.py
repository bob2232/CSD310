import mysql.connector

db= mysql.connector.connect(
    user= "root",
    password= "Akof@2232",
    host = "127.0.0.1",
    database= "movies",
    raise_on_warnings= True
    )

print("--DISPLAYING studio RECORDS--")

cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name FROM studio")
studio = cursor.fetchall()
for studio in studio:
    print("Studio ID: {}\nStudio Name:{}\n" .format(studio[0], studio[1])) 

print()
print("--DISPLAYING genre RECORDS--")

cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre")
genre = cursor.fetchall()
for genre in genre:
    print("Genre ID: {}\nGenre Name:{}\n" .format(genre[0], genre[1]))
print()

print("--DISPLAYING short film RECORDS--")

cursor.execute("SELECT film_name, film_runtime FROM film where film_runtime<120 ")
film = cursor.fetchall()
for film in film:
    print("Film Name: {}\nRuntime:{}\n" .format(film[0], film[1]))

print()

print("--DISPLAYING Director RECORDS in order--")

cursor.execute("SELECT film_name, film_director FROM film order by film_director ")
film = cursor.fetchall()
for film in film:
    print("Film Name: {}\nDirector:{}\n" .format(film[0], film[1]))



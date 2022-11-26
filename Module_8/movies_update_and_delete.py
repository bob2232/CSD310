import mysql.connector

db = mysql.connector.connect(
    database = 'movies',
    user = 'root',
    password = 'Akof@2232',
    host = '127.0.0.1',
    raise_on_warnings= True)

cursor = db.cursor()


# method to execute an inner join on all table,
# iterate over the data set and output the results to the terminal window.
def show_films(cursor, title):
    
# inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre,\
studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN\
 studio ON film.studio_id = studio.studio_id")

#get the results from the cursor object
    films = cursor.fetchall()
    print("\n -- {} --".format(title))

#iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0],\
            film[1], film[2], film[3]))


show_films(cursor, "DISPLAYING FILMS")
#print()
#insert new row
sql_command = """INSERT INTO film(film_id, film_name, film_releaseDate, film_runtime,\
                film_director, studio_id, genre_id) VALUES ( 4, "Star War", "2000", "112",\
             "George Lucas",(select studio_id from studio WHERE studio_name = "20th Century Fox"),\
                            (select genre_id from genre WHERE genre_name = "Scifi"));"""

cursor.execute(sql_command)
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

#update film table

sql_command = """UPDATE film SET genre_id = 1 WHERE film_name = 'Alien';"""

cursor.execute(sql_command)
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Change Alien to Horror")


#delete row

sql_command = """DELETE from film WHERE film_name = 'Gladiator';"""
cursor.execute(sql_command)
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")



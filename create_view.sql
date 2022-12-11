CREATE VIEW film_view AS
SELECT film_name, film_director
FROM film
WHERE film_releaseDate = '2017';
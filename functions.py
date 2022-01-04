import json
import sqlite3

def load_db(query):
    '''function which load data from database'''
    con = sqlite3.connect("data/netflix.db")
    cur = con.cursor()
    sqlite_query = (query)
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    return executed_query


def search_title(title_name):
    '''function which searching movies by title'''
    executed_query = load_db(
        "SELECT `title`, `country`, `release_year`, `listed_in`, `description` "
        "FROM netflix "
        f"WHERE title = '{title_name}' "
        "ORDER BY `release_year` DESC LIMIT 1 ")
    data = []
    if executed_query:
        data.append({
            "title": executed_query[0][0],
            "country": executed_query[0][1],
            "release_year": executed_query[0][2],
            "genre": executed_query[0][3],
            "description": executed_query[0][4]
            })
        return data
    data.append({
        "title": '-',
        "country": '-',
        "release_year": '-',
        "genre": '-',
        "description": '-'
    })
    return data

print(search_title(1995))

def search_years(year_1, year_2):
    '''function which searching movies between set years'''
    executed_query = load_db(
        "SELECT `title`, `release_year` "
        "FROM netflix "
        f"WHERE release_year BETWEEN {year_1} AND {year_2} "
        "ORDER BY `release_year` DESC LIMIT 100 ")
    data = []
    for i in executed_query:
        films = {
        "title": i[0],
        "release_year": i[1]
        }
        data.append(films)
    return data

print(search_years(1990, 1991))


def search_rating(rating):
    '''function which searching movies by rating'''
    executed_query = load_db (
        "SELECT `title`, `rating`, `description` "
        "FROM netflix "
        f"WHERE rating = '{rating}' "
        "ORDER BY `title` DESC LIMIT 100 ")
    data = []
    for i in executed_query:
        films = {
            "title": i[0],
            "rating": i[1],
            "description": i[2]
        }
        data.append(films)
    return data

print(search_rating('PG-13'))

def rating_exist():
    '''function which making all exist ratings in list'''
    executed_query = load_db (
        "SELECT `rating` "
        "FROM netflix "
        "GROUP BY rating")
    rating_list = []
    for i in executed_query:
        rating_list += i
    return rating_list

print(rating_exist())

def search_genre(genre):
    '''function which searching movies by genre'''
    executed_query = load_db (
        "SELECT `title`, `description` "
        "FROM netflix "
        f"WHERE `listed_in` LIKE '%{genre}%' "
        "ORDER BY `release_year` DESC LIMIT 10 ")
    data = []
    for i in executed_query:
        films = {
            "title": i[0],
            "description": i[1]
        }
        data.append(films)
    return data

print(search_genre('Dramas'))

def genre_exist():
    '''function which making all exist genre in list'''
    executed_query = load_db (
        "SELECT `listed_in` "
        "FROM netflix "
        "GROUP BY listed_in")
    genre_list = []
    for i in executed_query:
        genre_list += i[0].split(', ')
    return list(set(genre_list))

print(genre_exist())

def search_actors(actor_1, actor_2):
    '''function which searching movies by two set actors and show those actors which played with them more than two times'''
    executed_query = load_db (
        "SELECT `cast` "
        "FROM netflix "
        f"WHERE `cast` LIKE '%{actor_1}%' AND `cast` LIKE '%{actor_2}%' "
        "ORDER BY `release_year` DESC LIMIT 10 ")
    all_actors_list = []
    actors_list = []
    for i in executed_query:
        all_actors_list += i[0].split(', ')
    count_actors = {}.fromkeys(all_actors_list, 0)
    for i in all_actors_list:
        count_actors[i] += 1
    for key, value in count_actors.items():
        if value > 2 and key != actor_1 and key != actor_2:
            actors_list.append(key)
    return actors_list

print(search_actors('Rose McIver', 'Ben Lamb'))

def some_movies(movie_type, year, genre):
    '''function which searching movies by type, year and genre'''
    executed_query = load_db (
        "SELECT `title`, `description` "
        "FROM netflix "
        f"WHERE `type`='{movie_type}' AND `release_year`='{year}' AND `listed_in` LIKE '%{genre}%' "
        "LIMIT 100 ")
    data = []
    for i in executed_query:
        films = {
            "title": i[0],
            "description": i[1]
        }
        data.append(films)
    return data

print(some_movies('Movie', '2020', 'Dramas'))
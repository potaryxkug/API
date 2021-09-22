
#  Importer flask
from os import times
from MesFichiersFonctions import make_film, make_public_film
from flask import Flask, json, jsonify, abort, request
from flask.helpers import make_response, url_for
#  import pour mysql_flask
from flask_mysqldb import MySQL
from werkzeug.wrappers import response

# le nom de mon app 
app = Flask(__name__)

# appel de mysql pour l'utiliser
mysql = MySQL(app)
#  configuration à la connection msql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sakila'

#-------------------------------------------------------------------------------

'''
-----------* R *-------------- Read the data base -----methods = ['GET'] -----
'''
# voir en bas fonction 1 et fonction 2
#  route pour recuperer la liste des films dans ma bdd
@app.route('/films', methods=['GET'])
def get_film():
    try:
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM film")
        reponse = cur.fetchall()
        cur.close()
        filmes=[]
        for f in reponse:
            film = make_film(f)
            filmes.append(film)
        return jsonify([make_public_film(film) for film in filmes])
        #return jsonify(filmes)
    except Exception as e:
        print(e)
        abort(404)


#  route pour recuperer les couleurs
@app.route('/films/<int:film_id>', methods=['GET'])
def get_film_by_id(film_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM film WHERE film_id=%s",(str(film_id)))
        response = cur.fetchone()
        cur.close()
       # return jsonify(response)
        return jsonify(make_public_film(make_film(response))) # application de la fonction qui retourne le nom des couleurs
    except Exception as e:
        print(e)
        abort(404)

'''
-----------* U *-------------- Read the data base -----methods = ['GET'] -----
'''
#  route pour modifier un film de ma liste de ma bdd
@app.route('/films/<int:film_id>', methods=['PUT'])
def update_film(film_id):
    film=get_film_by_id(film_id)
    if not request.json:
        abort(400)

    # if "film_id" in request.json and type(request.json['film_id']) != int:
    #     abort(400)
    # if "language_id" in request.json and type(request.json["language_id"]) is not str:
    #     abort(400)
    # if "last_update" in request.json and type(request.json['last_update']) is not times:
    #     abort(400)
    # if "length" in request.json and type(request.json['length']) != int:
    #     abort(400)
    # if "original_language" in request.json and type(request.json["original_language"]) is not :
    #      abort(400)
    # if "rating" in request.json and type(request.json['rating']) is not bool:
    #     abort(400)
    # if "release_year" in request.json and type(request.json['release_year']) is not str:
    #      abort(400)
    # if "rental_duration" in request.json and type(request.json['rental_duration']) != int:
    #     abort(400)
    # if "rental_rate" in request.json and type(request.json["rental_rate"]) is not float:
    #     abort(400)
    # if "remplacement_cost" in request.json and type(request.json['remplacement_cost']) is not float:
    #     abort(400)
    # if "special_feactures" in request.json and type(request.json['special_feactures']) is not float:
    #     abort(400)
    if "title" in request.json and type(request.json['title']) is not float:
        abort(400)

    try:
        film_id = request.json.get('film_id', film.json['film_id'])
        language_id = request.json.get('language_id', film.json['language_id'])
        last_update = request.json.get('last_update', film.json['last_update'])
        length = request.json.get('length', film.json['length'])
        original_language = request.json.get('original_language', film.json['original_language'])
        rating = request.json.get('rating', film.json['rating'])
        release_year = request.json.get('release_year', film.json['release_year'])
        rental_duration = request.json.get('rental_duration', film.json['rental_duration'])
        remplacement_cost = request.json.get('remplacement_cost', film.json['remplacement_cost'])
        special_feactures = request.json.get('special_feactures', film.json['special_feactures'])
        social_feacture = request.json.get('social_feacture', film.json['social_feactures'])
        titre = request.json.get('titre', film.json['titre'])
        description = request.json.get('description', film.json['description'])
      
        cur= mysql.connection.cursor()
        cur.execute("UPDATE film SET titre=%s, description=%s, social_feacture=%s, special_feactures=%s, remplacement_cost%s,rental_duration=%s,rental_duration=%s ,release_year=%s,rating=%s,original_language=%s,length=%s,last_update=%s, language_id=%s, film_id=%s, WHERE id=%s",
        (titre, description,social_feacture, special_feactures, remplacement_cost,rental_duration,release_year,rating,original_language,length,last_update,film_id,language_id))
        mysql.connection.commit()
        cur.close()
        return get_film_by_id(film_id)
    except Exception as e:
        print(e)
        return jsonify({'is': False})    


'''
-----------* C *-------------- Read the data base -----methods = ['GET'] -----
'''
#route pour ajouter une tache à ma liste dans ma bdd
@app.route('/films', methods=['POST'])
def create_film():
    if "film_id" in request.json and type(request.json['film_id']) != int:
        abort(400)
    if "language_id" in request.json and type(request.json["language_id"]) is not str:
        abort(400)
    if "last_update" in request.json and type(request.json['last_update']) is not times:
        abort(400)
    if "length" in request.json and type(request.json['length']) != int:
        abort(400)

    try:
        # creer les champs de ma nouvelle tache
        #id_article = request.json['id_article'] automatisé

        film_id = request.json['film_id']
        language_id = request.json['language_id']
        last_update = request.json['last_update']
        length = request.json.get['length']
        original_language = request.json['original_language']
        rating = request.json['rating']
        release_year = request.json['release_year']
        rental_duration = request.json['rental_duration']
        remplacement_cost = request.json['remplacement_cost']
        special_feactures = request.json['special_feactures']
        social_feacture = request.json['social_feactures']
        titre = request.json['titre']
        description = request.json['description']

    # rendre ID_ARTICLE auto incrémente

        cur = mysql.connection.cursor()
        cur.execute("SELECT film_id FROM film ORDER BY film_id DESC" )
        res = cur.fetchone()
        cur.close()
        film_id = res[0]+1
        # creer ma connection et envoyer à ma bdd
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO film(titre, description,social_feacture, special_feactures, remplacement_cost,rental_duration,release_year,rating,original_language,length,last_update,film_id,language_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(titre, description,social_feacture, special_feactures, remplacement_cost,rental_duration,release_year,rating,original_language,length,last_update,film_id,language_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({'is':True})
    except Exception as e:
        print(e)
        return jsonify({'is':False})

'''
-----------* D *-------------- Delete element in the data base ------ methods = DELETE----
'''
#  route pour supprimer une tache de ma liste dans ma bdd
@app.route('/films/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    film = get_film_by_id(film_id)
    try:
        cur= mysql.connection.cursor()
        cur.execute("DELETE FROM film WHERE film_id =%s", (str(film_id)))
        mysql.connection.commit()
        cur.close()
        return film
    except Exception as e:
        print(e)
        return jsonify({'is': False}) 








#  lancer mon application
if __name__ == '__main__':
    app.run(debug=True)


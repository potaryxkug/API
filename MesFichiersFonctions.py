
from flask.helpers import url_for

'''
#fonction crée une liste de valeur à partire de page html parser
'''
def make_film(film):
    list_tache= list(film)
    # transformation en Json
    new_film={}
    new_film['film_id']=int(list_tache[0])
    new_film['language_id']=str(list_tache[1])
    new_film['last_update']=str(list_tache[2])
    new_film['length']=int(list_tache[3])
    new_film['original_language']=str(list_tache[4])
    new_film['rating']=str(list_tache[5])
    new_film['release_year']=str(list_tache[6])
    new_film['rental_duration']=int(list_tache[7])
    new_film['rental_rate']=str(list_tache[8])
    new_film['remplacement_cost']=str(list_tache[9])
    new_film['special_feactures']=str(list_tache[10])
    new_film['title']=str(list_tache[11])
    # print(new_film)
    return new_film


'''
# fonction crée une liste de valeur à partire de page html parser
'''
def make_public_film(film):
    public_film={}
    for argument in film:
        if argument == "film_id":
            public_film['url_film']= url_for('get_film_by_id', film_id=film['film_id'], _external=True)


        else:
            public_film[argument]=film[argument]


    return public_film


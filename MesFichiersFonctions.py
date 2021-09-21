
'''
fonction crée une liste de valeur à partire de page html parser
'''

def liste_token( parser,titre ,style_titre ):
    body = parser.find_all(titre, style = style_titre)
    liste_token = []
    for i in body:
        premiere_balyse = i
        monaie = [ j for j in premiere_balyse]
        monaie = monaie[1]
        liste_token.append(monaie)
    return liste_token

''' 
Création de la liste du prix des tokens
'''
def liste_prix_token( parser, titre ,titre_class):
    a = parser.find_all(titre,class_=titre_class ) # Pour extraire le prix de toutes les monnaie
    list_prix = []
    for i in range(len(a)):
        list_prix.append(a[i].text)
        list_prix_token = []
    for i in range(0,len(list_prix),4):
        list_prix_token.append(list_prix[i])
    return list_prix_token
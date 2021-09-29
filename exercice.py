#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values=[]
        while len(values)<10:
            values.append(input('donnez une valeur'))
    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        anagrame1=[]
        anagrame2=[]
        word1=input('ecrit un mot')
        word2=input('ecrit un deuxieme mot')
        for lettre in word1:
            anagrame1.append(word1(lettre))
        for lettre in word2:
            anagrame2.append(word2(lettre))
    print("anagrame" if sorted(anagrame1)==sorted(anagrame2) else "pas anagrame")


def contains_doubles(items: list) -> bool:
    listeComparaison = set(items)
    return len(listeComparaison) > len(items)
    


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_grades2=[]
    names2=[]
    for names in student_grades:
        grades=student_grades[name]
        
    return {names2[best_grades2.index(best_grade)]:best_grade}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    lettres_repetees={}
    lettres_repetees5={}
    for lettre in sentence:
        lettres_repetees[lettre]=0
    for lettre in sentence:
        lettres_repetees[lettre]+=1
    for lettre in lettres_repetees:
        if lettres_repetees[lettre]<=5:
            lettres_repetees5[lettre]=lettres_repetees[lettre]
    lettres_repetees5.sort(key=lambda x : x)
    print(lettres_repetees5)
    return lettres_repetees5


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    livre={}
    continuer_livre=('oui')
    while continuer_livre=='oui':
        recette=input('donnez le nom de la recette')
        livre[recette]=(input('donnez les ingredients de la rectte'))
        continuer_livre=(input('voulez vous continuer?'))
    return livre


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom_recette=input("donne le nom d'une recette:")
    if nom_recette in ingredients:
        print(ingredients[nom_recette])


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()

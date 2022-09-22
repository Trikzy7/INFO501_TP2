from image import *

def lecture_modeles(chemin_dossier):
    """Fonction qui lis en mémoire dans une liste les images de modèles de chiffres.

    Parameters
    ----------
    chemin_dossier : str
        chemin d'accès au dosser contenant les images

    Returns
    -------
    list
        liste des images modèles
    """
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = load_image(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, H, W, liste_modeles, S):
    """Fonction qui effectue la reconnaissance de chiffre.

    Parameters
    ----------
    image : numpy array
        image à reconnaitre
    H : int
        hauteur de l'image
    W : int
        largeur de l'image
    liste_modeles : liste
        liste des images de modèles
    S : int
        seuil de binarisation
    """
    max_similarity = 0
    cpt = 0

    # 1. Binarisation
    img_bin = binarisation_image(image, H, W, S)

    # 2. Localisation
    img_bin_loc = localisation_image(img_bin, H, W)

    for model in liste_modeles:
        # Get data from current model
        current_model_image, current_model_H, current_model_W = model

        # 3. Resize Image according model's dimension
        img_bin_loc_res = resize_image(img_bin_loc, current_model_H, current_model_W)

        # 4. Get Similarity with the current model
        current_model_similarity = similitude(current_model_image, img_bin_loc_res, current_model_H, current_model_W)
        if current_model_similarity > max_similarity:
            max_similarity = current_model_similarity
            id_model_with_max_similarity = cpt

        cpt += 1

    return id_model_with_max_similarity


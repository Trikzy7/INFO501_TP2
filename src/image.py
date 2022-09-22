'''
File: image.py
Created Date: Friday August 27th 2021 - 02:35pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Wed Sep 14 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
'''

from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np


def load_image(file_name):
    """Fonction permettant de lire une image en émoire dans un numpy array.

    Parameters
    ----------
    file_name : str
        chemin d'accès à l'image

    Returns
    -------
    numpy array, int, int
        l'image lue, la hauteur de l'image et la largeur de l'image
    """
    image = io.imread(file_name)
    H, W = image.shape
    # print("lecture image : " + file_name + " (" + str(H) + "x" + str(W) + ")")
    return image, H, W


def display_image(image, titre):
    """Fonction permettant d'afficher à l'écran l'image passée en paramètre.

    Parameters
    ----------
    image : numpy array
        image à afficher
    titre : str
        titre de la figure

    Returns
    -------
    figure
        un objet représentant la figure affichée
    """
    fig = plt.figure(figsize=(4,6))
    plt.imshow(image, aspect='auto', cmap='gray')
    plt.title(titre)
    plt.show()
    # print("ICIIIIIIIIIIIIIIIIIIIIIIII AKA LE VRAI DEBUG")
    return fig


def creer_image_tableau(tableau):
    """Fonction qui à partir d'un tableau (liste de liste) renvoie un numpy array 2D.

    Parameters
    ----------
    tableau : liste de liste
        le tableau à convertir en numpy array
    """
    return np.array(tableau, dtype=np.uint8)


def creer_image_vide(H, W):
    """Fonction qui initialise un numpy array avec des zeros.

    Parameters
    ----------
    H : int
        hauteur de l'image
    W : int
        largeur de l'image

    Returns
    -------
    numpy arary
        image de zeros
    """
    return np.zeros((H, W), dtype=np.uint8)


def binarisation_image(image, H, W, S):
    """Fonction permettant de binariser une image où les pixels sont stockés sur 8bits.

    Parameters
    ----------
    image : numpy array
        image à binariser
    H : int
        hauteur de l'image
    W : numpy array
        largeur de l'image
    S : int
        seuil de binarisation

    Returns
    -------
    numpy array
        image binarisée
    """
    # Creation Image Vide
    result = creer_image_vide(H, W)

    for line in range(H):
        for column in range(W):
            # Au dessus du seuil on met le pixel au max en blanc sinon on met au min en noir
            result[line, column] = 255 if image[line, column] > S else 0

    return result

def resize_image(image, new_H, new_W):
    """Fonction permettant de redimensionner une image passée en entrée.

    Parameters
    ----------
    image : numpy array
        image à redimensionner
    new_H : int
        nouvelle hauteur de l'image
    new_W : int
        nouvelle largeur de l'image

    Returns
    -------
    numpy array
        image redimensionnée
    """
    pixels_resized = resize(image, (new_H, new_W), 0)
    img_resized = np.uint8(pixels_resized*255)
    return img_resized


def localisation_image(image, H, W):
    """Fonction permettant de localiser l'emplacement d'un chiffre dans l'image.

    Parameters
    ----------
    image : numpy array
        image à découper
    H : int
        hauteur de l'image
    W : int
        largeur de l'image

    Returns
    -------
    numpy array
        image ne contenant uniquement que le chiffre sans espace autoir
    """
    cMin, cMax = W, 0
    lMin, lMax = H, 0

    for line in range(H):
        for column in range(W):
            if image[line, column] == 0:
                cMin = column if column < cMin else cMin
                cMax = column if column > cMax else cMax

                lMin = line if line < lMin else lMin
                lMax = line if line > lMax else lMax

    return image[lMin:lMax+1, cMin:cMax+1]

def similitude(image_1, image_2, H, W):
    """Fonction permettant de calculer la similitude entre deux images de la même taille.

    Parameters
    ----------
    image_1 : numpy array
        image 1
    image_2 : numpy array
        image 2
    H : int
        hauteur des images
    W : int
        largeur des images

    Returns
    -------
    float
        la valeur de similitude entre les deux images
    """
    cpt_similarity = 0
    cpt_pixels = 0

    for line in range(H):
        for column in range(W):
            if image_1[line, column] == image_2[line, column]:
                cpt_similarity += 1
            cpt_pixels += 1

    ratio = cpt_similarity / cpt_pixels

    return ratio

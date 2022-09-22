'''
File: main.py
Created Date: Friday August 27th 2021 - 02:35pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Wed Sep 14 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
'''
import matplotlib.pyplot as plt
from image import *
from reconnaissance import reconnaissance_chiffre, lecture_modeles

if __name__ == '__main__':
    # Variables utiles
    path_to_assets = '../assets/'
    plt.ion()  # Mode interactif de matplotlib our ne pas bloquer l'éxécutions lorsque l'on fait display

    # ==============================================================================
    # Lecture image et affichage
    # ==============================================================================
    image, H, W = load_image(path_to_assets + 'test4.JPG')
    display_image(image, "Image Test")

    # image_bin = binarisation_image(image, H, W, 200)
    # display_image(image_bin, "Exemple d'image Bin")
    #
    # image_bin_localisation = localisation_image(image_bin, H, W)
    # display_image(image_bin_localisation, "Exemple d'image Bin localisée")
    #
    # image_bin_localisation_resized = resize_image(image_bin_localisation, 60, 100)
    # display_image(image_bin_localisation_resized, "Exemple d'image Bin localisée Resize (60, 100)")

    list_models = lecture_modeles(path_to_assets)
    id_model_image = reconnaissance_chiffre(image, H, W, list_models, 200)

    image_model, H_model, W_model = load_image(path_to_assets + '_' + str(id_model_image) + '.png')
    display_image(image_model, 'Image Model')

    print("C'est un jolie : " + str(id_model_image))







    # print( similitude(image_bin_localisation_resized, image_bin_localisation_resized, 60, 100) )
    # ==============================================================================
    # Binarisation de l'image et affichage. Décommenter au besoin.
    # ==============================================================================
    S = 70
    # image_binarisee = binarisation_image(image, H, W, S)
    # display_image(image_binarisee, "Image binarisee")

    # ==============================================================================
    # Localisation de l'image et affichage. Décommenter au besoin.
    # ==============================================================================
    # image_localisee = localisation_image(image_binarisee, H, W)
    # display_image(image_localisee, "Image localisee")

    # ==============================================================================
    # Redimensionnement de l'image et affichage. Décommenter au besoin.
    # ==============================================================================
    # image_resizee = resize_image(image_localisee, 100, 500)
    # display_image(image_resizee, "Image redimensionee")

    # ==============================================================================
    # Lecture modeles et reconnaissance. Décommenter au besoin.
    # ==============================================================================
    # liste_modeles = lecture_modeles(path_to_assets)
    # chiffre = reconnaissance_chiffre(image, H, W, liste_modeles, 70)
    # print("Le chiffre reconnu est : ", chiffre)

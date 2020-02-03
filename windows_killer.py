import cv2  # opencv-python
import os
import numpy as np
from time import time, sleep
from PIL import ImageGrab
import pyautogui

template_ = cv2.imread('croix.png', 0)  # 0 c'est pour le noir et blanc.  # todo faut en avoir plusieurs pour cross platform


def cv2_from_doc(img_rgb, template):
    """ C'est très lent, et ca prend pas qd la croix est grisée, en arrière plan (pas plus mal pour ce que je veux faire
    d'ailleurs.
    Provient de la doc de cv2
    """

    # fixme plutot que de faire une detection de plusieurs points, detecter 1 seul, cliquer dessus, le fermer, refaire une capture..
    # on peut essayer d'utiliser cv2.UMat(cv2.imread('croix.png', 0)), (OpenCl) mais c'est pas beaucoup plus rapide, et surtt ca fout la merde

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)  # testé les aures algo, de la merde
    # une solution pure numpy pour du exact matching serait pe plus perf
    # todo compiler ac PyInstaller pr voir si c'est plus rapide

    threshold = 0.8
    loc = np.where(res >= threshold)

    points = []
    for pt in zip(*loc[::-1]):
        points.append(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    print("Executed in: ", time()-t1)

    # interomp le programme..
    # cv2.imshow('blabla', img_rgb)
    # cv2.waitKey(0)
    return points


def click_to(point):
    # pyautogui.moveTo(point[0], point[1], 5)
    pyautogui.moveTo(point[0], point[1], pyautogui.easeInOutSine(0.9)*2)
    # todo faut interpoler des points intermédiaires maintenant..
    # todo bouger les arrow key et faire entrée en cas de dialog de fermeture. juste entrée devrait suffire d'ailleurs..


    pyautogui.click()



# sleep(5)

t1 = time()
print("start")

# todo faudrait un listener pour interompre, en appuyant sur un bouton
while True:
    os.startfile("")  # todo faut trouver un truc pour pop à un endroit différent.. o pire je peux faire un drag ultra rapide.. ou faire partir la souris d'un endroit aléatoire, mais moins marrant
    # faire comme ca évite d'installer d'autres grosses libs genre Qt
    # => cv2.moveWindow() tien tien

    sleep(3)

    img_rgb_ = np.array(ImageGrab.grab())  # problème d'inversion de couleurs..;
    # cap = cv2.VideoCapture(0) # marche pas..

    points_ = cv2_from_doc(img_rgb_, template_)
    print(points_)
    for point_ in points_:
        click_to(point_)

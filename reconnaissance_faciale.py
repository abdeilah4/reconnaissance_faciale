import threading
import cv2
from deepface import DeepFace

# Initialisation du la caméra
cam = cv2.VideoCapture(0)


cam.set(cv2.CAP_PROP_FRAME_HEIGHT,640)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,480)

# un compteur pour ne pas faire des testes sur chaque frame => une rapidité d'utilisation
compteur=0

# boolean pour tester si l'image capturer est similaire à l'image réf ou non
similaire=False

# l'image référence
imgRef = cv2.imread(r'assets\img1.png')


def verifier_visage(frame):
    global similaire
    
    try:
        if DeepFace.verify(frame,imgRef)['verified']:
            similaire=True
        else:
            similaire = False
    except ValueError:
        pass

while True:
    ret,frame=cam.read()

    if ret:
        if compteur % 30==0:
            try:
                threading.Thread(target=verifier_visage,args=(frame.copy(),)).start()
            except ValueError:
                compteur=0
        compteur+=1
        if similaire:
            cv2.putText(frame,'Similaire!',(180,30),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,'Non Similaire !!',(180,30),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
        cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break
    
cv2.destroyAllWindows()
cam.release()
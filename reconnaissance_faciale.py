import threading
import cv2
from deepface import DeepFace

#Caméra
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#l'image de référence
imgRef=cv2.imread(r'assets\img1.png')
 
similaire = False
frame_a_verifier = None
lock = threading.Lock()

#fonction principale
def verifier_visage():
    global similaire, frame_a_verifier
    while True:
        if frame_a_verifier is not None:
            with lock:
                frame = frame_a_verifier
                frame_a_verifier = None
            
            try:
                similaire = DeepFace.verify(frame, imgRef)['verified']
            except Exception:
                similaire = False

#Lancer le thread
threading.Thread(target=verifier_visage, daemon=True).start()

#Boucle principale
while True:
    ret, frame = cam.read()
    if not ret:
        break
    
    if frame_a_verifier is None:
        with lock:
            frame_a_verifier = frame.copy()
    
    texte = 'Similaire!' if similaire else 'Non Similaire !!'
    couleur = (0, 255, 0) if similaire else (0, 0, 255)
    cv2.putText(frame, texte, (180, 30),cv2.FONT_HERSHEY_SIMPLEX, 2, couleur, 3)

    cv2.imshow('Reconnaissance Faciale', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



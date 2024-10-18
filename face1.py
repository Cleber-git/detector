import cv2
from deepface import DeepFace

video_capture = cv2.VideoCapture(0)

while True:

    # Captura frame por frame
    ret, frame = video_capture.read()
    
    # Converte frame em bgr
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Tenta detectar rostos e faz a verificação com o deepface
    
    try:
        # Analisa o frame atual em busca de rostos
        result = DeepFace.analyze(rgb_frame, actions=['emotion', 'age' ], enforce_detection=False)
        cv2.putText(frame, f"Emoção: {result[0]['dominant_emotion']}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f"Idade: {result[0]['age']}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        # cv2.putText(frame, f"Gênero: {result[0]['gender']}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    except Exception as e:
        print(f"Erro: {e}")    
        
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

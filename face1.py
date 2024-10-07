import face_recognition
import face_recognition_models
import cv2
import os

def carregar_rostos_conhecidos(pasta_rostos):
    rostos_conhecidos = []
    nomes_rostos_conhecidos = []

    for arquivo in os.listdir(pasta_rostos):
        if ".jpg" in arquivo: 
            print(arquivo)

            caminho_imagem = os.path.join(pasta_rostos, arquivo)
            # carregar a imagem para obter a codificação
            imagem = face_recognition.load_image_file(caminho_imagem)
            codificacoes = face_recognition.face_encodings(imagem)

            if len(codificacoes) > 0:
                rostos_conhecidos.append(codificacoes[0])
                nomes_rostos_conhecidos.append(os.path.splitext(arquivo)[0])

    return rostos_conhecidos, nomes_rostos_conhecidos

# carregar rostos conheicidos
pasta_rostos_conhecidos = "C:/Users/pc/Documents/detector/"
rostos_conhecidos, nomes_rostos_conhecidos = carregar_rostos_conhecidos(pasta_rostos_conhecidos)


video_capture = cv2.VideoCapture(0)

while True:
    # capturar um frame de vídeo 
    ret, frame = video_capture.read()

    # converter o frame em bgr 
    rgb_frame = frame[:, :, ::-1]

    # localizar o rosto no frame
    localizar_rosto = face_recognition.face_locations(rgb_frame)
    codificacoes_rosto = face_recognition.face_encodings(frame, localizar_rosto)

    # percorrer todos os rostos detectados

    for(top, right, bottom, left), codificacoes_rosto in zip(localizar_rosto, codificacoes_rosto):
        # comparar rostos detectados com rostos conhecidos
        resultados = face_recognition.compare_faces(rostos_conhecidos, codificacoes_rosto)
        distancias = face_recognition.face_distance(rostos_conhecidos, codificacoes_rosto)

        # selecionar rosto mais semelhante

        melhor_indice = distancias.argmin()
        if resultados[melhor_indice]:
            nome = nomes_rostos_conhecidos[melhor_indice]
        else:
            nome = "Desconhecido"

        #  desenhar um retângulo ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255,  0), 2)
        #  Escrever o nome da pessoa detectada

        cv2.putText(frame, nome, (left, top - 10), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,255, 0), 2)

    cv2.imshow('Video',frame)
    if cv2.waitKey(1) == ord('q'):
        break

# liberar a captura de video e fechar as janelas
video_capture.release()
cv2.destroyAllWindows()
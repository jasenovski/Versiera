import numpy as np
import cv2
from utils.utils import reta_igual_circunferencia as ric

verde, vermelho, azul, preto, branco = (0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 0, 0), (255, 255, 255)
padding = 10
imagens = []

def gerar_versiera(configs):
    canvas = np.ones(shape=(configs["altura"] + 10, configs["largura"], 3), dtype=np.uint8) * 255

    circunferencia = {"centro": (int(0.5 * configs["largura"]), int(0.5 * (configs["altura"] - 2 * padding))), "r": int(0.5 * configs["altura"]) - padding}
    canvas = cv2.circle(img=canvas, center=(circunferencia["centro"]), radius=circunferencia["r"], color=verde, thickness=1)

    passo = 1 / configs["num_pontos"]
    ks = np.arange(0 + passo, 1, passo)
    pontos_dois = [(int(k * configs["largura"]), configs["altura"] - 2 * padding) for k in ks]

    indice_correto = 1

    dt = (configs["T"] / configs["num_pontos"])

    print("[INFO] Pressione a tecla 'q' para parar a geração de pontos")
    for ponto_dois in pontos_dois:

        reta = {"pt1": (int(0.5 * configs["largura"]), 0), "pt2": ponto_dois, "a": 0, "b": 0}
        try:
            reta["a"] = (reta["pt2"][1] - reta["pt1"][1]) / (reta["pt2"][0] - reta["pt1"][0])
            reta["b"] = (reta["pt2"][0] * reta["pt1"][1] - reta["pt1"][0] * reta["pt2"][1]) / (reta["pt2"][0] - reta["pt1"][0])

            solucao = ric(reta=reta, circunferencia=circunferencia, indice_correto=indice_correto)

            ponto_versiera = (reta["pt2"][0], solucao[1])

            canvas = cv2.line(img=canvas, pt1=reta["pt1"], pt2=reta["pt2"], color=vermelho, thickness=1)

            canvas = cv2.line(img=canvas, pt1=reta["pt2"], pt2=ponto_versiera, color=preto, thickness=1)
            canvas = cv2.line(img=canvas, pt1=ponto_versiera, pt2=solucao, color=preto, thickness=1)

            canvas = cv2.circle(img=canvas, center=ponto_versiera, radius=3, color=azul, thickness=-1)
        
        except ZeroDivisionError:
            canvas = cv2.line(img=canvas, pt1=reta["pt1"], pt2=ponto_dois, color=vermelho, thickness=1)
            canvas = cv2.circle(img=canvas, center=(int(0.5 * configs["largura"]), configs["altura"] - 2 * padding), radius=3, color=azul, thickness=-1)
            indice_correto = 0
        
        imagens.append(cv2.flip(src=cv2.rotate(src=canvas, rotateCode=cv2.ROTATE_180), flipCode=1))

        cv2.imshow(winname="Maria Gaetana Agnesi", mat=cv2.flip(src=cv2.rotate(src=canvas, rotateCode=cv2.ROTATE_180), flipCode=1))
        chave = cv2.waitKey(int(dt * 1000))
        if chave in [ord("Q"), ord("q")]:
            break

    canvas = cv2.flip(src=cv2.rotate(src=canvas, rotateCode=cv2.ROTATE_180), flipCode=1)

    return canvas, imagens
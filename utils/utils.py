import os
import cv2
import numpy as np
import json
import imageio
import time

MENSAGEM = \
"""[INFO] Pressione a tecla 'ENTER' para gerar uma imagem da figura.
[INFO] Pressione outra tecla para sair..."""

def exportar_canvas(configs, canvas):
    nome_arquivo = "Versiera_{}x{}_{} pontos.jpg".format(configs["largura"], configs["altura"], configs["num_pontos"])
    export_path = os.path.join("imagens", nome_arquivo)
    if not os.path.exists(export_path):
        cv2.imwrite(filename=export_path, img=canvas)
        print(f"[INFO] A imagem foi exportada para {export_path}")
    else:
        print("[INFO] A imagem já existia.")


def exportar_video(configs, imagens, fps):

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    nome_arquivo = "Versiera_{}x{}_{} pontos.mp4".format(configs["largura"], configs["altura"], configs["num_pontos"])
    export_path = os.path.join("videos", nome_arquivo)

    if not os.path.exists(export_path):
        writer = cv2.VideoWriter(export_path, fourcc, fps, (imagens[0].shape[1], imagens[0].shape[0]))
        time.sleep(1)

        for imagem in imagens:
            writer.write(imagem)
        
        writer.release()
        time.sleep(1)
        print(f"[INFO] O video foi exportada para {export_path}")
    else:
        print("[INFO] O video já existia.")


def exportar_gif(configs, imagens):
    nome_arquivo = "Versiera_{}x{}_{} pontos.gif".format(configs["largura"], configs["altura"], configs["num_pontos"])
    export_path = os.path.join("gifs", nome_arquivo)
    if not os.path.exists(export_path):
        imageio.mimsave(export_path, imagens, duration=0.001)
        print(f"[INFO] O gif foi exportada para {export_path}")
    else:
        print("[INFO] O gif já existia.")


def pitagoras(pt1, pt2):
    return np.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)


def carregar_configs(caminho_carregar):

    arquivo_json = os.path.join(*caminho_carregar.split("/"))
    with open(file=arquivo_json, mode="r") as json_file:
        dados = json.load(json_file)

        configs = {}
        for key, value in dados.items():
            configs[key] = value
        
        return configs


def reta_igual_circunferencia(reta, circunferencia, indice_correto):
    # coeficiente "a" da solução de segundo grau
    coef_um = (1 + reta["a"] ** 2)

    # coeficiente "b" da solução de segundo grau
    coef_dois = (2 * reta["a"] * reta["b"]) - (2 * reta["a"] * circunferencia["centro"][1]) - 2 * circunferencia["centro"][0]

    # coeficiente "c" da solução de segundo grau
    coef_tres = (reta["b"] ** 2) + (circunferencia["centro"][1] ** 2) - (2 * reta["b"] * circunferencia["centro"][1]) + (circunferencia["centro"][0] ** 2) - (circunferencia["r"] ** 2)

    # parametro delta da solução de segundo grau
    delta = coef_dois ** 2 - (4 * coef_um * coef_tres)

    x_cruz = [(-coef_dois + np.sqrt(delta)) / (2 * coef_um), (-coef_dois - np.sqrt(delta)) / (2 * coef_um)]
    y_cruz = [reta["a"] * x_cruz[0] + reta["b"], reta["a"] * x_cruz[1] + reta["b"]]
    solucoes = list(zip(x_cruz, y_cruz))
    solucao = solucoes[indice_correto]

    solucao = (int(round(number=solucao[0], ndigits=0)), int(round(number=solucao[1], ndigits=0)))

    return solucao
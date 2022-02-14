import numpy as np
import cv2
from utils.utils import exportar_canvas, carregar_configs, MENSAGEM
from model.versiera import gerar_versiera

if __name__ == "__main__":
    configs = carregar_configs(caminho_carregar="configuracoes/config.json")
    canva = gerar_versiera(configs=configs)
    cv2.imshow(winname="Maria Gaetana Agnesi", mat=canva)
    print(MENSAGEM)
    chave = cv2.waitKey(0)
    if chave == 13:
        exportar_canvas(configs=configs, canvas=canva)

    cv2.destroyAllWindows()

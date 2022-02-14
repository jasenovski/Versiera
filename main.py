import numpy as np
import cv2
from utils.utils import exportar_canvas, carregar_configs, exportar_gif, exportar_video, MENSAGEM
from model.versiera import gerar_versiera

if __name__ == "__main__":
    configs = carregar_configs(caminho_carregar="configuracoes/config.json")
    
    canva, imagens = gerar_versiera(configs=configs)

    cv2.imshow(winname="Maria Gaetana Agnesi", mat=canva)
    print(MENSAGEM)
    chave = cv2.waitKey(0)
    if chave == 13:
        exportar_canvas(configs=configs, canvas=canva)
        exportar_video(configs=configs, imagens=imagens, fps=30)
        exportar_gif(configs=configs, imagens=imagens)

    cv2.destroyAllWindows()

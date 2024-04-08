import glob  # biblioteca para listar arquivos
import os  # biblioteca para manipular arquivos e pastas
from typing import List

import pandas as pd

input_path = './data/input'


def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de uma pasta data/input
    e retornar uma lista de dataframes

    args: input_path (str): caminho da pasta com os arquivos

    return:lista de dataframes
    """
    file_path = glob.glob(os.path.join(input_path, '*.xlsx'))

    data_frame_list = []
    for file in file_path:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    """
    declaramos dessa forma por que temos as variaveis de ambiente setadas
    pelo python,e uma delas é o name, por padrao o nome do scritp que rodamos é
    main, quando fazemos da forma acima estamos falando que o código em questão é um modulo
    e não um script unico, então tudo que estiver abaixo não sera executado quando charmos o módulo
    em outro arquivo, pois ele vai ser executado com o nome do arquivo salvo e não como main, e
    só sera executado o que estiver abaixo do main, se eu executar direto o arquivo.

    E para isso (Trabalhar com módulos) precisamos tambem  criar o __init__.py
    """

    dataframe_list = extract_from_excel(input_path)
    print(dataframe_list)

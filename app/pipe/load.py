import os

import pandas as pd

def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    Recebe um dataframe concatenado de todos os outros arquivos e salva em
    um só arquivo excel.

    args:
    data_frame: Conjunto de dados unificados de todos os arquivos
    output_path: Caminho onde vamos salvar o arquivo
    file_name: Nome do arquivo Excel a ser gerado    

    return: "Arquivo salvo com sucesso"
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)

    return 'Arquivo salvo com sucesso'

from typing import List

import pandas as pd




def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função que concatena todos os dataframes em um só.
    
    args:
    data_frame_list: Lista com todos os dataframes gerados, de todos os arquivos 
    Excel.

    return: Dataframe concatenado com todos os arquivos Excel
    """
    return pd.concat(data_frame_list)

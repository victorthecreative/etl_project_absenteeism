from pipe.extract import extract_from_excel
from pipe.load import load_excel
from pipe.transform import concat_data_frames

if __name__ == '__main__':
    dataframe_list = extract_from_excel('data/input')
    print("extraido do excel")
    data_frame = concat_data_frames(dataframe_list)
    print("concatenado em um unico dataframe")
    load_excel = load_excel(data_frame, 'data/output', 'output_file')
    print("Processo concluido")


import pandas as pd
import json
import os

directory_path = 'plcs'
output_directory_path = 'saidas'
json_config_data_types = './configs/datatypes.json'
json_types = './configs/types.json'

def load_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def process_csv(file_path, output_path, json_config_data_types, json_types):
    try:
        df = pd.read_csv(file_path, skiprows=6, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, skiprows=6, encoding='latin1')

    df.columns = ['TYPE', 'SCOPE', 'NAME', 'DESCRIPTION', 'DATATYPE', 'SPECIFIER', 'ATTRIBUTES']

    types = load_json(json_types)["types"]

    df = df[(df['TYPE'] == 'TAG') & (df['DATATYPE'].str.lower().isin(types))]

    df['DATATYPE'] = df['DATATYPE'].str.lower()

    dataTypes = load_json(json_config_data_types)

    plc_name = os.path.splitext(os.path.basename(file_path))[0]

    expanded_rows = []
    for _, row in df.iterrows():
        datatype = row['DATATYPE']
        if datatype in dataTypes:
            for suffix in dataTypes[datatype]:
                new_row = row.copy()
                new_row['NAME'] = f"{row['NAME']}{suffix}"
                expanded_rows.append(new_row)
        else:
            expanded_rows.append(row)

    df_expanded = pd.DataFrame(expanded_rows)

    df_expanded['plcName'] = plc_name
    df_expanded['plcTag'] = df_expanded['NAME']
    df_expanded['pointName'] = df_expanded['NAME'].str.replace('.', '_')
    df_expanded['description'] = df_expanded['NAME'].str.replace('.', '_')

    df_final = df_expanded[['plcName', 'plcTag', 'pointName', 'description']]

    df_final.to_excel(output_path, index=False)

    print(f"Arquivo processado e salvo em {output_path}")

for filename in os.listdir(directory_path):
    if filename.endswith(".xls") or filename.endswith(".csv"):
        file_path = os.path.join(directory_path, filename)
        output_path = os.path.join(output_directory_path, f"{os.path.splitext(filename)[0]}_saida.xlsx")
        process_csv(file_path, output_path, json_config_data_types, json_types)

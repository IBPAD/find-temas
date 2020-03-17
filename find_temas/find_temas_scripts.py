# coding: utf-8

import re
import json
import pandas as pd
from unicodedata import normalize

def remove_acents(text):
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def clear_name(text): 
    text = remove_acents(text)  
    text = re.sub(r'[^A-Za-z0-9_]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    text = re.sub(r' ', '_', text)
    text = text.lower()
    return text

def get_base_as_df(base_file_path, coluna_texto):
    base = pd.read_csv(base_file_path)
    base = base.dropna(subset=[coluna_texto])
    return base

def is_about_tema(tema_regex, text):
    return bool(re.findall(tema_regex, text))

def add_temas_to_df(df, temas, coluna_texto):
    df_temas = df.copy()
    for tema in temas:
         df_temas[tema['nome']] = df_temas[coluna_texto].apply(lambda x: is_about_tema(tema['regex'], x))
    return df_temas

def generate_temas_from_csv(temas_csv_path):
    temas_df = pd.read_csv(temas_csv_path)
    temas_names = list(temas_df)

    temas_list = []
    for tema in temas_names:
        terms = list(temas_df[tema])
        clear_terms = [term for term in terms if str(term) != 'nan']
        
        regex_list = [r'\b'+term+r'\b' for term in clear_terms]
        regex_pattern = '|'.join(regex_list)
        regex_pattern = '(?i)'+regex_pattern

        temas_list.append({"nome": tema, "regex": regex_pattern})

    return temas_list

def get_temas(temas_file_path):
    with open(temas_file_path) as file:  
        temas = json.load(file)

    temas = temas['temas']
    return temas

def find_temas(base, temas, coluna_texto, output):
    base_with_temas = add_temas_to_df(base, temas, coluna_texto)
    base_with_temas.to_csv(output, index=False)
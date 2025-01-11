# File: scripts/check_updates.py
import os
import json
import requests

MODS_JSON_PATH = os.path.join(os.path.dirname(__file__), "mods.json")
MODS_DIRECTORY = os.path.join(os.path.dirname(__file__), "../mods/")

def load_mods():
    """Carrega os dados do mods.json"""
    try:
        with open(MODS_JSON_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Erro] Não foi possível carregar mods.json: {e}")
        return {}

def download_file(url):
    """Faz o download do conteúdo do arquivo remoto"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[Erro] Falha ao baixar arquivo de {url}: {e}")
        return None

def update_existing_file(mod_name, local_file_path, remote_content):
    """Atualiza o arquivo existente com o conteúdo remoto"""
    with open(local_file_path, "r") as f:
        local_content = f.read()

    if local_content == remote_content:
        print(f"[Info] {mod_name}: já está atualizado.")
        return False

    with open(local_file_path, "w") as f:
        f.write(remote_content)

    print(f"[Info] {mod_name}: atualizado com sucesso.")
    return True

def update_mod(mod_name, url):
    """Verifica e atualiza o arquivo en_us.json de um mod"""
    local_file_path = os.path.join(MODS_DIRECTORY, mod_name, "en_us.json")

    if not os.path.exists(local_file_path):
        print(f"[Erro] O arquivo {local_file_path} não existe. Pule este mod.")
        return False

    remote_content = download_file(url)
    if remote_content is None:
        return False

    return update_existing_file(mod_name, local_file_path, remote_content)

def main():
    """Função principal"""
    mods_data = load_mods()
    if not mods_data:
        print("[Erro] Nenhum dado encontrado no mods.json")
        return

    for mod_name, url in mods_data.items():
        print(f"Verificando {mod_name}...")
        update_mod(mod_name, url)

if __name__ == "__main__":
    main()

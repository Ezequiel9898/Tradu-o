# File: scripts/check_updates.py
import os
import json
import requests
from datetime import datetime

MODS_JSON_PATH = os.path.join(os.path.dirname(__file__), "mods.json")
MODS_DIRECTORY = "../mods/"

def load_mods():
    try:
        with open(MODS_JSON_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Erro] Não foi possível carregar mods.json: {e}")
        return {}

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"[Erro] Falha ao baixar arquivo de {url}: {e}")
        return None

def update_mod(mod_name, url):
    mod_dir = os.path.join(MODS_DIRECTORY, mod_name)
    local_file_path = os.path.join(mod_dir, "en_us.json")
    os.makedirs(mod_dir, exist_ok=True)

    remote_content = download_file(url)
    if remote_content is None:
        return False, "Erro ao baixar"

    if os.path.exists(local_file_path):
        with open(local_file_path, "r") as f:
            local_content = f.read()
        if local_content == remote_content:
            print(f"[Info] {mod_name} já está atualizado.")
            return False, "Já atualizado"

    with open(local_file_path, "w") as f:
        f.write(remote_content)
    print(f"[Info] {mod_name} foi atualizado.")
    return True, "Atualizado com sucesso"

def main():
    mods_data = load_mods()
    if not mods_data:
        print("[Erro] Nenhum dado encontrado no mods.json")
        return

    summary = {}
    for mod_name, url in mods_data.items():
        print(f"Verificando {mod_name}...")
        updated, status = update_mod(mod_name, url)
        summary[mod_name] = {
            "status": status,
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S") if updated else "Não atualizado"
        }

    print("\nResumo da atualização:")
    for mod, info in summary.items():
        print(f"{mod}: {info['status']} (Última atualização: {info['last_update']})")

if __name__ == "__main__":
    main()

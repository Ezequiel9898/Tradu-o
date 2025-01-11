# File: scripts/check_updates.py
import os
import json
import requests
from datetime import datetime

# Caminhos para os arquivos
MODS_JSON_PATH = os.path.join(os.path.dirname(__file__), "mods.json")
MODS_DIRECTORY = "../mods/"

# Função para carregar o arquivo mods.json
def load_mods():
    with open(MODS_JSON_PATH, "r") as f:
        return json.load(f)

# Função para salvar o arquivo mods.json
def save_mods(mods_data):
    with open(MODS_JSON_PATH, "w") as f:
        json.dump(mods_data, f, indent=4)

# Função para baixar o conteúdo do arquivo en_us.json
def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Levanta erro se a requisição falhar
    return response.text

# Função para verificar e atualizar um mod
def update_mod(mod_name, mod_data):
    mod_dir = os.path.join(MODS_DIRECTORY, mod_name)
    local_file_path = os.path.join(mod_dir, "en_us.json")
    os.makedirs(mod_dir, exist_ok=True)

    try:
        remote_content = download_file(mod_data["url"])
    except Exception as e:
        print(f"[Erro] Não foi possível baixar o arquivo para {mod_name}: {e}")
        return False

    if os.path.exists(local_file_path):
        with open(local_file_path, "r") as f:
            local_content = f.read()
        if local_content == remote_content:
            print(f"[Info] {mod_name} está atualizado.")
            return False

    # Atualiza o arquivo local
    with open(local_file_path, "w") as f:
        f.write(remote_content)
    print(f"[Info] {mod_name} atualizado com sucesso.")
    return True

# Função principal
def main():
    mods_data = load_mods()
    updated_mods = []

    for mod_name, mod_data in mods_data.items():
        print(f"Verificando {mod_name}...")
        if update_mod(mod_name, mod_data):
            mods_data[mod_name]["status"] = "Atualizado"
            mods_data[mod_name]["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            updated_mods.append(mod_name)
        else:
            mods_data[mod_name]["status"] = "Já estava atualizado"

    save_mods(mods_data)

    if updated_mods:
        print("\nMods atualizados:")
        for mod in updated_mods:
            print(f"- {mod}")
    else:
        print("\nNenhum mod precisava de atualização.")

if __name__ == "__main__":
    main()

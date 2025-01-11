import os
import json
import requests
from datetime import datetime

MODS_JSON_PATH = 'scripts/mods.json'
MODS_DIR = 'mods/'

def load_mods_json():
    with open(MODS_JSON_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_mods_json(data):
    with open(MODS_JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def update_en_us_file(mod_name, mod_url):
    try:
        response = requests.get(mod_url)
        response.raise_for_status()

        try:
            json_data = response.json()
        except ValueError as e:
            print(f"Erro ao tentar decodificar JSON para o mod {mod_name}: {e}")
            return False

        mod_dir = os.path.join(MODS_DIR, mod_name)
        if not os.path.exists(mod_dir):
            os.makedirs(mod_dir)

        en_us_file_path = os.path.join(mod_dir, 'en_us.json')

        with open(en_us_file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)

        print(f"Arquivo en_us.json atualizado para o mod {mod_name}.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro ao atualizar o arquivo en_us.json para o mod {mod_name}: {e}")
        return False

def update_readme(mods_data):
    with open('README.md', 'r', encoding='utf-8') as file:
        readme_lines = file.readlines()

    start_index = None
    for i, line in enumerate(readme_lines):
        if "Status de Tradução dos Mods" in line:
            start_index = i
            break

    if start_index is not None:
        with open('README.md', 'w', encoding='utf-8') as file:
            for i, line in enumerate(readme_lines):
                if i == start_index + 1:
                    file.write("## Status de Tradução dos Mods\n")
                    for mod_name, mod_info in mods_data.items():
                        status = mod_info['status']
                        file.write(f"- **{mod_name}**: {status}\n")
                else:
                    file.write(line)

def main():
    mods_data = load_mods_json()

    for mod_name, mod_info in mods_data.items():
        print(f"Verificando atualização para o mod: {mod_name}")

        mod_url = mod_info['url']

        if update_en_us_file(mod_name, mod_url):
            mod_info['status'] = 'Atualizado'
        else:
            mod_info['status'] = 'Desatualizado'

        mod_dir = os.path.join(MODS_DIR, mod_name)
        readme_path = os.path.join(mod_dir, 'README.md')

        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write(f"# Status da Tradução - {mod_name}\n\n")
            file.write(f"- **Status**: {mod_info['status']}\n")
            file.write(f"- **Última atualização**: {datetime.now().strftime('%Y-%m-%d')}\n")

    save_mods_json(mods_data)
    update_readme(mods_data)

if __name__ == "__main__":
    main()

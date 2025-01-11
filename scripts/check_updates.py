import os
import json
import requests
from datetime import datetime

# Caminhos para os arquivos
MODS_JSON_PATH = 'scripts/mods.json'
EN_US_JSON_PATH = 'scripts/en_us.json'  # Caminho do arquivo en_us.json local
README_PATH = 'README.md'

# Função para ler o arquivo mods.json
def load_mods_json():
    with open(MODS_JSON_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

# Função para escrever de volta o mods.json
def save_mods_json(data):
    with open(MODS_JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Função para verificar se a tradução precisa ser atualizada
def check_mod_update(mod_url, mod_name):
    try:
        response = requests.get(mod_url)
        response.raise_for_status()  # Vai lançar um erro se a resposta não for 200
        return response.json(), None
    except requests.exceptions.RequestException as e:
        return None, f"Erro ao acessar {mod_name}: {e}"

# Função para atualizar o arquivo en_us.json com a versão mais recente
def update_en_us_file(mod_url):
    try:
        response = requests.get(mod_url)
        response.raise_for_status()
        
        # Salva o conteúdo do arquivo en_us.json original
        with open(EN_US_JSON_PATH, 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, ensure_ascii=False, indent=4)
        
        print(f"Arquivo en_us.json atualizado com sucesso.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro ao atualizar o arquivo en_us.json: {e}")
        return False

# Função para atualizar o README.md
def update_readme(mods_data):
    with open(README_PATH, 'r', encoding='utf-8') as file:
        readme_lines = file.readlines()

    # Identificar onde o status dos mods está no README
    start_index = None
    for i, line in enumerate(readme_lines):
        if "Lista de Mods" in line:
            start_index = i
            break

    if start_index is not None:
        with open(README_PATH, 'w', encoding='utf-8') as file:
            for i, line in enumerate(readme_lines):
                if i == start_index + 2:  # Adiciona a linha com os status dos mods
                    file.write("## 📜 Lista de Mods\n")
                    file.write("| Mod              | Status        | Última Atualização |\n")
                    file.write("|-------------------|---------------|--------------------|\n")
                    for mod_name, mod_url in mods_data.items():
                        status = mod_url if mod_url != 'Atualizado' else 'Atualizado'
                        last_update = datetime.now().strftime('%Y-%m-%d')
                        file.write(f"| **{mod_name}** | {status} | {last_update} |\n")
                else:
                    file.write(line)

# Função principal para atualizar o mods.json e README
def main():
    mods_data = load_mods_json()

    for mod_name, mod_url in mods_data.items():
        print(f"Verificando atualização para o mod: {mod_name}")
        
        mod_data, error = check_mod_update(mod_url, mod_name)

        if error:
            print(f"Erro: {error}")
        else:
            # Atualiza o arquivo en_us.json com a versão mais recente
            if mod_data:
                print(f"Atualizando o arquivo en_us.json para o mod: {mod_name}")
                if update_en_us_file(mod_url):
                    mods_data[mod_name] = 'Atualizado'
                else:
                    mods_data[mod_name] = 'Desatualizado'
            else:
                mods_data[mod_name] = 'Desatualizado'

    save_mods_json(mods_data)
    update_readme(mods_data)

if __name__ == "__main__":
    main()

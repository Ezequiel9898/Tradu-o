import os
import json
import requests
from datetime import datetime

# Diretórios
MODS_DIR = os.path.join(os.getcwd(), 'mods')
MODS_JSON = os.path.join(os.getcwd(), 'scripts', 'mods.json')

# Função para baixar e atualizar o arquivo en_us.json
def update_en_us_file(mod_name, mod_url):
    try:
        # Baixa o arquivo original
        print(f"Baixando o arquivo para o mod: {mod_name} de {mod_url}")
        response = requests.get(mod_url)

        # Verifica se a resposta foi bem sucedida
        if response.status_code != 200:
            print(f"Falha ao baixar o arquivo {mod_name}: Status {response.status_code}")
            return False

        # Tenta decodificar o JSON
        try:
            json_data = response.json()
        except ValueError as e:
            print(f"Erro ao tentar decodificar JSON para o mod {mod_name}: {e}")
            return False

        # Verifica ou cria a pasta do mod
        mod_dir = os.path.join(MODS_DIR, mod_name)
        if not os.path.exists(mod_dir):
            os.makedirs(mod_dir)

        # Caminho do arquivo en_us.json
        en_us_file_path = os.path.join(mod_dir, 'en_us.json')

        # Salva o arquivo en_us.json
        with open(en_us_file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)

        print(f"Arquivo en_us.json atualizado para o mod {mod_name}.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro ao atualizar o arquivo en_us.json para o mod {mod_name}: {e}")
        return False

# Função para atualizar o status do mod no mods.json
def update_mod_status(mod_name, mod_url, status):
    try:
        # Carrega o arquivo mods.json
        with open(MODS_JSON, 'r', encoding='utf-8') as file:
            mods_data = json.load(file)

        # Atualiza o status mantendo o link original
        mods_data[mod_name] = {
            'url': mod_url,  # Mantém o link original
            'status': status,  # Atualiza o status
            'last_update': datetime.now().strftime('%Y-%m-%d')  # Adiciona a data da última atualização
        }

        # Salva novamente o arquivo mods.json
        with open(MODS_JSON, 'w', encoding='utf-8') as file:
            json.dump(mods_data, file, ensure_ascii=False, indent=4)

        print(f"Status do mod {mod_name} atualizado para: {status}.")
    except Exception as e:
        print(f"Erro ao atualizar o status do mod {mod_name}: {e}")

# Função principal para verificar e atualizar todos os mods
def main():
    try:
        # Carrega o arquivo mods.json
        with open(MODS_JSON, 'r', encoding='utf-8') as file:
            mods_data = json.load(file)

        for mod_name, mod_info in mods_data.items():
            print(f"Verificando atualização para o mod: {mod_name}")

            mod_url = mod_info['url']  # Pega o link da URL do mod

            # Atualiza o arquivo en_us.json para o mod
            if update_en_us_file(mod_name, mod_url):
                # Se o arquivo for atualizado, marca como atualizado
                update_mod_status(mod_name, mod_url, "Atualizado")
            else:
                # Caso contrário, marca como desatualizado
                update_mod_status(mod_name, mod_url, "Desatualizado")
    except Exception as e:
        print(f"Erro ao executar o processo: {e}")

# Executa o script
if __name__ == '__main__':
    main()

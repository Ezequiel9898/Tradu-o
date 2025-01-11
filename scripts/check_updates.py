import os
import json
import requests
from datetime import datetime

# Diretórios
MODS_DIR = os.path.join(os.getcwd(), 'mods')
MODS_JSON = os.path.join(os.getcwd(), 'scripts', 'mods.json')

# Função para baixar o arquivo en_us.json de uma URL
def download_en_us_file(mod_name, mod_url):
    try:
        print(f"Baixando o arquivo para o mod: {mod_name} de {mod_url}")
        response = requests.get(mod_url)

        # Verifica se a resposta foi bem sucedida
        if response.status_code != 200:
            print(f"Falha ao baixar o arquivo {mod_name}: Status {response.status_code}")
            return None

        # Retorna o conteúdo JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {mod_name}: {e}")
        return None

# Função para comparar e atualizar o arquivo en_us.json
def update_en_us_file(mod_name, mod_url):
    try:
        mod_dir = os.path.join(MODS_DIR, mod_name)
        if not os.path.exists(mod_dir):
            os.makedirs(mod_dir)

        # Caminho do arquivo en_us.json
        en_us_file_path = os.path.join(mod_dir, 'en_us.json')

        # Baixa o conteúdo atualizado
        new_content = download_en_us_file(mod_name, mod_url)
        if new_content is None:
            print(f"Não foi possível atualizar o arquivo {mod_name}.")
            return False

        # Verifica se o arquivo já existe localmente
        if os.path.exists(en_us_file_path):
            with open(en_us_file_path, 'r', encoding='utf-8') as file:
                current_content = json.load(file)

            # Compara o conteúdo local com o novo conteúdo
            if current_content == new_content:
                print(f"O arquivo {mod_name} já está atualizado.")
                return False
            else:
                print(f"O arquivo {mod_name} foi alterado. Atualizando...")
        else:
            print(f"Arquivo {mod_name} não encontrado. Criando um novo.")

        # Salva o novo conteúdo no arquivo local
        with open(en_us_file_path, 'w', encoding='utf-8') as file:
            json.dump(new_content, file, ensure_ascii=False, indent=4)

        print(f"Arquivo en_us.json do mod {mod_name} atualizado.")
        return True

    except Exception as e:
        print(f"Erro ao atualizar o arquivo en_us.json para o mod {mod_name}: {e}")
        return False

# Função para atualizar o status no arquivo mods.json
def update_mod_status(mod_name, mod_url, status):
    try:
        # Carrega o arquivo mods.json
        with open(MODS_JSON, 'r', encoding='utf-8') as file:
            mods_data = json.load(file)

        # Atualiza o status do mod
        mods_data[mod_name] = {
            'url': mod_url,  # Link da URL do mod
            'status': status,  # Atualiza o status
            'last_update': datetime.now().strftime('%Y-%m-%d')  # Data da última atualização
        }

        # Salva as alterações no arquivo mods.json
        with open(MODS_JSON, 'w', encoding='utf-8') as file:
            json.dump(mods_data, file, ensure_ascii=False, indent=4)

        print(f"Status do mod {mod_name} atualizado para: {status}.")
    except Exception as e:
        print(f"Erro ao atualizar o status do mod {mod_name}: {e}")

# Função principal para verificar todos os mods
def main():
    try:
        # Carrega o arquivo mods.json
        with open(MODS_JSON, 'r', encoding='utf-8') as file:
            mods_data = json.load(file)

        for mod_name, mod_info in mods_data.items():
            print(f"Verificando atualização para o mod: {mod_name}")

            mod_url = mod_info['url']  # Pega o link da URL do mod

            # Tenta atualizar o arquivo en_us.json do mod
            if update_en_us_file(mod_name, mod_url):
                # Se o arquivo foi atualizado, marca como "Atualizado"
                update_mod_status(mod_name, mod_url, "Atualizado")
            else:
                # Se o arquivo não foi alterado, marca como "Desatualizado"
                update_mod_status(mod_name, mod_url, "Desatualizado")
    except Exception as e:
        print(f"Erro ao executar o processo: {e}")

# Executa o script
if __name__ == '__main__':
    main()

import json
import os
import requests
from datetime import datetime

def fetch_content(url):
    """
    Baixa o conteúdo do arquivo de uma URL fornecida. Se o link for do GitHub, ajusta a URL para usar o formato 'raw'.
    """
    try:
        # Se a URL for do GitHub, substituímos a parte do 'blob' por 'raw.githubusercontent.com'
        if 'github.com' in url:
            url = url.replace('github.com', 'raw.githubusercontent.com').replace('blob/', '')

        # Fazendo a requisição para baixar o conteúdo do arquivo
        response = requests.get(url)
        response.raise_for_status()  # Lança erro para códigos de status de erro (404, 403, etc.)

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o conteúdo de {url}: {e}")
        return None

def load_json_from_file(file_path):
    """
    Carrega um arquivo JSON local.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_to_file(file_path, data):
    """
    Salva os dados em formato JSON em um arquivo.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_readme(mods_json, readme_path):
    """
    Atualiza o arquivo README.md com o status dos mods.
    """
    with open(readme_path, 'w', encoding='utf-8') as readme:
        readme.write("# Traduções de Mods para Minecraft\n\n")
        readme.write("Este repositório contém traduções de mods para Minecraft. O status das traduções é monitorado automaticamente.\n\n")
        readme.write("## 📜 Lista de Mods\n\n")
        readme.write("| Mod              | Status        | Última Atualização |\n")
        readme.write("|------------------|---------------|--------------------|\n")

        for mod_name, mod_url in mods_json.items():
            # Aqui estamos verificando o status do mod. Adiciona "Atualizado" ou "Desatualizado".
            status = "Desatualizado"
            content = fetch_content(mod_url)

            # Verificando o status do mod
            if content:
                try:
                    mod_data = json.loads(content)
                    if mod_data:
                        status = "Atualizado"
                        # Aqui você deve salvar o conteúdo do arquivo en_us.json no seu repositório local
                        en_us_path = f"mods/{mod_name}/en_us.json"
                        os.makedirs(os.path.dirname(en_us_path), exist_ok=True)
                        save_json_to_file(en_us_path, mod_data)
                except json.JSONDecodeError:
                    status = "Erro ao processar o JSON"

            # Adiciona a linha da tabela no README
            last_update = datetime.now().strftime('%Y-%m-%d')
            readme.write(f"| **{mod_name}** | {status} | {last_update} |\n")

def main():
    mods_json_path = 'scripts/mods.json'  # Caminho do arquivo mods.json
    readme_path = 'README.md'  # Caminho do README
    mods_json = load_json_from_file(mods_json_path)

    # Exemplo de como adicionar novos mods
    mods_to_check = {
        "Vinery": "https://github.com/satisfyu/Vinery/blob/1.20.1/common/src/main/resources/assets/vinery/lang/en_us.json",
        # Adicione mais mods conforme necessário
    }

    # Mantém apenas os links no mods.json
    for mod_name, mod_url in mods_to_check.items():
        mods_json[mod_name] = mod_url

    # Salvando o mods.json atualizado (agora sem o status)
    save_json_to_file(mods_json_path, mods_json)

    # Atualizando o README com o status
    update_readme(mods_json, readme_path)

    print("Atualização concluída.")

if __name__ == '__main__':
    main()

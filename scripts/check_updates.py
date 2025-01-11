import os
import json
import requests
from datetime import datetime

# Caminhos importantes
MODS_DIR = "mods"
MODS_FILE = "scripts/mods.json"
README_FILE = "README.md"

# Função para baixar o conteúdo de um URL
def fetch_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Função para verificar atualizações de mods
def check_updates():
    with open(MODS_FILE, "r", encoding="utf-8") as f:
        mods = json.load(f)
    
    overall_status = []
    
    for mod_name, url in mods.items():
        mod_dir = os.path.join(MODS_DIR, mod_name)
        os.makedirs(mod_dir, exist_ok=True)

        en_us_path = os.path.join(mod_dir, "en_us.json")
        pt_br_path = os.path.join(mod_dir, "pt_br.json")
        mod_readme_path = os.path.join(mod_dir, "README.md")
        
        # Baixa o conteúdo do arquivo original
        try:
            latest_content = fetch_content(url)
        except requests.RequestException as e:
            print(f"Erro ao baixar {mod_name}: {e}")
            continue

        # Verifica se o arquivo já existe
        if os.path.exists(en_us_path):
            with open(en_us_path, "r", encoding="utf-8") as f:
                current_content = f.read()
        else:
            current_content = None

        # Salva o novo arquivo
        with open(en_us_path, "w", encoding="utf-8") as f:
            f.write(latest_content)

        # Verifica mudanças
        status = "Atualizado" if current_content == latest_content else "Desatualizado"
        date = datetime.now().strftime("%Y-%m-%d")

        # Atualiza o README individual
        with open(mod_readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {mod_name.capitalize()}\n\n")
            f.write(f"**Status**: {status}\n\n")
            f.write(f"**Última atualização**: {date}\n")

        # Coleta status geral
        overall_status.append({
            "name": mod_name.capitalize(),
            "status": status,
            "last_update": date
        })

    # Atualiza o README principal
    update_readme(overall_status)

# Função para atualizar o README principal
def update_readme(status_list):
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write("# Traduções de Mods para Minecraft\n\n")
        f.write("Este repositório contém traduções de mods para Minecraft. O status das traduções é monitorado automaticamente.\n\n")
        f.write("## 📜 Lista de Mods\n\n")
        f.write("| Mod              | Status        | Última Atualização |\n")
        f.write("|-------------------|---------------|--------------------|\n")
        for mod in status_list:
            f.write(f"| **{mod['name']}** | {mod['status']}    | {mod['last_update']}         |\n")
        f.write("\n")

if __name__ == "__main__":
    check_updates()

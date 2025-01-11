# Contribuindo para o Minecraft Mods Translations

Obrigado por seu interesse em contribuir para o projeto de traduções de mods do Minecraft! Este projeto visa fornecer traduções para mods populares do Minecraft, facilitando a experiência para jogadores que preferem jogar em português do Brasil.

Se você gostaria de contribuir, siga as etapas abaixo.

---

## 1. Verifique o Arquivo `mods.json`

Antes de começar, dê uma olhada no arquivo `mods.json` para ver quais mods já foram adicionados ao projeto. Ele lista todos os mods e seus links para os arquivos de tradução (`en_us.json`) originais.

---

## 2. Adicionando um Novo Mod

Para adicionar um novo mod ao projeto:

### 2.1. **Obtenha o Link para o Arquivo `en_us.json` Original:**

1. Vá até o repositório do mod no GitHub.
2. Encontre o arquivo de tradução `en_us.json`.
3. Copie a URL bruta (`raw.githubusercontent.com`) para esse arquivo. **Lembre-se** de que o link deve começar com `https://raw.githubusercontent.com/`.

### 2.2. **Adicione o Mod ao `mods.json`:**

1. Abra o arquivo `mods.json` no diretório raiz.
2. Adicione o nome do mod e o link no formato abaixo:

```json
{
    "NomeDoMod": "https://raw.githubusercontent.com/usuario/Mod/branch/paths/en_us.json"
}
```

### 2.3. **Criação das Pastas e Arquivos:**

O script irá automaticamente criar a pasta e os arquivos necessários para o mod dentro da pasta `mods/`. A estrutura será semelhante a:

```
mods/
└── NomeDoMod/
    ├── en_us.json
    ├── pt_br.json
    └── README.md
```

---

## 3. Atualizando Traduções

Quando um mod for atualizado, o script verifica automaticamente o link no arquivo `mods.json` para garantir que as traduções estão atualizadas. O arquivo `README.md` dentro da pasta do mod será atualizado para refletir se o mod está **"Atualizado"** ou **"Desatualizado"**.

### 3.1. **Status de Tradução**

No arquivo `README.md` de cada mod, o status da tradução será atualizado. Isso ajuda a manter o controle sobre quais mods já possuem traduções completas e quais precisam ser trabalhadas.

---

## 4. Contribuindo com Traduções

Se você deseja traduzir ou atualizar traduções para o português, basta seguir os passos abaixo:

1. **Abrir o arquivo `pt_br.json`** na pasta do mod.
2. **Adicionar ou alterar as traduções** conforme necessário.
3. **Salvar e enviar suas alterações** para o repositório.

### 4.1. **Como Funciona o Processo de Tradução:**

- O arquivo `en_us.json` contém as strings originais em inglês.
- O arquivo `pt_br.json` contém as traduções que você faz para o português.
- As traduções são feitas linha por linha, onde você substitui o texto em inglês pela tradução correspondente em português.

---

## 5. Enviando um Pull Request

Quando terminar suas alterações (adicionar mods ou atualizar traduções), faça o seguinte:

1. **Crie um fork** do repositório.
2. **Clone o repositório** para sua máquina local.
3. Faça as alterações necessárias e adicione os arquivos no seu fork.
4. **Crie um pull request** explicando o que foi feito:
   - Se for adicionar um mod, certifique-se de ter adicionado o link correto no `mods.json`.
   - Se for atualizar a tradução, detalhe qual parte foi alterada no `pt_br.json`.

---

## 6. Verificando o Status de Atualização

O script também mantém o status dos mods no arquivo `README.md` de cada mod. Ele marcará como **"Atualizado"** ou **"Desatualizado"** baseado em uma comparação entre o conteúdo do arquivo original `en_us.json` e a versão baixada. A ideia é manter os mods sempre atualizados com as traduções mais recentes.

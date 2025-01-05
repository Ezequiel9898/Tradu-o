# Central de Traduções - Mods do Minecraft

Este repositório contém as traduções de diversos mods do **Minecraft**. O objetivo é centralizar as traduções para facilitar a atualização e manter o controle sobre o estado de cada tradução.

## Status das Traduções

A tabela abaixo exibe o status atual das traduções de cada mod. O status é automaticamente atualizado após cada execução do processo de sincronização.

| Mod                    | Última Atualização | Status         | Detalhes                                      |
|------------------------|--------------------|----------------|-----------------------------------------------|
| **Projeto A**           | 2025-01-05         | ✅ Atualizado  | Traduções atualizadas para a versão mais recente. |
| **Projeto B**           | 2025-01-04         | ❌ Desatualizado| Traduções desatualizadas. Requer atualização. |
| **Projeto C**           | 2025-01-03         | ✅ Atualizado  | Traduções alinhadas com a versão mais recente. |

> **Nota**: As traduções podem ser desatualizadas se houver novas atualizações nos mods que não foram refletidas aqui.

## Como Funciona

Este repositório sincroniza as traduções de mods de Minecraft de outros repositórios. O processo é automatizado para garantir que todas as traduções estejam sempre atualizadas.

1. **Verificação Automática**: O workflow verifica periodicamente os repositórios de mods listados e atualiza as traduções no repositório central.
2. **Status Atualizado**: Após a sincronização, o `README.md` é automaticamente atualizado para refletir a data da última atualização e o status da tradução.

### Como Adicionar Novos Mods

Se você quiser adicionar um novo mod ao repositório de traduções, siga os passos abaixo:

1. **Adicione o Link do Repositório**: Edite o arquivo `repositorios.json` e adicione o link do repositório do mod no formato `usuario/repo`.
2. **Rodar a Sincronização**: O workflow automático irá clonar o repositório do mod, copiar as traduções e atualizar o status no `README.md`.

### Contribuindo

Se você deseja ajudar a manter ou melhorar as traduções, ou corrigir algo que tenha sido perdido na sincronização, basta fazer o seguinte:

1. **Fork o Repositório**: Faça um fork deste repositório e adicione suas contribuições.
2. **Envie um Pull Request**: Envie um PR com suas alterações, incluindo traduções ou ajustes de conteúdo no `README.md`.

## Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
### Feedback ou Sugestões?

Se você tem alguma sugestão para melhorar o processo de tradução ou qualquer outro aspecto do projeto, fique à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

# 🚀 Gerador de Planilhas para Hyboard

Este projeto gera automaticamente planilhas de saídas para facilitar o mapeamento de tags no **Hyboard** por **PLC**. Com ele, você pode exportar todas as tags da pasta de PLCs e configurar quais **types** e **datatypes** deseja incluir no arquivo final.

## 📌 Funcionalidades

✅ **Filtragem Personalizada**: Escolha quais tipos de tags (exemplo: `Motor`, `p_ain`, etc.) deseja incluir.
✅ **Mapeamento de Datatypes**: Configure a conversão de datatypes/libs existentes no PLC para o formato desejado.
✅ **Geração Automática**: Executando o `main.py`, as planilhas serão geradas na pasta `saidas`.

## 📂 Estrutura do Projeto

```
📁 projeto
 ├── 📁 plcs              # Pasta com arquivos de tags exportados
 ├── 📁 configs           # Configurações de tipos e datatypes
 ├── 📁 saidas            # Pasta onde as planilhas geradas serão salvas
 ├── 📝 README.md         # Documentação do projeto
 ├── 🐍 main.py           # Arquivo principal para geração das planilhas
```

## ⚙️ Como Usar

1. **Adicione os arquivos de tags** na pasta `plcs`.
2. **Configure os tipos** no arquivo de configurações (`configs/types.json`).
3. **Defina os datatypes** no arquivo `configs/datatypes.json`.
4. **Execute o script principal**:
   ```bash
   python main.py
   ```
5. **Encontre as planilhas geradas** na pasta `saidas`.

## 📌 Exemplo de Configuração

### `configs/types.json`
```json
{
    "types": ["p_din", "p_intotalizer", "p_ain", "motor"]
}
```

### `configs/datatypes.json`
```json
{
    "p_din": [".Sts", ".Sts_TgtDisagree"],
    "p_intotalizer": [".PV", ".Total_D", ".H_VAL_0", ".H_VAL_1", ".D_VAL_0", ".D_VAL_1", ".M_VAL_0", ".M_VAL_1"]
    ...
}
```

## 🛠 Tecnologias Utilizadas

- 🐍 **Python** → Processamento e geração de arquivos Excel
- 📊 **Pandas** → Manipulação de dados
- 📄 **OpenPyXL** → Criação e formatação de planilhas Excel

## 🤝 Contribuição

Sinta-se à vontade para sugerir melhorias, abrir issues ou fazer um fork do projeto! 🚀

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
🔹 Desenvolvido para facilitar o mapeamento de tags no **Hyboard**! 😉


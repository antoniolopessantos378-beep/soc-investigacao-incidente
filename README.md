# 🛡️ SOC Lab - Investigação de Incidente

Este projeto simula um cenário real de um analista de segurança em um Security Operations Center (SOC), focado na análise de logs e detecção de atividades suspeitas.

---

## 🎯 Objetivo

Identificar comportamentos anômalos, como tentativas de login falhadas e acessos suspeitos, simulando um possível ataque de força bruta.

---

## 🛠️ Tecnologias Utilizadas

- Linux (Kali Linux)
- Python
- Análise de logs

---

## 📂 Estrutura do Projeto

- `logs.txt` → Arquivo com eventos simulados
- `analise_logs.py` → Script para análise e detecção de ameaças

---

## 🔍 Análise Realizada

Durante a análise dos logs foi possível identificar:

- Múltiplas tentativas de login falhadas
- Login bem-sucedido após falhas (indicando possível ataque)
- Acesso a arquivos sensíveis

---

## 🚨 Detecção

O script identifica padrões suspeitos como:

- Ataque de força bruta
- Acessos incomuns
- Comportamentos anômalos

---

## ▶️ Como executar

```bash
python3 analise_logs.py

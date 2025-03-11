# Insta Charger 🕵️♂️📲

Script Python que automatiza a coleta de informações de posts do Instagram de casas de show em Fortaleza/CE, ajudando na escolha de programas de final de semana.

## Funcionalidades Principais
- Coleta automática do último post de cada perfil listado em `agenda.txt`
- Extração de dados como:
  - URL do flyer do evento
  - Detalhes das atrações
  - Horários de funcionamento
  - Informações sobre ingressos
- Classificação dos resultados por engajamento (curtidas)
- Geração automática do arquivo `resultados.txt`
- Barra de progresso visual durante a execução

## Pré-requisitos
- Python 3.x instalado
- Bibliotecas Python (executar no terminal):
```bash
pip install instaloader tqdm
```

## Instalação e Execução
1. Clonar repositório
```bash
git clone https://github.com/laerciomonteiro/insta-charger.git
```
2. Acesse o diretório:
```bash
cd insta-charger
```
3. Execute o script:
```bash
python3 insta-charger.py
```

## Configuração
1. Adicione os perfis do Instagram que deseja monitorar no arquivo `agenda.txt`
2. Um arquivo de exemplo está incluído para referência

## Saída
- Resultados armazenados em `resultados.txt`
- Ordenação automática dos posts mais populares (mais curtidos) para os menos populares

## Licença
`MIT License`

## Autor
**Laercio Monteiro**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/laercio-monteiro) 
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram)](https://instagram.com/laercio.monteiro_)

✉️ Contato profissional: laercio@betacoding.com.br

---

🔐 *Desenvolvido por um profissional de segurança com paixão por desenvolvimento de software e automação inteligente*


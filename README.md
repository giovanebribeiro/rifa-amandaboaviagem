# rifa-amandaboaviagem

App para a Rifa de Amanda Boaviagem, criado e hospedado via Streamlit: [streamlit.io/gboaviagem/cha-rifa-app](https://share.streamlit.io/gboaviagem/cha-rifa-app/main/app.py).

Banco de dados: MongoDB

## Configurações iniciais

Para as configurações iniciais para desenvolvimento, é recomendado o [pipenv](https://pypi.org/project/pipenv/)

Execute os seguintes comandos:

```
$ pipenv install
$ ./setup.sh # para criar a pasta .streamlit e os arquivos iniciais
$ pipenv shell # para executar o ambiente
```

Em seguida, edite o arquivo .streamlit/secrets.toml e adicione suas credenciais de banco de dados

Para executar a aplicação, rode o comando `streamlit hello`.

O objetivo do site é permitir que as pessoas selecionem rifas de forma online, e fazer escrita/leitura de um banco de dados onde esse registro fica armazenado. O site também permite que o usuário saiba quais rifas ele já selecionou previamente, e quantas (do total de 150) ainda estão disponíveis.

O script [`fetch_picked_numbers.py`](./fetch_picked_numbers.py) consulta o banco de dados e joga em `picked_numbers.csv` a relação das rifas e quem já escolheu alguma.

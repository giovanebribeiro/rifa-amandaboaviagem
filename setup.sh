mkdir -p ./.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ./.streamlit/config.toml

echo "\
[mongo] \n\
host = \"endereço do banco\"\n\
port = 27017\n\
username = \"usuario do banco\"\n\
password = \"senha para acesso ao banco\"\n\
\n\n\
[email] \n\
host = \"endereço do servidor de e-mail SMTP\"\n\
port = 465\n\
username = \"usuario do email\"\n\
password = \"senha do email\"\n\
" > ./.streamlit/secrets.toml

# Nslookup UOL Host

<img src='https://img.shields.io/badge/License-MIT-informational'>

# :computer: Sobre o projeto:
Nslookup UOL Host: O objetivo deste projeto é auxiliar pessoas que tenham dificuldades em verificar o **DNS** do seu domínio,
porém o sistema verifica somente se o seu domínio encontra-se no servidor do **UOL HOST**


## :pushpin: Pré-requisitos:
- Bibliotecas para o projeto: ```make requirements```

## :closed_lock_with_key: Arquivo .env:
- É preciso criar um arquivo com o nome .env na raiz do projeto, pois precisa conter dois parâmetros:
  - DEBUG= True ou False
  - SECRET_KEY=chave key do formulário

## :rocket: Executar o script:
- Para acessar a página web via localhost, basta digitar o comando:
  - ```make run```

- Caso queira rodar no heroku:
  - Crie um app no heroku com o nome: **specific-dns**
  - Execute o comando: ```make deploy```
  - Após finalizar, execute: ```make upload```

## :cloud: Acesso:
- Heroku: http://specific-dns.herokuapp.com/whois/
- Local: http://localhost:5000/whois/

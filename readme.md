# Nslookup UOL Host

# :computer: Sobre o projeto:
Nslookup UOL Host: O objetivo deste projeto é auxiliar pessoas que tenham dificuldades em verificar o **DNS** do seu domínio,
porém o sistema verifica somente se o seu domínio encontra-se no servidor do **UOL HOST**


## :pushpin: Pré-requisitos:
- Versão do Python: ```3.8.18```
- Bibliotecas para o projeto: ```make requirements```
- Adicionar na variável de ambiente: ```PYTHONPATH=. pytest```

## :closed_lock_with_key: Arquivo .env:
- É preciso criar um arquivo com o nome .env na raiz do projeto, pois precisa conter dois parâmetros:
  - DEBUG= True ou False
  - SECRET_KEY=chave key do formulário

## :rocket: Executar o script:
- Para acessar a página web via localhost, basta digitar o comando:
  - ```make run```

## :rocket: Executar testes:
  - ```make tests```

## :cloud: Acesso:
- Local: http://localhost:5000/whois/

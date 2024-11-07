FRAMEWORKS DESENVOLVIMENTO WEB

-> Nesta matéria vamos utilizar a linguagem: Python e o framework Flask; 
-> ORM - Mapeamento de Objeto Relacional: SQLAlchemy;

AULA 01 (09/10):
ANOTAÇÕES E FORMAS DE AVALIAÇÃO 

    Avaliação:
        1- Programação ao vivo (vamos receber o pedido 48h antes) - (11 e 18/12)
        2- Entrega do portifólio; (12/02)
        3- Aplicação prática com requisitos (22/01)
        vai ser a última atividade, precisa ter:
        pelo menos uma API desenvolvida por mim;
        tem que ter um end point documentados com períodos de entrada e saída;
        código limpo (nada de linhas de comentário);
        funcionando;
        com validações necessárias como entrada de dados, erro etc;
        BONUS se for uma aplicação elástica ou escalável;
        Tem que ter integração com banco de dados; 
        Os testes vão ser feitos seguindo a nossa documentação do projeto;
        Individual. 

    Revisar para a próxima aula:
        Criar um ambiente virtual do python com VENV (descobrir como criar pelo terminal tbm);
        Estar famiiarizado com linux...;
        Saber instalar pacote no Python;
        Extensões do Python - Python Venv (f1 e digitar create... criar ambiente virtual, criar um venv na minha versão do python), vai criar uma pasta oculta na pasta onde estou;
        executar o activate que tá na pasta;
        Vamos instalar pacotes para podermos usar nas aulas; 
        Requiriments - arquivo de dependências para replicar o ambiente virtual. É um arquivo TXT que vem com as dependencias que usamos + a versão; (é tipo packet json)
        -> dá pra gerar pelo próprio Python;
        Descobrir como gerar e usar pra poder testar;

    O python 3.11 pelo menos deve estar instalado na máquina; 

    SABER USAR LINUX!  

    Boas práticas:
        Nunca colocar código dentro da pasta do ambiente virtual;

    Aplicações WEB e não locais; 

AULA 2 (23/10):
CRIANDO UM AMBINETE VIRTUAL EM PYTHON:

    Passo a passo:
        - Criando o ambiente dentro do terminal do VSCode: python -m venv nome_do_ambiente
        - Autorizar a criação dos ambinetes (dentro do powershell) - necessário apenas 1 vez: 
            Get-ExecutionPolicy
            Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
        - Ativando o ambiente: nome_do_ambiente\Scripts\activate

        Para acessar venv depois de criado: 
        - Acessando o caminho: cd D:\Documentos Usuário\Documents\GitHub\FrameworksDesenvolvimentoWeb\projeto01
        - Ativando: ambiente1.venv\Scripts\activate
        - Desativando: deactivate

    Instalando dependencias:
        pip install nome_pacote
        pip list - exibe todos os pacotes instalados
    -> O que instalamos nessa primeira aula:
            flask
            flask sqlalchemy
            numpy - serve para manipular arrays, matrizes etc, é mais rápido que laços de repetição
    -> pypi - site que tem campo de busca de pacotes e como instalar.

    INSTALAMOS E RODAMOS BIBLIOTECAS SEMPRE DENTRO DO AMBIENTE VIRTUAL

    -> Nesta aula criamos as pastas: templates, static e pastas adjacentes. Além disso, o arquivo app.py - app.py é o arquivo principal que vamos utilizar;
    -> Utilizamos a barra de progresso e o tempo.

    * As aulas vão começar com uma lista de atividades, depois conceitos que vamos utilizar pra fazer essas atividades.

* PADÕRES DE ARQUIVO E ORGANIZAÇÃO DE CÓDIGO:
    - Frameworks trabalham com padrão;
    - Os arquivos html devem estar na pasta templates nessa primeira parte;
    - CÓDIGO LIMPO! ZERO COMENTÁRIOS E NOMES RELEVANTES; 
    - NOMES TODOS EM INGLÊS, NADA EM PORTUGUÊS - classes, variáveis, nomes, arquivos;
    - Variáveis snakecase (padrão da linguagem), nada de acentos ou caracteres especiais.

AULA 03 (30/10):
CRIANDO UM NOVO AMBIENTE VIRTUAL E DESENVOLVENDO CÓDIGOS:

    Sempre importar o Flask no começo: from flask import Flask

    -> TODA requisição web trabalha com RR (request and response)
    -> No ambiente web, ele funciona com requisições reativas pois só faz coisas se alguém pede
    -> O Flask permite com que o código Python fique escutando e esperando uma requisição, primeiro a 
    requisição chega no flask, chega no python e o python devolve a requisição 

        A primeira coisa a se fazer é criar a sua aplicação - ela vai ser do tipo flask para rodar aplicações web 

        A variável web pode ter qualquer nome, mas geralmente se usa app mesmo

            app.run(debug=True) - vai atualizar automáticamente o servidor
            para mudar a porta em que a aplicaçãoestá rodando: app.run(debug=True, port 'xxxx')
            isso vai disponibilizar a aplicação para todo mundo que estiver conectado na mesma rede que eu = app.run(debug=True, port 'xxxx', host = '0.0.0.0)
            
            Para a aplicação ser reativa, nós criamos as rotas, mas para isso, nós precisamos ter alguma função

           @app.route('/contact')
            def contact():
                return 'This is the user page'

            -> essa é a forma de criar diferentes páginas 

            criamos um novo app.py
            criamos páginsas para ele 
            aprendemos usar o HTML para usar no python
        
    1 - Crie uma rota para uma página web com a tag *canvas* que permite ao usuário deslocar uma fotografia para a direita e esquerda com as setinhas do teclado (rota:atividade 1)

    2 - Crie uma rota para a atividade 2 que permita ao usuário capturar uma fotografia pela webcam e mostrar na tela

    3 - Crie uma rota para a atividade 3 com a python app que exiba uma tabela (sem usar table) com 997 linhas e 5 colunas: nas colunas id, nome, sobre nome, email, ações.

    4 - Criar uma rota com 3 links, um para cada uma das atividades anteriores, porém todas elas bonitas

    5 - Criar 6 rotas, sendo cada uma estilizada, bonita e etc. Sendo que em cada rota deve conter o curriculo de um integrante do grupo. 

    TODOS ESSES PROJETOS DEVEM ESTAR EM UM PROJETO SÓ - DATA DE ENTREGA 05/11

    * Variável especial em python em que o nome da variável e o seu valor é a mesma coisa * pesquisar como isso funciona 

AULA 04 (06/11):

    render_template('index.html', nome = nome) - passando parâmetros de app para template

    1 - Considerando um usuário e uma senha mocados (dados fictícios) faça uma página de autenticação que retorne uma mensagem caso a autenticação funcionar (bom dia, tarde, noite a depender do horário), se não, diz que o login não bateu; - id "user" "key"

    2 - Limite as tentativas de autenticação do usuário em 2x, se ele errar duas vezes, tirar a opção de login e exibir uma mensagem de erro; - deixar uma div vazia com uma classe de resposta dentro

    3 - Estilizar de forma bonita a página de identificação; - colocar tudo dentro de uma div com class = container - estilizar o que está dentro

    4 - Escreva um script python que gere automáticamente um template HTML contendo um formulário para input de dados com os campos que serão recebidos por JSON; - gerar o html e o formulário e a outra parte recebe o JSON, trata ele e devolve como uma lista de strings

    5 - Incremente o script 4 para que após gerar o template, ele construa automáticamente uma rota que permita visualizar o template. - 
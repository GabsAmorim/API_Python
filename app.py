#1. Objetivo - Criar API que disponibiliza a consulta, criação, edição e exclusão de informações
#2. URL Base - localhost
#3. Endpoints - 
    # -localhost/reclamaçoes (GET) - Obter reclamação
    # -localhost/reclamaçoes (POST) - Criar novas reclamações
    # -localhost/reclamações/id (GET) - Obter reclamação por ID
    # -localhost/reclamações/id (PUT) - Editar reclamação por ID 
    # -localhost/reclamações/id (DELETE) - Deletar informação por ID 
#4. Quais recursos - Reclamações

from flask import Flask, jsonify, request

app = Flask(__name__)

reclamacoes = [
    {
            'id': 1,
            'nome': 'Aline Santos',
            'tipo': 'Buraco',
            'Status': 'Em andamento'
    },
    {
            'id': 2,
            'nome': 'Taylor Swift',
            'tipo': 'Asfalto',
            'Status': 'Concluido'
    },
    {
            'id': 3,
            'nome': 'Cassio Ramos',
            'tipo': 'Iluminação',
            'Status': 'Recusado'
    },
]

#Consultar todas as reclamações contidas na biblioteca criada
@app.route('/reclamacoes',methods=['GET']) #Aqui estamos criando a rota para executar a aplicação flaks criada acima, caso tivessemos um BD, iriamos referenciar a rota para o BD aqui
def obter_reclamacoes(): #Crinado uma função para obter as informações registradas na biblioteca criado  junto ao flask acima
    return jsonify(reclamacoes) #Retorno das informações obtidas
#Consultar por ID
@app.route('/reclamacoes/<int:id>',methods=['GET'])#Aqui é a mesma criação de tota anterior, porém, informando que também informamos que será esparada a informação de ID, lembrando, que também é especificado que só é permitido o metodo de GET na mesma
def obter_rec_por_id(id): #Crinado uma função para obter as informações registradas na biblioteca criado  junto ao flask acima esperando o retorno de ID
    for reclamacao in reclamacoes:#criada uma variavel para conversar com a biblioteca criada
        if reclamacao.get('id') == id: #Aqui estamos informando que caso o ID informado acima no obter_rec_por_id for compativel com algum ID contido na biblioteca, ele irá reclamar abaixo a reclamação
            return jsonify(reclamacao)#retorno da reclamação capturada pelo ID
#Editar por ID
@app.route('/reclamacoes/<int:id>',methods=['PUT'])#Mesma informação dita acima, porém aceita apenas metodo de PUT
def editar_rec_por_id(id):#Criando função para poder editar as reclamações de acordo com o ID informado
    reclamacao_alterada = request.get_json()#Criada a variavel que vai trocar a informação anterior pelo nova através de um request no json
    for indice,reclamacao in enumerate(reclamacoes):# for criado para a "seleção" das informações
        if reclamacao.get('id') == id:#Caso a o ID de informação fornecido pelo usuario exista, ele irá executar o codigo abaixo
            reclamacoes[indice].update(reclamacao_alterada)# Aqui ele está alterando as informações selecionadas de acordo com o indice na biblioteca
            return jsonify(reclamacoes[indice])#Aqui é retornada a nova informação
#Criar nova reclamação
@app.route('/reclamacoes', methods=['POST'])#Mesma lógica das anteriores, porém aceita apenas metodo POST
def incluir_nova_rec():#Criando a função para pode incluir reclamações
    nova_reclamacao = request.get_json()#Criação da variavel que será responsável pela inclusão da nova informação
    reclamacoes.append(nova_reclamacao)#Através da nova variavel daremos um append (a append vai criar as novas informações após todas as outras informações)
    return jsonify(reclamacoes)#Aqui temos o retorno da nova tabela
#Excluir por ID
@app.route('/reclamacoes/<int:id>', methods=['DELETE'])#Mesma lógica das anteriores, porém aceita apenas metodo DELETE
def excluir_rec(id):#Criando função para poder excluir as reclamações de acordo com o ID informado
    for indice, reclamacao in enumerate(reclamacoes):# for criado para a "seleção" das informações
        if reclamacao.get('id') == id:  #Aqui estamos informando que caso o ID informado acima no excluir_rec for compativel com algum ID contido na biblioteca, ele irá excluir a reclamação
            del reclamacoes[indice] #Aqui ele deleta a reclamação de acordo com o indice na biblioteca
    
    return jsonify(reclamacoes)#por fim ele reclama as reclamações contidas na tabela

app.run(port=5000,host='localhost',debug=True) #aqui estamos informando que o app flaks criado no começo do programa irá abrir através da porta 5000 do nosso localhost
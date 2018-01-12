## Crud
Create - push():
Cria insere um novo nó na arvore (coleção) e recebe como parâmetro um id que pode ser passada pelo o usuário e um dict com os dados.
    

Read - get():
O read deve possuir a opção de ser chamado com parâmetro ou não. Quando não for passado parâmetro, a função deverá retornar uma lista com todos os valores da coleção (todos os nós da arvore). Quando for passado o parâmetro, que é o id do item, a função retornará os dados apenas desse objeto.
    

Update - update():
Essa função deverá receber como parâmetro um dict com o que deve ser colocado nos dados da chave. A falta ou a adição de algum dado ao dict não deverá afetar a operação.

Delete - remove():
Delete existem duas possibilidades, com parâmetro ou sem parâmetro. Com parâmetro, a função remove somente a o nó referente a chave recebida. Sem parâmetro, a função removerá toda a coleção do banco de dados.
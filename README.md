# PROJETO 01 DA DISCIPLINA DE ORIENTAÇÃO À OBJETO

-----------------------FEIRINHA-----------------------
    O programa tem como objetivo facilitar compras em 
uma espécie de feira. O usuário pode entrar como admi-
nistrador, com um login e senha pré-definidos, ou pode
se registrar como cliente para que os produtos sejam 
entregues em sua residência.

---------------------CASOS DE USO---------------------
    CASO DE USO 1: Fazer pedido online.
Ator: Cliente
Descrição:
1.Cenário principal: 
- O cliente acessa o programa com o objetivo de fazer
suas compras.
- O programa pergunta se ele deseja acessar como cli-
ente ou administrador.
- Ele acessa como cliente e é perguntado nome, ende-
reço e número para contato.
- Após o registro, é mostrado a ele as opções de fru-
tas disponíveis e suas quantidades.
- Ele adiciona as que deseja, juntamente com a quanti-
dade, e pode finalizar o pedido. 
- Ele é informado do valor que deve pagar quando rece-
ber as frutas em sua residência.
2.Fluxo alternativo:
- O cliente pode retirar algum item do carrinho antes
de confirmar.
3.Exceções:
- Caso o cliente tente registrar alguma fruta indispo-
nível, ou alguma quantidade dela que não possui no es-
toque, ele será informado que não é possível prosseguir
com a adição do produto.

CASO DE USO 2: Renovar o estoque e confirmar que um 
cliente já recebeu seu pedido
Ator: Administrador
Descrição:
1.Cenário principal:
- Um trabalhador da feira renovou o estoque e deseja
adicionar ao programa.
- Ele entra no programa e seleciona a opção de entrar
como administrador.
- Ele coloca o login e a senha que o estabelecimento 
utiliza (já definido).
- Ele seleciona a opção de renovar o estoque e coloca 
o nome da fruta que deseja adicionar, além de quantas
unidades foram acrescentadas.
- O programa informa que conseguiu adicionar a quan-
tidade de frutas e, caso já houvesse algumas disponí-
veis no estoque, o programa informa a nova quantidade 
disponível.
2.Caso alternativo:
- Após renovar o estoque, o administrador deseja con-
firmar que um dos clientes já recebeu o pedido.
- Ele informa o nome do cliente e automáticamente
o cliente é removido da lista.
3.Exceções:
- Caso o nome do cliente que ele deseja confirmar en-
trega não esteja cadastrado, o trabalhador é informa-
do que o cliente não possui registro.

LOGIN E SENHA PARA ADMNISTRADOR: login123 senha321



# Projeto-Redes

Aplicação cliente e outra servidora, em que:

O servidor é “uma sala” de bate-papo em grupo, onde os clientes irão se conectar (não havendo
qualquer limite de clientes conectados).

Com protocolo de transporte TCP para que haja o controle das conexões.

Os clientes conectados poderão enviar e receber mensagens para o servidor (ou seja, para todos
“da sala”).

Quando um cliente envia mensagens para “a sala”, o servidor deverá encaminhá-las para todos
os demais clientes conectados, bem como mostrá-las em sua tela (terminal). Neste ponto, tanto
os clientes quanto o servidor devem exibir as mensagens nas suas respectivas telas.

foi implementado com threads e sockets.

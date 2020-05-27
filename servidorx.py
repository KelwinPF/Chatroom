import socket
import _thread
import os
import sys

HOST = '127.0.0.1'      
PORT = 5000             
clients=[]#ip e porta dos clientes
Apelidos=[]#apelidos dos clientes
privados=[]#quem esta com quem e atualmente em privado
aux4= []#indice de quem recebeu o pedido de privado
aux6 =[]#nome de quem recebeu o pedido de privado
aux5 =[]#nome de quem fez pedido de privado
aux8 =[]#indice de quem fez o pedido de privado

def conectado(con, cliente):
    print('\nO cliente entrou:', cliente)
    while True:
        i=0
        j=0
        k=0
        l=0
        m=0
        teste =0 
        auxliarprivados=0
        msg = con.recv(1024).decode("utf8")
        if (msg != '/lista') and (msg.split(" ")[0] != '/nome') and (msg != '/sair') and (msg.split(" ")[0] != '/privado') and (msg != '/aceitarprivado') and (msg != '/sairprivado') and (msg != '/recusarprivado'):
            if con not in clients:
                clients.append(con)
                aux =  msg.split(" ")[0]
                Apelidos.append(aux)
                while j<len(clients):
                    if(clients[j] != con):
                        clients[j].send((aux + ' entrou na sala!').encode("utf8"))
                        j = j+1
                    else:
                        j=j+1
            if not msg:
                break
            print(msg)
            ms = msg.encode("utf8")
            while i<len(clients):
                if (aux in aux6):
                    while(k<len(privados)):
                        if(aux == privados[k].split(" ")[0]):
                            while l<len(aux5):
                                if(aux==aux5[l]):
                                    auxiliarprivados=l
                                l=l+1
                            clients[aux8[auxiliarprivados]].send(('[PRIVADO]' + msg).encode("utf8"))
                            clients[aux4[auxiliarprivados]].send(('[PRIVADO]' + msg).encode("utf8"))
                        k=k+1
                    break
                elif(aux in aux5):
                    while(k<len(privados)):
                        if(aux == privados[k].split(" ")[0]):
                            while m<len(aux5):
                                if(aux==aux5[m]):
                                    auxiliarprivados=m
                                m=m+1
                            clients[aux8[auxiliarprivados]].send(('[PRIVADO]' + msg).encode("utf8"))
                            clients[aux4[auxiliarprivados]].send(('[PRIVADO]' + msg).encode("utf8"))
                        k=k+1
                    break
                else:
                    if (Apelidos[i] in aux6):
                        i=i+1 
                    elif(Apelidos[i] in aux5):
                        i=i+1
                    else:
                        clients[i].send(ms)
                        i = i+1                     
                            
        elif msg.split(" ")[0]=='/nome':
            while i<len(clients):
                if(msg.split(" ")[2]==Apelidos[i]):
                    Apelidos[i] = msg.split(" ")[1]
                    aux = msg.split(" ")[1]
                i=i+1
        elif msg == '/sairprivado':           
            while i<len(privados):
                if(privados[i].split(" ")[0] == aux):
                    ps = privados[i].split(" ")[1]
                    ps2 = aux + ' ' + ps
                    ps3 = ps + ' ' + aux
                    privados.remove(ps2)
                    privados.remove(ps3)
                    while j<len(aux5):
                        if(aux==aux5[j]):
                            auxiliarprivados = j
                        if(aux ==aux6[j]):
                            auxiliarprivados = j
                        j=j+1
                    clients[aux8[auxiliarprivados]].send(('sala desfeita').encode("utf8"))
                    clients[aux4[auxiliarprivados]].send(('sala desfeita').encode("utf8"))
                    x = aux5[auxiliarprivados]
                    y = aux6[auxiliarprivados]
                    z = aux4[auxiliarprivados]
                    v = aux8[auxiliarprivados]
                    aux5.remove(x)                    
                    aux6.remove(y)
                    aux4.remove(z)
                    aux8.remove(v)
                i = i + 1
        elif msg == '/recusarprivado':
            if (aux not in aux6):
                con.send(('voce nao recebeu pedido de privado').encode("utf8"))
            else:
                while j<len(aux5):
                    if(aux==aux5[j]):
                        auxiliarprivados = j
                    if(aux ==aux6[j]):
                        auxiliarprivados = j
                    j=j+1
                con.send(('voce recusou o pedido de privado! ').encode("utf8"))
                clients[aux8[auxiliarprivados]].send((aux6[auxiliarprivados] + ' recusou seu pedido de privado').encode("utf8"))
                a = aux5[auxiliarprivados]
                b = aux6[auxiliarprivados]
                c = aux4[auxiliarprivados]
                d = aux8[auxiliarprivados]

                aux5.remove(a)
                aux6.remove(b)
                aux4.remove(c)
                aux8.remove(d)
                        
        elif msg == '/aceitarprivado':
            if (aux not in aux6):
                con.send(('voce nao recebeu pedido de privado').encode("utf8"))
            else:
                while j<len(aux5):
                    if(aux==aux5[j]):
                        auxiliarprivados = j
                    if(aux==aux6[j]):
                        auxiliarprivados = j
                    j=j+1
                p1 = aux6[auxiliarprivados]
                p2 = aux5[auxiliarprivados]
                privados.append(p1 + ' ' + p2 )
                privados.append(p2 + ' ' + p1 )
                clients[aux8[auxiliarprivados]].send((aux + ' aceitou seu privado, agora voces estao conversando em privado').encode("utf8"))
        elif msg == '/sair':
            print(aux + ' saiu da sala') 
            clients.remove(con)
            Apelidos.remove(aux)
            con.close()
            _thread.exit()
        elif msg.split(" ")[0] == '/privado':
            if (aux in aux6):
                con.send(('ja esta em privado com alguem').encode("utf8"))
            elif(aux in aux5):
                con.send(('ja esta em privado com alguem').encode("utf8"))
            elif(msg.split(" ")[1] == aux):
                con.send(('não pode fazer privado com voce mesmo!').encode("utf8"))
            else:
                aux5.append(aux)
                while i<len(Apelidos):
                    if(aux==Apelidos[i]):
                        aux8.append(i)
                    i=i+1
                while j<len(Apelidos):
                    if(msg.split(" ")[1]==Apelidos[j]):
                        aux6.append(Apelidos[j])
                        aux4.append(j)
                        teste=j
                    j = j + 1
                clients[teste].send((aux + ' quer falar com voce em privado! digite /aceitarprivado para aceitar e /recusarprivado para recusar!').encode("utf8"))
        else:
            mgaux = 'Lista de Conectados:'
            con.send(mgaux.encode("utf8"))
            while i<len(clients):
                con.send((Apelidos[i] + '|').encode("utf8"))
                i = i+1      
    con.close()
    _thread.exit()
    
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
 

tcp.bind(orig)
 

tcp.listen(2)

os.system('cls' if os.name == 'nt' else 'clear') 
print('       ___------__')
print(' |\__-- /\       _-')
print(' |/    __      -')
print(' //\  /  \    /__')
print(' |  o|  0|__     --_')
print(' \\____-- __ \   ___-')
print(' (@@    __/  / /_')
print('    -_____---   --_')
print('     //  \ \\   ___-')
print('   //|\__/  \\  \-')
print('   \_-\_____/  \-')
print('        // \\--\|')   
print('   ____//  ||_')
print('  /_____\ /___\.')
print(' SONIC MESSENGER\n')
print('SERVIDOR INICIADO', HOST, 'na porta', PORT)
while True:
    con, cliente = tcp.accept() 
    _thread.start_new_thread(conectado, tuple([con, cliente]))
tcp.close()




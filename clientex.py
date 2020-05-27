from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
import os
import sys

class Send:
 def __init__(self):
  self.__msg=''
  self.new=True
  self.con=None
 def loop(self):
  return self.new
 def env(self,msg):
  self.__msg=msg
  if self.con != None:
   self.con.send(str.encode(self.__msg))


def esperar(tcp,send,host='localhost',port=5000):
 destino=(host,port)
 tcp.connect(destino)
 while send.loop():
  if flag == 1:
    break
  send.con=tcp

  while send.loop():
   msg=tcp.recv(1024) 
   if not msg: break
   print(msg.decode("utf8"))


if __name__ == '__main__':

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
 print('digite o IP do servidor')
 host=input()
 print('Digite seu apelido : ')
 apelido = input()  

 tcp=socket(AF_INET,SOCK_STREAM)
 send=Send()
 flag=0
 processo=Thread(target=esperar,args=(tcp,send,host))
 processo.start()
 print('')
  
 msg=input()
 msg2 = (apelido +' disse: ')
 if (msg=='/lista'):
    msg='/lista'
 else:
    msg = (msg2+msg)

 while True:
  send.env(msg)
  msg=input()
  msg2 = (apelido +' disse: ')
  if (msg=='/lista'):
      msg='/lista'
  elif (msg.split(" ")[0]=='/nome'):
      msg = msg + " " + apelido
      apelido = msg.split(" ")[1]
  elif(msg=='/sair'):
      flag=1
      os.system('cls' if os.name == 'nt' else 'clear') 
      msg='/sair'
      send.env(msg)
      break
  elif(msg.split(" ")[0] == '/privado'):
      print('aguardando aceitaçao/rejeicao do pedido!')
  elif(msg=='/aceitarprivado'):
        msg='/aceitarprivado'
  elif(msg=='/recusarprivado'):
        msg='/recusarprivado'
  elif(msg=='/sairprivado'):
        msg='/sairprivado'
  else:
      msg = (msg2+msg)

 processo.join()
 tcp.close()
 exit()


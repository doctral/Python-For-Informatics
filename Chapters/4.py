import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mess='GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
mysock.send(mess.encode('utf-8'))
while True:
      data = mysock.recv(512)
      if ( len(data) < 1 ) :
            break
      print (data.decode('utf-8'))
    
mysock.close()

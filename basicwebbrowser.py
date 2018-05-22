import socket

#@create socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#@establish connection
mysock.connect(('data.pr4e.org', 80))

#@send GET request followed by a blank line per http protcol
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    #receive data until recv() returns an empty string, then break
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    #print data receieved
    print(data.decode(),end='')

mysock.close()

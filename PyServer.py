# Import python libraries
from socket import *

# Create Server
def createServer():
    # Creating the Server Socket (end point of protocol based communication) 
    #There will be a client socket(browser socket) on the other end
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        # Binding the call from the client. 9000 is port number
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while(1):
            # Accepting the call from the client. At this point server-client 
            # communication has been established  
            (clientsocket, address) = serversocket.accept()
            
            # reading the message (Get request) sent from the client.
            #  Client socket is a server socket here for a specific client
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])
            
            # Returning what client has asked for 
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            
            # Closing the client socket 
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)
    # Closing the Server socket
    serversocket.close()

print('Access http://localhost:9000')
createServer()

import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.101"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        """
        self.id = self.connect()
        print(self.id)
        """
        
    def getPos(self):
        return self.pos
   
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
  
        
        """  
        def connect(self):
            try:
                self.client.connect(self.addr)
                return self.client.recv(2048).decode()
            except Exception as e:
                print(f"Error al conectar: {e}")
                return "0,0" #Devuelve una posición
        """
        
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

        
n = Network()
print(n.send("hello"))
print(n.send("working"))
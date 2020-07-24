from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(ForkingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("got connection from", addr)
        self.wfile.write(b'connected')


server = Server(('', 9999), Handler)
server.serve_forever()

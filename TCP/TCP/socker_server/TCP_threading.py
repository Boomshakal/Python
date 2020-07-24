from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler


class Server(ThreadingMixIn, TCPServer): pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print("got connection from", addr)
        self.wfile.write(b"connected")


server = Server(('', 9999), Handler)
server.serve_forever()

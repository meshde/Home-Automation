import tornado.web
import tornado.websocket
import tornado.escape
import json

class Handler(object):
	def __init__(self):
		pass
	def set_connection(self,conn):
		self.conn = conn
		return
	def write(self,message):
		self.conn.write_message(message)
		return

class Server(tornado.web.RequestHandler):

	def initialize(self,handler):
		self.handler = handler
		return

	def get(self):
		self.write("HELLO\n")
		pass

	def post(self):
		# data = tornado.escape.json_decode(self.request.body)
		# print data['light']
		data = self.request.body
		self.handler.write(data)

class Connection(tornado.websocket.WebSocketHandler):
	def initialize(self,handler):
		self.handler = handler
		pass

	def open(self):
		print "Opened"
		self.handler.set_connection(self)
		return

	def on_message(self,message):
		print message
		self.write_message("Acknowledged!\n")
		return

	def on_close(self):
		print "Closed"
		return
def main():
	handle = Handler()
	app = tornado.web.Application([
		(r"/",Server,{'handler':handle}),
		(r"/meh",Connection,{'handler':handle})
		])

	app.listen(8080)

	tornado.ioloop.IOLoop.instance().start()

	return

if __name__ == '__main__':
	main()
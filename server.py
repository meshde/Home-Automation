import tornado.web
import tornado.websocket
import json

# class Handler(object):
# 	def __init__(self):
# 		pass
# 	def set_connection(self,conn):
# 		self.conn = conn
# 		return
# 	def write(self,message):
# 		self.conn.write(message)
# 		return
class Server(tornado.web.RequestHandler):

	def initialize(self):
		pass

	def get(self):
		self.write("HELLO\n")
		pass

class Connection(tornado.websocket.WebSocketHandler):
	def initialize(self):
		pass

	def open(self):
		print "Opened"
		return

	def on_message(self,message):
		print message
		self.write_message("Acknowledged!\n")
		return

	def on_close(self):
		print "Closed"
		return
def main():
	# handle = Handler()
	app = tornado.web.Application(
		[
		(r"/",Server),
		(r"/meh",Connection)])

	app.listen(8080)

	tornado.ioloop.IOLoop.instance().start()

	return

if __name__ == '__main__':
	main()
import websocket
import json

def on_message(ws,message):
	print message
	mes = raw_input("Enter your message:\t")
	ws.send(mes)
	return

def on_close(ws):
	print "### CLOSED ###"
	return

def on_error(ws):
	return

def on_open(ws):
	print "### OPENED ###"
	return

def main():
	websocket.enableTrace(True)

	ws = websocket.WebSocketApp(
		"ws://localhost:8080/meh",
		on_message = on_message,
		on_error = on_error,
		on_close = on_close)

	ws.on_open = on_open
	ws.run_forever()

if __name__ == '__main__':
	main()

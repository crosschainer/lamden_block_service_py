from db import mongo_connector
import websocket
import _thread
import time
import rel
import json
import logging

class BlockService:
    blockservice_port = None
    database = None
    currentBlock = 1

    masternode = "wss://masternode-01.lamden.io"
    websocket_connection = None

    def on_message(ws, message):
        logging.debug(message)

    def on_error(ws, error):
        logging.debug(error)

    def on_close(ws, close_status_code, close_msg):
        logging.debug("Websocket connection closed")

    def on_open(ws):
        logging.debug("Opened websocket connection")

    def startup(self, port):
        self.blockservice_port = port
        self.database = mongo_connector.get_database()
        self.websocket_connection = websocket.WebSocketApp(self.masternode,
                              on_open=self.on_open,
                              on_message=self.on_message,
                              on_error=self.on_error,
                              on_close=self.on_close)
        self.websocket_connection.run_forever()

if __name__ == "__main__":
    log = logging.getLogger("Blockservice")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    blockservice = BlockService()
    blockservice.startup(port=1337)
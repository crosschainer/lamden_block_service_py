from db import mongo_connector
from urllib.request import urlopen, Request
import json
import logging

class BlockService:
    blockservice_port = None
    database = None
    currentBlock = 1

    masternode = "https://masternode-01.lamden.io"

    def getNewBlock(self, block_id):
        block_info = urlopen(Request(self.masternode + "/blocks?num=" + str(block_id), headers={'User-Agent': 'Mozilla'}))
        return json.loads(block_info.read())

    def startup(self, port):
        self.blockservice_port = port
        self.database = mongo_connector.get_database()
        logging.debug(self.getNewBlock(self.currentBlock))


if __name__ == "__main__":
    log = logging.getLogger("Blockservice")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    blockservice = BlockService()
    blockservice.startup(port=1337)
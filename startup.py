from db import mongo_connector

class BlockService:
    blockservice_port = None

    masternode = "https://masternode-01.lamden.io"

    def getNewBlocks(currentBlock):
        pass
    
    def startup(self, port):
        self.blockservice_port = port

blockservice = BlockService()
blockservice.startup(port=1337)
class BaseWorker(object):
    def __init__(self, data: dict):
        raise NotImplementedError
    
    def run(self, data: dict) -> dict:
        raise NotImplementedError

    def getFunctions(self) -> dict:
        raise NotImplementedError
        

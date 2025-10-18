from datetime import datetime, timedelta
from typing import Dict, Any

class Cache():
    def __init__(self):
        self.values : Dict[str, Dict[str, Any]] = {}
    
    def set(self, key: str, value: str, expiry : int=-1):
        expiry_value = datetime.now() + timedelta(seconds=expiry) if expiry != -1 else expiry
        self.values[key] = {'value':value, expiry:expiry_value}
        return value

    def get(self, key):
        val = self.values[key]
        if val is not None:
            if val['expiry'] == -1:
                return val['value']
            now = datetime.now()
            expiry = val['expiry']
            if now > expiry:
                self.values[key] = None
                return None
            return val['value']
        return None
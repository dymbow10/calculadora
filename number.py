from dataclasses import dataclass

@dataclass
class Number:
    integer: str
    decimal: str
    def getNumber(self): return float(self.integer+'.'+self.decimal)
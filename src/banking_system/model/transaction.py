from datetime import datetime


class Transaction:
    
    def __init__(self, transaction_id: str, transaction_type: str, amount: float, transaction_date: datetime):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.transaction_date = transaction_date
        
    
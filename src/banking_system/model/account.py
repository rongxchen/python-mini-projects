from typing import List
from datetime import datetime
from src.banking_system.model.user import User
from src.banking_system.model.transaction import Transaction
from src.util import id_util


class Account:
    
    def __init__(self, account_number: int, user_id: str, account_type: str):
        self.account_number = account_number
        self.user_id = user_id
        self.account_type = account_type
        self.balance = 0.0
        self.transactions: List[Transaction] = []
        self.user_info = None
        
    
    def set_user(self, user: User):
        self.user_info = user
        
        
    def check_balance(self):
        print(f"Balance: [{self.balance}]")
        print("=" * 80)
        
    
    def check_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction.__dict__)
        print("=" * 80)
        
    
    def deposit(self, amount: float):
        transaction = Transaction(
            transaction_id=id_util.generate_id(),
            transaction_type="deposit",
            amount=amount,
            transaction_date=datetime.now(),
        )
        self.balance += amount
        self.transactions.append(transaction)
        
    
    def withdraw(self, amount: float):
        if self.balance < amount:
            print(f"Insufficient balance: [{self.balance}]")
            return
        transaction = Transaction(
            transaction_id=id_util.generate_id(),
            transaction_type="withdraw",
            amount=amount,
            transaction_date=datetime.now(),
        )
        self.balance -= amount
        self.transactions.append(transaction)

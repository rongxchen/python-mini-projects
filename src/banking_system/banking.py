from typing import List
from src.banking_system.model.user import User
from src.banking_system.model.account import Account
from src.banking_system.enum.enum import AccountType
from src.util import id_util, number_util


class BankingSystem:
    
    def __init__(self):
        self.users: List[User] = [
            User(user_id=id_util.generate_id(), username="user1", password="0000"),
            User(user_id=id_util.generate_id(), username="user2", password="0000"),
            User(user_id=id_util.generate_id(), username="user3", password="0000"),
        ]
        self.accounts: List[Account] = [
            Account(account_number=number_util.generate_numbers(8), user_id=self.users[0].user_id, account_type=AccountType.SAVINGS.value),
            Account(account_number=number_util.generate_numbers(8), user_id=self.users[1].user_id, account_type=AccountType.SAVINGS.value),
            Account(account_number=number_util.generate_numbers(8), user_id=self.users[2].user_id, account_type=AccountType.SAVINGS.value),
        ]
        self.curr_user = None
        self.curr_account = None
        
        
    def __find_account(self, user_id: str):
        for account in self.accounts:
            if account.user_id == user_id:
                return account
        return None
        
    
    def login(self, username: str, password: str):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None
    
    
    def transfer(self, from_account: int, to_account: int, amount: float):
        from_account: Account = self.__find_account(from_account)
        to_account: Account = self.__find_account(to_account)
        if not to_account:
            print(f"Account not found: [{to_account}]")
            print("=" * 80)
            return
        if from_account.balance < amount:
            print(f"Insufficient balance: [{from_account.balance}]")
            print("=" * 80)
            return
        from_account.withdraw(amount)
        to_account.deposit(amount)
    
    
    def auth_menu(self):
        while True:
            print("1. Check balance")
            print("2. Check transactions")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.curr_account.check_balance()
            elif choice == "2":
                self.curr_account.check_transactions()
            elif choice == "3":
                amount = float(input("Enter amount: "))
                self.curr_account.deposit(amount)
            elif choice == "4":
                amount = float(input("Enter amount: "))
                self.curr_account.withdraw(amount)
            elif choice == "5":
                to_account = int(input("Enter from account: "))
                amount = float(input("Enter amount: "))
                self.transfer(self.curr_account.account_number, to_account, amount)
            elif choice == "6":
                break
            else:
                print("Invalid choice")
            print("=" * 80)
    
    
    def run(self):
        while True:
            print("1. Login")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = self.login(username, password)
                if user:
                    print(f"Welcome {user.username}")
                    print("=" * 80)
                    self.curr_user = user
                    self.curr_account = self.__find_account(user.user_id)
                    self.auth_menu()
                else:
                    print("Invalid credentials")
                    print("=" * 80)
            elif choice == "2":
                break
            else:
                print("Invalid choice")
                print("=" * 80)
    

def main():
    banking_system = BankingSystem()
    banking_system.run()

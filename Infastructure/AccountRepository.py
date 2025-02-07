class AccountRepository:
    def __init__(self):
        self.accounts = {}
        self.transactions = {}

    def save_account(self, account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id):
        return self.accounts.get(account_id)

    def find_accounts_by_customer_id(self, customer_id):
        return [account for account in self.accounts.values() if account.customer_id == customer_id]

    def find_transactions_by_account_id(self, account_id):
        return self.transactions.get(account_id, [])

    def save_transaction(self, transaction):
        if transaction.account_id not in self.transactions:
            self.transactions[transaction.account_id] = []
        self.transactions[transaction.account_id].append(transaction)
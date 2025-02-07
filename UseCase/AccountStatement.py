class AccountStatement:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise AccountNotFoundError("Account not found")

        transactions = self.account_repository.find_transactions_by_account_id(account_id)

        statement = f"Account Statement for Account Number: {account.account_number}\n"
        for transaction in transactions:
            statement += f"Transaction: {transaction.transaction_type}, Amount: {transaction.amount}\n"
        statement += f"Current Balance: {account.get_balance()}"
        return statement

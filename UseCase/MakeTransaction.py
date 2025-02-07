from Domain.Transaction import Transaction
from exceptions import AccountNotFoundError, InvalidTransactionTypeError


class MakeTransaction:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise AccountNotFoundError("Account not found")

        if transaction_type == 'deposit':
            account.deposit(amount)
            transaction = Transaction(account_id, 'deposit', amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
            transaction = Transaction(account_id, 'withdraw', amount)
        else:
            raise InvalidTransactionTypeError("Invalid transaction type")

        self.account_repository.save_account(account)
        return transaction

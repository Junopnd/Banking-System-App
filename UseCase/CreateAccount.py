import uuid
from Domain.Customer import Customer
from Domain.Account import Account


class CreateAccount:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer_id, name, email, phone_number):
        customer = Customer(customer_id, name, email, phone_number)
        account_number = self._generate_account_number()
        account = Account(self._generate_account_id(), customer_id, account_number)
        self.account_repository.save_account(account)
        return customer, account

    def _generate_account_id(self):
        return uuid.uuid4()

    def _generate_account_number(self):
        return "1234567890"

import uuid
from Domain.Customer import Customer
from Infastructure.AccountRepository import AccountRepository
from UseCase.AccountStatement import AccountStatement
from UseCase.CreateAccount import CreateAccount
from UseCase.MakeTransaction import MakeTransaction


def main():
    account_repository = AccountRepository()
    create_account_use_case = CreateAccount(account_repository)
    make_transaction_use_case = MakeTransaction(account_repository)
    generate_statement_use_case = AccountStatement(account_repository)

    customer_id = uuid.uuid4()
    #customer_name = input("Enter customer name: ")
    #customer_email = input("Enter customer email: ")
    customer_name = "Jastine Melody Pineda"
    customer_email = "agentmelody@example.com"
    customer_phone = "123-456-7890"

    #while True:
    #    customer_phone = input("Enter customer phone number: ")
    #    try:
    #        int(customer_phone)
    #        break
    #    except ValueError:
    #        print("Invalid phone number. Please enter numbers only.")

    customer, account = create_account_use_case.create_account(customer_id, customer_name, customer_email, customer_phone)

    make_transaction_use_case.make_transaction(account.account_id, 100, 'deposit')
    #make_transaction_use_case.make_transaction(account.account_id, 50, 'withdraw')

    statement = generate_statement_use_case.generate_account_statement(account.account_id)

    print("\nAccount Statement:")
    print(f"  Name: {customer.name}")
    print(f"  Email: {customer.email}")
    print(f"  Phone: {customer.phone_number}")
    print(f"  UUID: {customer.customer_id}")
    print(f"\n{statement}")

    make_transaction_use_case.make_transaction(account.account_id, 50, 'withdraw')
    statement = generate_statement_use_case.generate_account_statement(account.account_id)
    print("\nYou've withdrawn 50 from your account")
    print(f"\n{statement}")


if __name__ == "__main__":
    main()

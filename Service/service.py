from Domain.domain import Account, Customer

class CreateAccountUseCase:
    def create_account(self, customer_id, name, email, phone_number):
        # Assume account_number is generated somehow
        account_number = "ACC123456"
        customer = Customer(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
        account = Account(account_id=None, customer_id=customer_id, account_number=account_number)
        # Additional logic to save the account data in the repository
        return account


class TransactionUseCase:
    def make_transaction(self, account_id, amount, transaction_type):
        # Additional logic to fetch account from repository
        account = Account(account_id, customer_id=None, account_number=None)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        # Additional logic to save the updated account data in the repository


class GenerateStatementUseCase:
    def generate_account_statement(self, account_id):
        # Additional logic to fetch account and transaction data from repository
        account = Account(account_id, customer_id=None, account_number=None)
        # Additional logic to generate statement string based on transactions
        statement = f"Account Statement for Account ID {account_id}:\nBalance: {account.get_balance()}"
        return statement
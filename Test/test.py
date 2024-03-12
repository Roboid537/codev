from Service.service import CreateAccountUseCase, TransactionUseCase, \
    GenerateStatementUseCase

def test_banking_system():
    # Creating instances
    create_account_use_case = CreateAccountUseCase()
    transaction_use_case = TransactionUseCase()
    generate_statement_use_case = GenerateStatementUseCase()

    # Creating a new account
    new_account = create_account_use_case.create_account(
                                            customer_id="CUST123",
                                            name="John Doe",
                                            email="john@example.com",
                                            phone_number="1234567890")

    # Making transactions
    transaction_use_case.make_transaction(
                                    account_id=new_account.account_id,
                                    amount=1000,
                                    transaction_type='deposit')
    transaction_use_case.make_transaction(
                                    account_id=new_account.account_id,
                                    amount=500,
                                    transaction_type='withdraw')

    # Generating account statement
    statement = generate_statement_use_case.generate_account_statement(
                                            account_id=new_account.account_id)

    # Displaying results
    print(statement)


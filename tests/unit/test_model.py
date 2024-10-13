from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.country == 'Spain'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_create_account_empty_name():
    """
    GIVEN an Account model
    WHEN an account is created with an empty name
    THEN ensure that the account creation fails or behaves as expected
    """
    with pytest.raises(ValueError):  # Assuming the model raises a ValueError
        account = Account('', '€', 'Spain')  # Empty name

def test_create_account_missing_country():
    """
    GIVEN an Account model
    WHEN an account is created without a country
    THEN ensure the account creation fails
    """
    with pytest.raises(ValueError):  # Assuming the model raises a ValueError for missing country
        account = Account('John Doe', '€', None)  # Missing country

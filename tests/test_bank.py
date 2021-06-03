"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account


@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_accounts_are_immutable():
    account = Account('Immutable')
    with pytest.raises(Exception):
        # This operation should raise an exception
        account.name = 'Mutable'


def test_bank_creates_empty(bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_cannot_duplicate_accounts(bank):
    bank.create_account('duplicate')
    bank.create_account('duplicate')

    assert len(bank.accounts) == 1


def test_cannot_modify_accounts_set(bank):
    accounts = bank.accounts
    accounts.append(Account('New Account'))

    assert len(bank.accounts) == 0


def test_add_funds(bank):
    bank.create_account('Test')
    bank.add_funds('Test', 30)

    assert bank.transactions[-1].amount == 30

def test_add_funds_nonexisting_account(bank):
    with pytest.raises(ValueError):
        bank.add_funds('Test', 30)

def test_add_funds_not_number(bank):
    bank.create_account('Test')
    with pytest.raises(ValueError):
        bank.add_funds('Test', 'a')

def test_add_funds_all_numbers(bank):
    try:
        bank.create_account('Test')
        bank.add_funds('Test', 30)
        bank.add_funds('Test', 30.0)
        bank.add_funds('Test', '30')
    except ValueError:
        pytest.fail()

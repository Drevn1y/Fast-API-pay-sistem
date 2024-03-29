from database import get_db
from database.models import Transfer, UserCard
from datetime import datetime


# Проверка карты
def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()
    return exact_card


# Создание перевода
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    # Проверка на наличии обеих карт в бд
    checker_card_from = validate_card(card_from, db)
    checker_card_to = validate_card(card_to, db)

    # Если обе карты существует в БД то делаем транзакцию (перевод)
    if checker_card_from and checker_card_to:
        # Проверить балланс отправителя
        if checker_card_from.balance >= amount:
            # Минусуем у того кто отправляет деньги
            checker_card_from.balance -= amount
            # Добавляем тому кто получает
            checker_card_to.balance += amount

            # Создаем платеж в БД
            new_transaction = Transfer(card_from_number=checker_card_from.card_number,
                                       card_to_number=checker_card_to.card_number,
                                       amount=amount,
                                       transaction_data=datetime.now)
            db.add(new_transaction)
            db.commit()

            return 'Перевод успешно выполнен'
        else:
            return 'Недостаточно средст на карте!'
    else:
        return 'Одна из карт не существует!'


# Получить все переводы по карте, то есть История
def get_history_transaction(cart_from_number):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(cart_from_number=cart_from_number).all()

    if card_transaction:
        return card_transaction
    else:
        return 'Нету истории!'


# Отмена транзакции
def cancel_transaction_db(card_form, card_to, amount, transfer_id):
    db = next(get_db())

    # Проверка на наличии обеих карт в бд
    checker_card_form = db.query(Transfer).filter_by(card_form, db)
    checker_card_to = db.query(Transfer).filter_by(card_to, db)

    if checker_card_form and checker_card_to:
        transaction_to_cancel = db.query(Transfer).filter_by(transfer_id=transfer_id).first()

        if transaction_to_cancel:
            checker_card_form.balance += amount
            checker_card_to -= amount
            transaction_to_cancel.status = False

            db.delete(transaction_to_cancel)
            db.commit()

            return 'Транзакция отменена'
        else:
            return 'Транзакция не найдена'

    else:
        return 'Одна из карт не существует!'



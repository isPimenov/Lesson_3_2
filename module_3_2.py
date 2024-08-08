def email_check(mail, end = ['.com', '.ru', '.net']):
    for i in end:
        if mail.endswith(i):
            return True
    return False


def send_email(message, recipient, sender="university.help@gmail.com"):
    if not '@' in recipient and not '@' in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if not email_check(recipient) or not email_check(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}."')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru' ,
           'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание' , 'urban.student@mail.ru' ,
           'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре' , 'urban.teacher@mail.ru' ,
           'urban.teacher@mail.ru')



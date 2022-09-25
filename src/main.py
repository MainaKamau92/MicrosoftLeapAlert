import logging
from datetime import datetime

from mail import EmailDispatcher
from scrap import scrap_leap_instance


def dispatch_reminder():
    logging.info("Dispatching Microsoft leap reminder @ %s", datetime.now())
    scrapped_data = scrap_leap_instance.parse_events()
    logging.info("Scrapped data: %s", scrapped_data)
    title = scrapped_data[0][1]
    terms = scrapped_data[1][1]
    email_dispatcher = EmailDispatcher(
        email="example@gmail.com",  # to email
        subject=title,
        terms=terms
    )
    email_dispatcher.send_email()


if __name__ == "__main__":
    dispatch_reminder()

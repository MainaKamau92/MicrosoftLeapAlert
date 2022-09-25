import os
import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv

load_dotenv()


class EmailDispatcher:
    def __init__(self, email: str, subject: str, terms: str) -> None:
        self.from_email = os.getenv("FROM_EMAIL")
        self.to_email = email
        self.subject = subject
        self.terms = terms
        self.API_KEY = os.getenv('SENDGRID_API_KEY')
        self.sendgrid_client = SendGridAPIClient(self.API_KEY)

    def _prepare_html_content(self) -> str:
        html_content = "<ul>"
        for term in self.terms:
            html_content += f"<li>{term}</li>"
        html_content += "</ul>"
        return html_content

    def prepare_mail_content(self) -> Mail:
        return Mail(
            from_email=self.from_email,
            to_emails=self.to_email,
            subject=self.subject,
            html_content=self._prepare_html_content())

    def send_email(self) -> None:
        try:
            message = self.prepare_mail_content()
            response = self.sendgrid_client.send(message)
            logging.info("Email sent successfully: %s", response.status_code)
        except Exception as e:
            breakpoint()

            logging.error("Error sending email: %s", e)






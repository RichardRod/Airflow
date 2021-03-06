from airflow.models import BaseOperator
from airflow.utils import send_email
from airflow.utils import apply_defaults


class EmailOperator(BaseOperator):

    template_fields = ('subject', 'html_content')

    __mapper_args__ = {
        'polymorphic_identity': 'EmailOperator'
    }

    @apply_defaults
    def __init__(
            self,
            to,
            subject,
            html_content,
            *args, **kwargs):
        """
        Sends an email.

        :param to: list of emails to send the email to
        :type to: list or string (comma or semicolon delimited)
        :param subject: subject line for the email (templated)
        :type subject: string
        :param html_content: content of the email (templated), html markup
            is allowed
        :type html_content: string
        """
        super(EmailOperator, self).__init__(*args, **kwargs)
        self.to = to
        self.subject = subject
        self.html_content = html_content

    def execute(self, execution_date):
        send_email(self.to, self.subject, self.html_content)

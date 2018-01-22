from django.db import models
from django.conf import settings
from ..questions.models import Question
from django.utils.translation import gettext_lazy as _


# answer model
class Answer(models.Model):
    # primary key
    id = models.AutoField(_('id'), auto_created=True, primary_key=True)
    # id to question object, on which need answer
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('question id'),
                                    db_column='question_id')
    # id user object, who create answer
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user id'),
                                db_column='user_id')
    # text answer
    text = models.TextField(_('text'), max_length=30000, db_column='text',
                            help_text=_('Required. 30000 character limit. Answer the question.'),
                            validators=[],
                            error_messages={
                                'invalid': _('Your answer not valid. Check text and try again.'),
                            })
    # date when answer was created
    date_created = models.DateTimeField(_('date_created'), db_column='date_column', auto_now_add=True)

    class Meta:
        verbose_name = 'Answers'
        db_table = 'answers'

    # return str object. Example: Answer №1 to №1 question by Vasiliy
    def __str__(self):
        return 'Answer №' + str(self.id) + ' to №' + str(self.question_id) + ' question, by ' + self.user_id.username


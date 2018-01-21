from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# question model
class Question(models.Model):
    # primary key
    id = models.AutoField(_('id'), auto_created=True, primary_key=True)
    # id to user object, who created this question
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user id'),
                                db_column='user_id')
    # title of question
    title = models.CharField(_('title'), max_length=180, db_column='title',
                             help_text=_('Required. 180 character or fewer.'),
                             validators=[],
                             error_messages={
                                 'invalid': _('Enter a valid title.'),
                             })
    # text question
    text = models.TextField(_('text'), max_length=30000, db_column='text',
                            help_text=_('Required. 30000 character or fewer. Ask a question.'),
                            validators=[],
                            error_messages={
                                'invalid': _('Your question not valid. Check text and try again.'),
                            })
    # date when questions was created
    date_created = models.DateTimeField(_('date created'), db_column='date_created', auto_now_add=True)

    class Meta:
        verbose_name = 'Questions'
        db_table = 'questions'

    # return str object. Example: Question №3 by Vasiliy
    def __str__(self):
        return 'Question №' + str(self.id) + ' by ' + str(self.user_id.username)







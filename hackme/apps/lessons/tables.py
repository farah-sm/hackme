from .models import Lesson
from table import Table
from table.utils import A
from table.columns import Column, CheckboxColumn, LinkColumn, Link


class LessonTable(Table):
    x = CheckboxColumn(field='', header='')
    id = Column(field='id', header='S/N', attrs={'class': "user-name"})
    name = Column(field='name', header='Name', attrs={
                  'class': 'custom user-name'}, header_attrs={'search': True}, searchable=False)
    lesson_format = Column(field='lesson_format',  header='Format',
                           searchable=False, attrs={'class': "user-name"})
    action = LinkColumn(header='Action',
                        links=[Link(text='Edit', viewname='lessons:edit', args=(A('id'),)),
                               Link(text='View', viewname='lessons:show', args=(A('id'),))],
                        delimiter=" | ")

    class Meta:
        model = Lesson
        attrs = {'class': 'table-bordered'}
        sort = [
            (0, 'asc'),
            (1, 'asc'),
            (2, 'asc')
        ]
        search = True
        pagination = True
        info = True
        zero_records = "No Records"
        # ext_button = True
        # ext_button_template = "My btn"
        # ext_button_template_name = "The btn"

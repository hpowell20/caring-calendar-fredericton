from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class TodoModel(Model):
    class Meta:
        simple_name = 'todos'

    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    description = UnicodeAttribute(null=True)
    is_complete = NumberAttribute(default=False)
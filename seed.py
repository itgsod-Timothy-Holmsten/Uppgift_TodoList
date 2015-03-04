
from pony.orm import db_session
from Todo.Models.models import Todo, Tag


with db_session:
    coffe=Tag(name='coffe')
    breakfast=Tag(name='breakfast')
    Todo(text="buy milk", tags=[coffe, breakfast])



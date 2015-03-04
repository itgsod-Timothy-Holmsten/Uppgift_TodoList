from pony.orm import PrimaryKey, Required, Set
from Todo import db

class Todo(db.Entity):
    id = PrimaryKey(int, auto=True)
    tags = Set("Tag")
    text = Required(str)


class Tag(db.Entity):
    todos = Set(Todo)
    name = PrimaryKey(str)






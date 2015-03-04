from pony.orm import db_session, select
import flask.ext.restful as rest

from ..Models.models import *

from Todo import api

from flask import request, abort


@api.resource('/todo/<int:id>')
class TodoAPI(rest.Resource):

    def get(self, id):

        with db_session:
            todo = Todo[id]

            if todo is None:
                return abort(404)

            return {
                "id": id,
                "tags": todo.tags,
                "text": todo.text
            }, 200

    def put(self, id):

        text = request.json.get('text', None)
        tags = request.json.get('tags', None)

        with db_session:
            todo = Todo[id]

            if not todo:
                return abort(404)
            else:
                if text:
                    todo.text = text
                if tags:
                    todo.tags = tags

        return {"todo": "updated"}, 202

    def delete(self, id):

        with db_session:
            todo = Todo[id]

            if todo is None:
                return abort(404)
            todo.delete()

        return {"delete": "todo %s" % id}, 200

@api.resource('/todos')
class Todos(rest.Resource):

    def get(self):

        with db_session:
            result = {}

            for todo in select(todo for todo in Todo):
                tags = []
                for tag in todo.tags:
                    tags.append(tag.name)
                    print tag
                result[todo.id] = {'text': todo.text, 'tags': tags}
            print result
            return result

    def put(self):

        if request.json is None:
            return abort(415)

        try:
            text = request.json.get('text')
            tags = request.json.get('tags', None)

        except KeyError, e:
            return abort(400)

        with db_session:
            tag_list = []
            for tag in tags:
                tag_list.append(Tag(name=tag))
            todo = Todo(text = text, tags = tag_list)
            db.commit()

            print tag_list.all()
            return {"id": todo.id, "text": todo.text, "tags": tag_list}



























from flask import Blueprint, jsonify
from .model import TodoModel
from .resource import TodoSchema
from webargs.flaskparser import use_kwargs

import logging
logger = logging.getLogger(__name__)
blueprint = Blueprint('todo', __name__)


@blueprint.route('/todos', methods=["GET"])
def list_todo_items():
    todo_items = TodoModel.scan()
    #return jsonify(todo_items.data)
    return jsonify(todo_items.dump({}).data)

    # response = []
    #
    # for account in accounts:
    #     response.append({
    #         'id': account.id,
    #         'name': account.name,
    #         'email': account.email
    #     })
    #
    # return jsonify(response)


@blueprint.route('/todos', methods=["POST"])
@use_kwargs(TodoSchema, locations=('json',))
def add_todo_item(**kwargs):
    todo_item = TodoModel(id=kwargs['id'],
                          title=kwargs['title'],
                          description=kwargs['description'],
                          is_complete=False)

    todo_item.save()
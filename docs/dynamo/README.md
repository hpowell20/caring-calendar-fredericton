## Working with DynamoDB ##

### Setup ###

* Add DynamoDB table definitions into `cloudformation/cfndsl_base.yaml` file
* Create / update the tables in the account by recreating the CloudFormation file and updating the stack
* Create new PynamoDB models for each table (name the file _model.py_)
    * Ensure the the simple_name attribute aligns with the table name; for example:
```
            class TodoModel(Model):
                class Meta:
                    simple_name = 'todos'
```
* Include the new classes in the `MODELS` list in `core/db.py` so they can be registered for use by PynamoDB

## Working with Services ##

### Setup ###

* Create a folder inside _services_ which relates to the actions being performed (for example: user)
* Create the following baseline files:
    * routes.py - Blueprint definitions (REQUIRED)
    * resource.py - Mapping of fields used in serialization / deserialization of JSON (OPTIONAL)
    * model.py - Mapping of fields used with PynamoDB (OPTIONAL)
* Update the `SERVICE_NAMES` list in `core/init.py` to include the new blueprints for use
    * The list entry must match the created folder name
* Sample APIs exist in the _examples_ folder


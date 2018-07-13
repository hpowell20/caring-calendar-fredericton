## Project Information ##

The serverless framework provides the ability to create and run the services within AWS.  The application
is deployed as a ZIP package to Lambda with API Gateway acting as a proxy to direct requests to Lambda.
Once inside Lambda Flask is used to handle routing to API endpoints.  This section provides documentation
on the main features of the starter kit as well as some how to guides.

### Structure ###

The main structure of the project consists of the following:

* apidocs - Swagger documentation for the APIs
* cloudformation - Collection of scripts used to setup AWS services and infrastructure
* configs - Configuration files for deployment (and local) environments
* core - Main startup and utility classes used by the application
* docs - Examples and how to guides
* scripts - Utility scripts which are used to supplement deployment and runtime (for example: creation of a user pool)
* services - Route, resource, and model definitions used for endpoints and business logic

### How To Guides ###

* [Working with Cognito](./cognito/README.md)
* [Working with DynamoDB](./dynamo/README.md)
* [Working with Services](./services/README.md)


## Working with Cognito ##

### User Pool Setup ###

* From the command line, run the _scripts/create_cognito_user_pool.py_ script by providing the AWS profile details and
environment to be created (dev, stage, uat, etc.)
* Record the values for the user pool ARN, user pool ID, and client ID as produced by the script
* Update the following environment specific configuration values:
    * user_pool_arn
    * user_pool_id
    * app_client_id
    * **NOTE:** These user pool ID and app client ID are also used by client applications

### Authentication ###

Each endpoint is secured using the Cognito authorizer service as defined in the following section within
the _serverless.yaml_ file:
```
          authorizer:
            arn: ${self:custom.env.user_pool_arn}
```

*NOTES:*

* Tokens need to be included in the _Authorization_ header
* Commenting these lines will remove authentication for endpoints when deployed to AWS
* When running the application locally token authentication is not enforced regardless of settings

### Token Generation ###

Each client (web / mobile) will provide a user token with each request after having authenticated
user credentials with Cognito.  However, there are several mechanisms within the project which allow for API
testing independent of a client application.

* The first is to use the _services/auth_cognito_user.py_ script (works locally and deployed to AWS)
* The second is the API endpoint _api/login_ as described in the _handlers/login.py_ file
    * The application must be deployed to AWS to access this method as the code is run within Lamdba



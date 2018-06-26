#!/usr/bin/env python
import argparse
import os
import boto3

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# =======================================================================
# Read input parameters
# =======================================================================
parser = argparse.ArgumentParser()
parser.add_argument('login', type=str, help='User login')
parser.add_argument('password', type=str, help='User password')
parser.add_argument('-p', '--profile', required=True,
                    help='AWS CLI profile to use')
parser.add_argument('-s', '--stage',
                    help='Stage name or environment such as dev, stage, uat, etc.', required=True)
args = parser.parse_args()

# =======================================================================
# Initialize boto3
# =======================================================================
session = boto3.Session(profile_name=args.profile)
cognito_idp_client = session.client('cognito-idp')

# =======================================================================
# Set variables
# =======================================================================
# user_pool_id = args.user_pool_id
username = args.login
password = args.password

# Find the details of the user pool
stage = args.stage
prefix = 'caring-fred'
user_pool_name = '{}-{}'.format(prefix, stage)

response = cognito_idp_client.list_user_pools(
    MaxResults=60
)

for user_pool in response['UserPools']:
    if user_pool['Name'] == user_pool_name:
        user_pool_id = user_pool['Id']

if user_pool_id:
    # Create the user
    arguments = {
        'Username': username,
        'TemporaryPassword': password,
        'MessageAction': 'SUPPRESS'
    }

    response = cognito_idp_client.admin_create_user(
        UserPoolId=user_pool_id,
        **arguments
    )

    # Authenticate the user
    response = cognito_idp_client.list_user_pool_clients(
        UserPoolId=user_pool_id,
        MaxResults=60
    )

    for user_pool_client in response['UserPoolClients']:
        if user_pool_client['ClientName'] == user_pool_name:
            client_id = user_pool_client['ClientId']

        if client_id:
            response = cognito_idp_client.admin_initiate_auth(
                UserPoolId=user_pool_id,
                ClientId=client_id,
                AuthFlow='ADMIN_NO_SRP_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': password,
                },
            )

            if response.get('ChallengeName') == 'NEW_PASSWORD_REQUIRED':
                response = cognito_idp_client.admin_respond_to_auth_challenge(
                    UserPoolId=user_pool_id,
                    ClientId=client_id,
                    ChallengeName='NEW_PASSWORD_REQUIRED',
                    ChallengeResponses={
                        'USERNAME': username,
                        'PASSWORD': password,
                        'NEW_PASSWORD': password,
                    },
                    Session=response['Session'],
                )

            print('User created')
        else:
            print('No matching app client defined for user pool id {}'.format(user_pool_id))
else:
    print('No user pool exists with name {}'.format(user_pool_name))

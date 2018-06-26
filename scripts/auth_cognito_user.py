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
parser.add_argument('-u', '--user_pool_id', required=True,
                    help='Cognito user pool ID')
parser.add_argument('-c', '--client_id', required=True,
                    help='Cognito pool app client ID')
args = parser.parse_args()

# =======================================================================
# Initialize boto3
# =======================================================================
session = boto3.Session(profile_name=args.profile)
cognito_idp_client = session.client('cognito-idp')


# =======================================================================
# Set variables
# =======================================================================
user_pool_id = args.user_pool_id
client_id = args.client_id
username = args.login
password = args.password

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
        ClientId= client_id,
        ChallengeName='NEW_PASSWORD_REQUIRED',
        ChallengeResponses={
            'USERNAME': username,
            'PASSWORD': password,
            'NEW_PASSWORD': password,
        },
        Session=response['Session'],
    )

# Print the retrieved token
print(response.get('AuthenticationResult', {}).get('IdToken'))
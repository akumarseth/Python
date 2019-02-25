## AADTokenCredentials for multi-factor authentication
from msrestazure.azure_active_directory import AADTokenCredentials
import adal, uuid, time
from getpass import getpass

def authenticate_device_code():
    """
    Authenticate the end-user using device auth.
    """
    authority_host_uri = 'https://login.microsoftonline.com'
    tenant = '******.onmicrosoft.com'
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.core.windows.net/'
    client_id = '*****'

    context = adal.AuthenticationContext(authority_uri, api_version=None)
    code = context.acquire_user_code(resource_uri, client_id)
    print(code['message'])
    mgmt_token = context.acquire_token_with_device_code(resource_uri, code, client_id)
    credentials = AADTokenCredentials(mgmt_token, client_id)

    return credentials


def authenticate_client_key():
    """
    Authenticate using service principal w/ key.
    """
    authority_host_uri = 'https://login.microsoftonline.com'
    tenant = 'eycloudappdev.onmicrosoft.com'
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.core.windows.net/'
    client_id = '******'
    client_secret = '*******'

    context = adal.AuthenticationContext(authority_uri, api_version=None)
    mgmt_token = context.acquire_token_with_client_credentials(resource_uri, client_id, client_secret)
    credentials = AADTokenCredentials(mgmt_token, client_id)

    return credentials
	
	
def authenticate_client_cert():
    """
    Authenticate using service principal w/ cert.
    """
    authority_host_uri = 'https://login.microsoftonline.com'
    tenant = '<TENANT>'
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.core.windows.net/'
    client_id = '******'
    client_cert = '*******'
    client_cert_thumbprint = '******'

    context = adal.AuthenticationContext(authority_uri, api_version=None)

    mgmt_token = context.acquire_token_with_client_certificate(resource_uri, client_id, client_cert, client_cert_thumbprint)
    credentials = AADTokenCredentials(mgmt_token, client_id)

    return credentials
	
def authenticate_username_password():
    """
    Authenticate using user w/ username + password.
    This doesn't work for users or tenants that have multi-factor authentication required.
    """
    authority_host_uri = 'https://login.microsoftonline.com'
    tenant = 'eycloudappdev.onmicrosoft.com'
    authority_uri = authority_host_uri + '/' + tenant
    resource_uri = 'https://management.core.windows.net/'
    username = '*******'
    password = getpass('Enter Password')
    client_id = '******'

    context = adal.AuthenticationContext(authority_uri, api_version=None)
    mgmt_token = context.acquire_token_with_username_password(resource_uri, username, password, client_id)
    credentials = AADTokenCredentials(mgmt_token, client_id)

    return credentials

if __name__ == '__main__':
	creds = authenticate_username_password()
	print(creds) 

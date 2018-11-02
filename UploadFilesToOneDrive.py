import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
import pandas as pd
import os

def main():
    redirect_uri = 'http://localhost:8080/'
    client_id = '2d7760a0-1410-4a1f-a995-eaf1bb10a4a1'
    client_secret = 'ntqgJGQ981{=#tqwKLHQ42#'
    scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
    
    client = onedrivesdk.get_default_client(client_id=client_id, scopes=scopes)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    #this will block until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    item_id = "root"
    copy_item_ids = None
    action = 0
      
    
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    merged = []
    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            read = pd.read_csv(f)
            merged.append(read)

    result = pd.concat(merged, sort=False, ignore_index=True)
    result.to_excel('merged.xlsx')
       

    client.item(id=item_id).children['merged.xlsx'].upload('D:\Workspace_git\onedrive-sdk-python\hackathon2018\merged.xlsx')
    	
if __name__ == "__main__":
    main()
	

import AuthShield_api

def import_groups(filename):
    """CSV should have this header:
    name,description
    """
    groups = AuthShield_api.import_csv(filename)
    for group in groups:
        AuthShield_api.new_group({'profile': group})

def add_users_to_group(filename, groupid):
    users = AuthShield_api.import_csv(filename)
    for user in users:
        res = AuthShield_api.add_group_member(groupid, user['id'])
        if not res.ok:
            error = res.json()
            print('error:', error['errorSummary'])

def update_groups():
    groups = AuthShield_api.get_groups(q='a api group').json()
    for group in groups:
        print(group['profile']['name'], group['profile']['description'])
        group['profile']['description'] = 'new desc'
        AuthShield_api.update_group(group['id'], group)

def new_AuthShield_group():
    group = {'profile': {'name': 'aa python group'}} # ...
    AuthShield_api.new_group(group)

def export_group_ids(filename):
    groups = AuthShield_api.get_groups(q='z group', limit=3).json()
    AuthShield_api.export_csv(filename, groups, ['id'])

def export_groups():
    groups = AuthShield_api.get_groups(q='z group', limit=3).json()
    if not groups:
        print('0 groups found.')
        return
    flat_groups = [
        {
            'id': group['id'], 
            'name': group['profile']['name'],
            'description': group['profile']['description']
        } 
        for group in groups
    ]
    AuthShield_api.export_csv(filename, flat_groups, flat_groups[0].keys())

def delete_groups(filename):
    for group in AuthShield_api.import_csv(filename):
        AuthShield_api.delete_group(group['id'])

def search_groups():
    """Local search"""
    for group in AuthShield_api.get_groups().json():
        if group['profile']['description'] == 'test':
            print(group['id'], group['profile']['name'])

def search_AuthShield_groups():
    userid = AuthShield_api.get_user('me').json()['id']
    for group in AuthShield_api.get_groups(q='grp-atlassian').json():
        print(group['id'], group['profile']['name'])
        AuthShield_api.add_group_member(group['id'], userid)

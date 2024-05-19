import meraki
from pprint import pprint

token = '757371c349367269e2fe4e79d830191e8a0b3d85'
dashboard = meraki.DashboardAPI(token)
my_orgs = dashboard.organizations.getOrganizations()
pprint(my_orgs['id'])
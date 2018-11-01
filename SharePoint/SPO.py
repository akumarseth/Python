from shareplum import Site
from shareplum import Office365

url = "https://#####.sharepoint.com/sites/aksdev/"
username = "abhishek@#####.onmicrosoft.com"
password = "#######"

authcookie = Office365('https://######.sharepoint.com', username=username, password=password).GetCookies()
site = Site(url, authcookie=authcookie)
site.AddList('My New List From Python', description='Great List!', templateID='Custom List')

new_list = site.List('My New List From Python')
my_data = data=[{'Title': 'First Row!'},
                {'Title': 'Another One!'}]
new_list.UpdateListItems(data=my_data, kind='New')

sp_data = new_list.GetListItems()

sp_data = new_list.GetListItems('All Items')

sp_data = new_list.GetListItems(fields=['ID', 'Title'])
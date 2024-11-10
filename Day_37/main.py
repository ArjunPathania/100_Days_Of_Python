import requests
import os
from datetime import  datetime

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# account_creation = requests.post(url=pixela_endpoint,json=user_params)
# print(account_creation.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN":TOKEN
}

graph_parameters = {
    "id":"nov2024graph1",
    "name":"Reading",
    "unit":"pages",
    "type":"int",
    "color":"shibafu"

}
# graph_create_request = requests.post(url=graph_endpoint,json=graph_parameters,headers= header)
# print(graph_create_request.text)

today = datetime(year=2024,month=11,day=9)
# today_str = f"{today.year}{today.month}{today.day}"
# using the strftime method
# print(today.strftime("%Y%m%d"))


pixel_endpt = f"{pixela_endpoint}/{USERNAME}/graphs/nov2024graph1"

quantity = 10

pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":str(quantity)
}

# pixel_req = requests.post(url=pixel_endpt,json=pixel_params,headers=header)
# print(pixel_req.text)

pixel_update_endpt = f"{pixela_endpoint}/{USERNAME}/graphs/nov2024graph1/{today.strftime("%Y%m%d")}"
pixel_update_params = {
    "quantity":str(quantity)
}
# pixel_update_req = requests.put(url=pixel_update_endpt,json=pixel_update_params,headers=header)
# print(pixel_update_req.text)

pixel_delete_req = requests.delete(url=pixel_update_endpt,headers=header)
print(pixel_delete_req.text)

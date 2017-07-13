import requests
import json
url = "https://57ee3429-c78f-4d83-8240-cf87f19c0233-bluemix:0881095de995d6379248c9231d071c32ccacf5a9db81d82cd448d5002b6792b4@57ee3429-c78f-4d83-8240-cf87f19c0233-bluemix.cloudant.com/"
def get_database(endpoint):
    get_request = requests.get("{}{}".format(url,endpoint))
    print(get_request.json())

def put_dbs(db_name):
    put_request = requests.put(("{}{}".format(url,db_name)))
    print(put_request.json())


def delete_dbs(db_name):
    delete_request = requests.delete("{}{}".format(url,db_name))
    print(delete_request.json())


def post_doc(db_name,doc_body):
    post_doc = requests.posttest4=requests.post(
        "{}{}".format(url,db_name),
        headers = {"Content-Type":"application/json"}, data = json.dumps(doc_body)
    )
    print(post_doc.json())

people2 = {"gino": {"name":"gino","age":"20","height":"175"}, "mike": {"name":"mike","age":"14","height":"170"}}
get_database("_all_dbs")
put_dbs("joel2")
get_database("_all_dbs")

for key in people2:
    people2[key]["_id"] = people2[key]["name"]
    post_doc("joel2",people2[key])
get_database("joel2/_all_docs")
delete_dbs("joel2")

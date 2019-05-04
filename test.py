import oci
from urllib import request, parse
import json

configfile = "c:\\oci\\config_ctd"
config = oci.config.from_file(configfile)

authtoken = "jhalkfdsjjhsajkdfhskjdhfsakljhfsjhalskjfhderewre"

identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
RootCompartmentID = user.compartment_id
print("RootID: {} ".format(RootCompartmentID))
print("Logged in as: {} @ {}".format(user.description, config["region"]))

workshopgroup = "f34052c061a94574908d1947a48999ce"
admingroup = "ocid1.group.oc1..aaaaaaaa63j5kkufv4mggyhawooi4pdwbpsi77kngzth7h2ffqyjh27zxzeq"

id_provider = "ocid1.saml2idp.oc1..aaaaaaaaypucmhaxy5s7j6wu7rff2wj7y46zlglklwaahtnsmmfkqgdfltpq"

users = oci.pagination.list_call_get_all_results(identity.list_users, compartment_id=RootCompartmentID, identity_provider_id=id_provider).data

usercount = 0
for user in users:
    name = user.name
    if name.find("@oracle.com") == -1:
        usercount = usercount + 1

print ("Users: {}".format(usercount))

data = {"auth_token": authtoken, "value": usercount}
data = json.dumps(data)
data = str(data)
data = data.encode('utf-8')
req =  request.Request("http://www.oci-workshop.com:3030/widgets/oci_users", data=data)
resp = request.urlopen(req)

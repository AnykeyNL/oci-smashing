import oci
from urllib import request, parse
import json
import smashing
import ocifunctions
import time

FR = "eu-frankfurt-1"
UK = "uk-london-1"

refreshdelay=60

configfile = "~/.oci/config"
config = oci.config.from_file(configfile)

identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
RootCompartmentID = user.compartment_id
print("RootID: {} ".format(RootCompartmentID))
print("Logged in as: {} @ {}".format(user.description, config["region"]))

while True:
    try:
        users = ocifunctions.Totalusers(RootCompartmentID)
        smashing.UpdateMeter("oci_users", users)

        compartments = ocifunctions.TotalCompartments(RootCompartmentID)
        smashing.UpdateMeter("oci_compartments", len(compartments))

        VCNs= ocifunctions.TotalVCNs(RootCompartmentID, compartments, FR)
        smashing.UpdateMeter("oci_vcns_fr", VCNs)

        VCNs = ocifunctions.TotalVCNs(RootCompartmentID, compartments, UK)
        smashing.UpdateMeter("oci_vcns_uk", VCNs)

        VMs = ocifunctions.TotalVMs(RootCompartmentID, compartments, FR, "VM.Standard2.1")
        smashing.UpdateMeter("oci_instance_fr_1", VMs)

        VMs = ocifunctions.TotalVMs(RootCompartmentID, compartments, UK, "VM.Standard2.1")
        smashing.UpdateMeter("oci_instance_uk_1", VMs)

        VMs = ocifunctions.TotalVMs(RootCompartmentID, compartments, FR, "VM.Standard2.2")
        smashing.UpdateMeter("oci_instances_fr_2", VMs)

        VMs = ocifunctions.TotalVMs(RootCompartmentID, compartments, UK, "VM.Standard2.2")
        smashing.UpdateMeter("oci_instances_uk_2", VMs)

        LB = ocifunctions.TotalLB(RootCompartmentID, compartments, FR)
        smashing.UpdateMeter("oci_lb_fr", LB)

        LB = ocifunctions.TotalLB(RootCompartmentID, compartments, UK)
        smashing.UpdateMeter("oci_lb_uk", LB)

        WAF = ocifunctions.TotalWaf(RootCompartmentID, compartments, FR)
        smashing.UpdateMeter("oci_waf_fr", WAF)

        WAF = ocifunctions.TotalWaf(RootCompartmentID, compartments, UK)
        smashing.UpdateMeter("oci_waf_uk", WAF)

        IMG = ocifunctions.TotalImagess(RootCompartmentID, compartments, FR)
        smashing.UpdateMeter("oci_customimg_fr", IMG)

        IMG = ocifunctions.TotalImagess(RootCompartmentID, compartments, UK)
        smashing.UpdateMeter("oci_customimg_uk", IMG)

        print ("update cycle done")
        time.sleep(refreshdelay)
    except:
        print ("encountered an error, will retry")
        time.sleep(refreshdelay)




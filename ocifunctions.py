import oci

configfile = "~/.oci/config"
config = oci.config.from_file(configfile)

def Totalusers(RootCompartmentID):
    id_provider = "ocid1.saml2idp.oc1..aaaaaaaaypucmhaxy5s7j6wu7rff2wj7y46zlglklwaahtnsmmfkqgdfltpq"
    identity = oci.identity.IdentityClient(config)
    users = oci.pagination.list_call_get_all_results(identity.list_users, compartment_id=RootCompartmentID,identity_provider_id=id_provider).data

    return (len(users))

def TotalCompartments(RootCompartmentID):
    identity = oci.identity.IdentityClient(config)
    c = oci.pagination.list_call_get_all_results(identity.list_compartments, compartment_id=RootCompartmentID).data
    compartments = []
    for comp in c:
        if comp.lifecycle_state == "ACTIVE":
            compartments.append(comp)

    return (compartments)

def TotalVCNs(RootCompartmentID, Compartments, Region):
    config["region"] = Region
    object = oci.core.VirtualNetworkClient(config)
    total = 0
    for compartment in Compartments:
        vcns = oci.pagination.list_call_get_all_results(object.list_vcns, compartment_id=compartment.id).data
        total = total + len(vcns)
    return total

def TotalVMs(RootCompartmentID, Compartments, Region, Shape):
    config["region"] = Region
    object = oci.core.ComputeClient(config)
    total = 0
    for compartment in Compartments:
        vms = oci.pagination.list_call_get_all_results(object.list_instances, compartment_id=compartment.id).data
        for vm in vms:
            if vm.shape == Shape:
                total = total + 1
    return total

def TotalLB(RootCompartmentID, Compartments, Region):
    config["region"] = Region
    object = oci.load_balancer.LoadBalancerClient(config)
    total = 0
    for compartment in Compartments:
        lb = oci.pagination.list_call_get_all_results(object.list_load_balancers, compartment_id=compartment.id).data
        total = total + len(lb)
    return total

def TotalWaf(RootCompartmentID, Compartments, Region):
    config["region"] = Region
    object = oci.waas.WaasClient(config)
    total = 0
    for compartment in Compartments:
        waf = oci.pagination.list_call_get_all_results(object.list_waas_policies, compartment_id=compartment.id).data
        total = total + len(waf)
    return total


def TotalImagess(RootCompartmentID, Compartments, Region):
    config["region"] = Region
    object = oci.core.ComputeClient(config)
    total = 0
    for compartment in Compartments:
        imgs = oci.pagination.list_call_get_all_results(object.list_images, compartment_id=compartment.id).data
        for img in imgs:
            if img.operating_system_version == "Custom":
                total = total + 1
    return total



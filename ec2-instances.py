import boto3
import pandas as pd

region = 'region'
profile = 'account'

#opening a session
my_session = boto3.session.Session(region_name=region, profile_name=profile)
ec2 = my_session.resource("ec2")



list_of_lists = []

for instance in ec2.instances.all():
    print(instance.id)
    print(instance.tags[0]['Value'])
    #in case of None Type error use instead
    #print(instance.key_name)
    print(instance.private_ip_address)
    print(instance.instance_type)
    print(instance.platform)
    print(instance.image.id)
    print(instance.vpc_id)

    sublist = []
    sublist.append(instance.id)
    sublist.append(instance.tags[0]['Value'])
    # in case of None Type error use instead
    #sublist.append(instance.key_name)
    sublist.append(instance.private_ip_address)
    sublist.append(instance.instance_type)
    sublist.append(instance.platform)
    sublist.append(instance.image.id)
    sublist.append(instance.vpc_id)
    sublist.append(profile)
    sublist.append(region)

    list_of_lists.append(sublist)


df = pd.DataFrame(list_of_lists, columns=["Instance", "Name", "IP", "Type", "OS", "AMI", "VPC", "Profile", "Region"])
df.to_csv("AWS_Instances_List1.csv", mode="a")


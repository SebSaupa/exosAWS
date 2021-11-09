import boto3
import time

fichier = open("liste_id_ip_public.txt", "a")

numVm = int(input("Veuillez saisir le numbre de vms à créer : "))

ec2 = boto3.client("ec2", region_name="eu-central-1")

ec2.run_instances(
    ImageId="ami-0a49b025fffbbdac6",    #Ubuntu server 20.04 LTS
    MinCount=1,
    MaxCount=numVm,
    InstanceType="t2.micro",
    KeyName="kp-first"
)

print("Création des vms en cours")
time.sleep(60)
print("Vm running")

instancesRunningList = ec2.describe_instances(Filters=[
    {
    "Name": "instance-state-name",
    "Values": ["running"],
    }
    ]).get("Reservations")

for instancesRunning in instancesRunningList:
    for instance in instancesRunning["Instances"]:
        instance_id = instance["InstanceId"]
        public_ip = instance["PublicIpAddress"]
        fichier.write(f"{instance_id},{public_ip},")
        print(f"{instance_id}, {public_ip}")

fichier.close()
import boto3

with open("liste_id_ip_public.txt", "r") as fichier:
    line = fichier.readline().split(",")

n = len(line)
i = 0
idList = []
ipList = []

while i < n-1:
    idList.append(line[i])
    ipList.append(line[i+1])
    i += 2

ec2 = boto3.client("ec2", region_name="eu-central-1")

for i in range(len(idList)):
    ec2.terminate_instances(InstanceIds=[idList[i]])
    print("Vm " + idList[i] + " supprimée")

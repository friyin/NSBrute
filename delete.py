import subprocess
import json
import sys

forceDelete = True
successful_zone = []
counter=0

accessKey = sys.argv[1]
secretKey = sys.argv[2]

command = "AWS_ACCESS_KEY_ID=" + accessKey + " AWS_SECRET_ACCESS_KEY=" + secretKey + " aws route53 list-hosted-zones"
out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
stdout, stderr = out.communicate()
json_data = None


if stdout != 'false':
    json_data = json.loads(stdout)

zones_to_be_removed = []
zones_for_account = []

for zone in json_data["HostedZones"]:
    zones_for_account.append(str(zone["Id"].replace("/hostedzone/", "")))

zones_to_be_removed = zones_for_account

print("zones_to_be_removed: "+str(zones_to_be_removed))

for zone in zones_to_be_removed:
    print("Removing: "+zone)
#    if zone in ('Z0446105FOOAXJRIBEOV', 'Z035745036HYX6O3X9FEO'):
#        print("Skipping "+zone)

    command = "AWS_ACCESS_KEY_ID=" + accessKey + " AWS_SECRET_ACCESS_KEY=" + secretKey + " aws route53 delete-hosted-zone --id " + str(
        zone)
    out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdout, stderr = out.communicate()

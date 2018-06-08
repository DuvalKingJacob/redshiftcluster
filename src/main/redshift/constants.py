"""Constants"""
from troposphere import Ref
import fanatics

# In case the implementation changes - reference once
get_cidrs = fanatics.network.cidrs.get_cidrs

OFFICE_VPN_CIDRS = get_cidrs("office_vpn")
APPLICATION = "redshift"
APPLICATION_GROUP = "redshift"
AWS_REGION = Ref("AWS::Region")
INFRASERVICES_ACCOUNT_ID = "946611947052"
SUBNET_TYPE = "db"
REDSHIFT_SG = "RedshiftAccess"

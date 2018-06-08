"""Module to grab appropriate subnet for deployment"""
from troposphere import Ref, Join
from troposphere.cloudformation import AWSCustomObject
from .constants import INFRASERVICES_ACCOUNT_ID, SUBNET_TYPE
from .params import vpc_param


class CustomSubnetInfo(AWSCustomObject):
    """Custom subnet info class"""
    resource_type = "Custom::SubnetInfo"

    props = {
        'ServiceToken': ((str, bytes), True),
        'account_id': ((str, bytes), True),
        'VpcId': ((str, bytes), True),
        'Purpose': ((str, bytes), True)
    }


subnet_info = CustomSubnetInfo(
    "SubnetInfo",
    ServiceToken=Join(":", [
        "arn:aws:lambda",
        Ref("AWS::Region"),
        INFRASERVICES_ACCOUNT_ID,
        "function:cloud-info-subnets"
    ]),
    account_id=Ref("AWS::AccountId"),
    VpcId=Ref(vpc_param),
    Purpose=SUBNET_TYPE
)

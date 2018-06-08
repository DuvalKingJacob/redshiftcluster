"""Custom Security Group Object"""
from troposphere import Ref
from troposphere.cloudformation import AWSCustomObject
from .constants import REDSHIFT_SG
from .params import vpc_param
from .util import lambda_path


class CustomSGSInfo(AWSCustomObject):
    """Uses lambda to return Security Group List"""
    resource_type = "Custom::SGInfo"

    props = {
        'ServiceToken': ((str, bytes), True),
        'account_id': ((str, bytes), True),
        'GroupNames': (list, True),
        'VpcId': ((str, bytes), True),
        'SecurityGroupIds': (list, False)
    }


sg_info = CustomSGSInfo(
    "SGInfo",
    ServiceToken=lambda_path("cloud-info-security-groups"),
    account_id=Ref("AWS::AccountId"),
    VpcId=Ref(vpc_param),
    GroupNames=[
        REDSHIFT_SG
    ])

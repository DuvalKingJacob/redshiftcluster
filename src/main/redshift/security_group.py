"""Cluster Security group"""
from troposphere import GetAtt, Ref, Select
from troposphere.ec2 import SecurityGroup, SecurityGroupRule
from .params import vpc_param
from .custom_sg_info import sg_info
from .constants import OFFICE_VPN_CIDRS

securitygroup = SecurityGroup(
    "RedShiftSecurityGroup",
    GroupDescription="RedShift Security Group",
    SecurityGroupIngress=[
        # Application Access
        SecurityGroupRule(
            "RedshiftApplicationIngress",
            SourceSecurityGroupId=Select(0, GetAtt(sg_info, "GroupIds")),
            FromPort="5439",
            ToPort="5439",
            IpProtocol="tcp",
        )
    ] + [
        # Office Access
        SecurityGroupRule(
            "RedshiftOfficeVPNIngress",
            CidrIp=cidr,
            FromPort="5439",
            ToPort="5439",
            IpProtocol="tcp",
        ) for cidr in OFFICE_VPN_CIDRS
    ],
    VpcId=Ref(vpc_param)
)

"""Main File for Route53"""
from troposphere.route53 import RecordSetType
from troposphere import GetAtt

dns_record = RecordSetType(
    "dnsRecord",
    HostedZoneId="Z3IK3DMEJXSM5O",
    ResourceRecords=[GetAtt('RedshiftCluster', 'Endpoint.Address')],
    Type="CNAME",
    Name="fanhouse.prod.frganalytics.com",
    TTL="300",
)

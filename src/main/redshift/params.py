"""Parameters"""
from troposphere import Parameter

environment_group_param = Parameter(
    "EnvironmentGroup",
    Description="Environment Group [lab, dev, ecomdev, ecomqc, ecomprod]",
    Type="String",
    AllowedValues=[
        "anadev",
        "anaqc",
        "lab",
        "anaprod",
    ],
    ConstraintDescription=("must be an valid environment group [lab,"
                           " anadev, anaqc, anaprod]")
)

vpc_param = Parameter(
    "VpcId",
    Description="VpcId",
    Type="AWS::EC2::VPC::Id"
)

dbname_param = Parameter(
    "DatabaseName",
    Description="The name of the first database to be created when the "
    "redshift cluster is created",
    Type="String",
    Default="defaultdb",
    AllowedPattern="([a-z]|[0-9])+",
)

clustertype_param = Parameter(
    "ClusterType",
    Description="The type of the cluster",
    Type="String",
    Default="single-node",
    AllowedValues=[
        "single-node",
        "multi-node"
    ],
)

numberofnodes_param = Parameter(
    "NumberOfNodes",
    Description="The number of compute nodes in the redshift cluster. "
    "When cluster type is specified as: 1) single-node, the NumberOfNodes "
    "parameter should be specified as 1, 2) multi-node, the NumberOfNodes "
    "parameter should be greater than 1",
    Type="Number",
    Default="1",
)

nodetype_param = Parameter(
    "NodeType",
    Description="The node type to be provisioned for the redshift cluster",
    Type="String",
    Default="dc1.large",
)

masterusername_param = Parameter(
    "MasterUsername",
    Description="The user name associated with the master user account for "
    "the redshift cluster that is being created",
    Type="String",
    Default="defaultuser",
    AllowedPattern="([a-z])([a-z]|[0-9])*",
    NoEcho=True,
)

masteruserpassword_param = Parameter(
    "MasterUserPassword",
    Description="The password associated with the master user account for the "
    "redshift cluster that is being created.",
    Type="String",
    NoEcho=True,
)

parameters = [
    environment_group_param,
    vpc_param,
    dbname_param,
    clustertype_param,
    numberofnodes_param,
    nodetype_param,
    masterusername_param,
    masteruserpassword_param
]

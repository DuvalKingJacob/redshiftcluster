"""RedShift Components"""
from troposphere import GetAtt, If, Ref
from troposphere.redshift import AmazonRedshiftParameter, Cluster, ClusterParameterGroup, ClusterSubnetGroup
from .custom_subnet_info import subnet_info
from .params import (
    clustertype_param, dbname_param, masterusername_param, masteruserpassword_param,
    nodetype_param, numberofnodes_param
)

amazonredshiftparameter1 = AmazonRedshiftParameter(
    "AmazonRedshiftParameter1",
    ParameterName="enable_user_activity_logging",
    ParameterValue="true"
)

redshiftclusterparametergroup = ClusterParameterGroup(
    "RedshiftClusterParameterGroup",
    Description="Cluster parameter group",
    ParameterGroupFamily="redshift-1.0",
    Parameters=[amazonredshiftparameter1]
)

redshiftclustersubnetgroup = ClusterSubnetGroup(
    "RedshiftClusterSubnetGroup",
    Description="Cluster subnet group",
    SubnetIds=GetAtt(subnet_info, "SubnetIds"),
)

redshiftcluster = Cluster(
    "RedshiftCluster",
    ClusterType=Ref(clustertype_param),
    NumberOfNodes=If(
        "IsMultiNodeCluster",
        Ref(numberofnodes_param),
        Ref("AWS::NoValue")
    ),
    NodeType=Ref(nodetype_param),
    DBName=Ref(dbname_param),
    MasterUsername=Ref(masterusername_param),
    MasterUserPassword=Ref(masteruserpassword_param),
    ClusterParameterGroupName=Ref(redshiftclusterparametergroup),
    VpcSecurityGroupIds=[Ref("RedShiftSecurityGroup")],
    ClusterSubnetGroupName=Ref(redshiftclustersubnetgroup),
)

redshift_resources = [
    redshiftclustersubnetgroup,
    redshiftclusterparametergroup,
    redshiftcluster
]

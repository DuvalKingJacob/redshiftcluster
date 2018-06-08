"""Conditions"""
from troposphere import Equals, Ref

conditions = {
    "IsMultiNodeCluster": Equals(
        Ref("ClusterType"),
        "multi-node"
    ),
}

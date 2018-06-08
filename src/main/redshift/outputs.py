"""Outputs"""
from troposphere import GetAtt, Join, Output
from .redshift import redshiftcluster

outputs = [
    Output(
        "ClusterEndpoint",
        Value=Join(
            ":",
            [
                GetAtt(redshiftcluster, "Endpoint.Address"),
                GetAtt(redshiftcluster, "Endpoint.Port")
            ]
        ),
    )
]

"""Util functions"""
from troposphere import Join, Ref
from .constants import INFRASERVICES_ACCOUNT_ID


def lambda_path(function_name):
    """Returns the arn for the lambda"""
    return Join(
        ":",
        [
            "arn:aws:lambda",
            Ref("AWS::Region"),
            INFRASERVICES_ACCOUNT_ID,
            'function:{}'.format(function_name)
        ]
    )

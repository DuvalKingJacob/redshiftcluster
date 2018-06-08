"""Main file for RedShift Cluster"""
# Converted from Redshift.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Template
from .params import parameters
from .conditions import conditions
from .security_group import securitygroup
from .redshift import redshift_resources
from .outputs import outputs
from .custom_subnet_info import subnet_info
from .custom_sg_info import sg_info

def create_cft():
    """Creates the CFT"""
    template = Template()
    template.add_version("2010-09-09")

    template.add_description(
        "AWS CloudFormation Template: Redshift cluster in a VPC"
    )

    # Parameters
    for param in parameters:
        template.add_parameter(param)

    # Conditions
    for condition in conditions:
        template.add_condition(condition, conditions[condition])

    # Custom lookups
    template.add_resource(subnet_info)
    template.add_resource(sg_info)

    # Security Group
    template.add_resource(securitygroup)

    # Redshift components
    for item in redshift_resources:
        template.add_resource(item)

    # Outputs
    for output in outputs:
        template.add_output(output)

    return template

if __name__ == "__main__":
    print(create_cft().to_json())

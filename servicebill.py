import boto3
ce = boto3.client('ce', region_name='us-east-1')

response = ce.get_cost_and_usage(
    TimePeriod={'Start': '2024-12-01', 'End': '2025-01-01'},
    Granularity='MONTHLY',
    Metrics=['UnblendedCost'],
    GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
)

for service in response["ResultsByTime"][0]["Groups"]:
    print(service["Keys"][0], ":", service["Metrics"]["UnblendedCost"]["Amount"])

import boto3
from datetime import datetime, timedelta

# Cost Explorer works only in us-east-1
ce = boto3.client('ce', region_name='us-east-1')

def get_last_3_month_cost():
    # Calculate dates for last 3 months
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=90)   # approx 3 months

    # Convert to required format YYYY-MM-DD
    start = start_date.strftime("%Y-%m-%d")
    end = end_date.strftime("%Y-%m-%d")

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End': end
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )

    print("\n📊 Last 3 Months AWS Billing:\n")
    for month in response["ResultsByTime"]:
        amount = month["Total"]["UnblendedCost"]["Amount"]
        currency = month["Total"]["UnblendedCost"]["Unit"]
        print(f"➡️ {month['TimePeriod']['Start']} : {amount} {currency}")

get_last_3_month_cost()

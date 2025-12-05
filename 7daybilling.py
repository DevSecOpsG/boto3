import boto3
from datetime import datetime, timedelta

# Cost Explorer client (must use us-east-1)
ce = boto3.client('ce', region_name='us-east-1')

def get_cost(start, end):
    """Fetch AWS cost between start and end date."""
    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    
    amount = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    currency = response['ResultsByTime'][0]['Total']['UnblendedCost']['Unit']
    return amount, currency

def main():
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)
    last_7_days = today - timedelta(days=7)

    print("\n📊 DAILY AWS BILLING REPORT\n")

    # 📌 Today's Cost
    today_amount, currency = get_cost(str(today), str(today + timedelta(days=1)))
    print(f"🔹 Today ({today})     : {today_amount} {currency}")

    # 📌 Yesterday's Cost
    yest_amount, _ = get_cost(str(yesterday), str(today))
    print(f"🔹 Yesterday ({yesterday}): {yest_amount} {currency}")

    # 📌 Last 7 Days (Total)
    response = ce.get_cost_and_usage(
        TimePeriod={'Start': str(last_7_days), 'End': str(today)},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    total_7_days = 0
    for day in response["ResultsByTime"]:
        total_7_days += float(day["Total"]["UnblendedCost"]["Amount"])

    print(f"🔹 Last 7 Days Total   : {round(total_7_days, 4)} {currency}")

    print("\n✅ Billing report generated successfully.\n")

if __name__ == "__main__":
    main()

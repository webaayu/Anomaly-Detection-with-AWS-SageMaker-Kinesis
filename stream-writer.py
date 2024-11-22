import csv
import boto3
import time


def read_csv_batches(file_path, batch_size=10):
    # Read CSV file in batches of 10 rows
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        batch = []
        for row in reader:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

def send_to_kinesis(kinesis_client, stream_name, records):
    # Add PartitionKey to each record
    kinesis_records = [
        {
            'Data': ','.join(record),
            'PartitionKey': record[0] if record else 'default-key'  # Use the first field or a default key
        }
        for record in records
    ]
    response = kinesis_client.put_records(StreamName=stream_name, Records=kinesis_records)
    return response

def main():
    # Set your AWS credentials and region
    aws_access_key_id = 'AKxxxxxxUAL3FF62YF'
    aws_secret_access_key = 'VLnGs9PvOxxxxxxGhP1'
    aws_region = 'ap-south-1'

    # Set your Kinesis stream name
    stream_name = 'modelTestStream'

    # Create a Kinesis client
    kinesis_client = boto3.client('kinesis', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    # Set the path to test data CSV file
    csv_file_path = 'path/file.csv'

    # Read batches of 10 lines and send to Kinesis every second
    for batch in read_csv_batches(csv_file_path):
        send_to_kinesis(kinesis_client, stream_name, batch)
        time.sleep(1)

if __name__ == "__main__":
    main()

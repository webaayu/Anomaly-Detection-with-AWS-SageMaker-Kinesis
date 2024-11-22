import boto3
import json
import base64

def lambda_handler(event, context):
    # Initialize SageMaker runtime client
    sagemaker_runtime = boto3.client("sagemaker-runtime", region_name="ap-south-1")
    
    # Initialize the list to hold the processed data (for logging purposes)
    processed_data = []

    # Process each record in the Kinesis event
    for record in event['Records']:
        # Extract base64-encoded data from the Kinesis record
        payload = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        
        # Log the decoded data for debugging
        print(f"Decoded Kinesis data: {payload}")
        
        # Assuming the Kinesis data is a comma-separated string like '1,2,3,4'
        # Convert the decoded data into a list of floats (or integers if necessary)
        data_values = [float(x) for x in payload.split(',')]  # Convert each value to a float
        
        # Structure the payload in the format expected by SageMaker
        formatted_payload = {"data": [data_values]}  # Wrap the data in the required format
        
        # Log the formatted payload that will be sent to SageMaker
        print(f"Formatted payload for SageMaker: {json.dumps(formatted_payload)}")
        
        # Invoke the SageMaker endpoint with the formatted payload
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName="endpoint2",  # Replace with your actual SageMaker endpoint name
            ContentType="application/json",
            Body=json.dumps(formatted_payload),
        )

        # Log the full response from SageMaker for debugging
        print(f"Received response from SageMaker: {response}")

        # Parse the response from SageMaker
        result = response["Body"].read().decode("utf-8")

        # Log the parsed result
        print(f"Decoded response from SageMaker: {result}")
        
        # Append the processed result to the processed_data list
        processed_data.append(result)

    # Return the final response (this is optional and depends on your Lambda use case)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Processed data successfully",
            "processed_data": processed_data  # List of results from SageMaker
        })
    }

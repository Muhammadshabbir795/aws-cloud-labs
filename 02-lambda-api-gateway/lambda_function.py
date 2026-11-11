import json

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

    if method == "POST":
        body = json.loads(event.get("body") or "{}")
        name = body.get("name", "Unknown")
        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": f"Student {name} received"})
        }

    params = event.get("queryStringParameters") or {}
    name = params.get("name", "World")
    print(f"Request received for name: {name}")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": f"Hello, {name}!"})
    }

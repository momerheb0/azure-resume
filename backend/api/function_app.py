import logging
import azure.functions as func
import os
import json
from azure.cosmos import CosmosClient, PartitionKey

# FunctionApp HTTP trigger
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GetResumeCounter")
def get_resume_counter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        # Environment variable for the connection string
        cosmos_db_connection_string = os.getenv('AzureResumeConnectionString')
        client = CosmosClient.from_connection_string(cosmos_db_connection_string)

        # Define database and container
        database_name = "AzureResume"
        container_name = "Counter"
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        # Retrieve the item from the Cosmos DB (assuming ID is 1 and partition key is "1")
        counter_item = container.read_item(item="1", partition_key="1")
        count = counter_item["count"]
        
        # Increment the count
        counter_item["count"] = count + 1
        
        # Replace updated count in the DataBase
        container.replace_item(item="1", body=counter_item)
        
        # Return the updated count as a JSON response
        return func.HttpResponse(
            json.dumps({"count": counter_item["count"]}),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"Error processing the request: {str(e)}")
        return func.HttpResponse(
            "An error occurred while processing the request.",
            status_code=500
        )

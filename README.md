# Azure-Resume
This is my [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/) built on Azure. It's a static portfolio website hosted on Azure storage, with a visitor counter built on Azure Functions. The website is built with HTML, CSS, and JavaScript. The visitor counter is built with Python and Azure Functions.

## Structure

- `frontend/`: Folder contains the website.
    - `main.js`: Folder contains visitor counter code.
- `api/`: Folder contains the Python API deployed on Azure Functions.
    - `function_app.py`: Contains the visitor counter code written in Python.


## Frontend

The front-end is a static site and has a visitor-counter. The visitor counter data fetched via an API call to an Azure Function.

- I used this [Template](https://styleshout.com/free-templates/ceevee/) to create my site.
- I am no JavaScript expert, but this [article](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-fetch-api-to-get-data) explains how to make an API call with JavaScript code.
- Deployed the static site folder to [Azure blob storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website-host).



## Backend 

The back-end is an [HTTP triggered Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-python) with Cosmos DB input and output binding. When the function is invoked it retrieves the CosmosDB item where the resume visitor count is stored, it incremenrts it by 1, saves it back in the DB then returns it's value to the caller. 

- Created a [Cosmos DB for NoSQL account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal) along with the Database, Container and the items inside.
- Here's a helpful MS document on how to [develop azure function using VS code --
    with python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=node-v4%2Cpython-v2%2Cisolated-process%2Cquick-create&pivots=programming-language-python#run-functions-locally)
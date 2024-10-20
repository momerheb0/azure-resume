# Azure-Resume
This is my [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/) built on Azure. It's a static portfolio website hosted on Azure storage, with a visitor counter built on Azure Functions. The website is built with HTML, CSS, and JavaScript. The visitor counter is built with Python and Azure Functions.

## Structure

- `frontend/`: Folder contains the website.
    - `main.js`: Folder contains visitor counter code.
- `api/`: Folder contains the Python API deployed on Azure Functions.
    - `function_app.py`: Contains the visitor counter code written in Python.
- `github/workflows/`: Folder contains CI/CD workflow configurations.


## Frontend

The front-end is a static site and has a visitor-counter. The visitor counter data fetched via an API call to an Azure Function.

- I used this [Template](https://styleshout.com/free-templates/ceevee/) to create my site.
- I am no JavaScript expert, but this [article](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-fetch-api-to-get-data) explains how to make an API call with JavaScript code.
- Deployed the static site folder to [Azure blob storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website-host).
- It's essential to enable CORS with Azure Functions locally and once it's [deployed to Azure](https://docs.microsoft.com/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal#cors) for the website to be able to call it.
- Created an Azure CDN for Blob Storage to cache the website content, provision a TLS certificate to enable HTTPS support and map a Custom Domain to the site. 


## Backend 

The back-end is an [HTTP triggered Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-python) with Cosmos DB input and output binding. When the function is invoked it retrieves the CosmosDB item where the resume visitor count is stored, it incremenrts it by 1, saves it back in the DB then returns it's value to the caller. 

- Created a [Cosmos DB for NoSQL account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal) along with the Database, Container and the items inside.
- Here's a helpful MS document on how to [develop azure function using VS code --
    with python](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=node-v4%2Cpython-v2%2Cisolated-process%2Cquick-create&pivots=programming-language-python#run-functions-locally).
- Deployed local Azure Function to Azure portal for production via Visual Studio Code Extension: Azure Functions.    
    - It's important to install the required Azure packages (ex: azure-cosmos, azure-core) in your virtual environment and export it to your `requirements.txt` file because Azure Functions will install the dependencies listed inside during the deployment process.
``` bash
$ pip install azure-cosmos
$ pip freeze > requirements.txt
```


## CI/CD Pipline

The porject utilizes GitHub Actions for continuous integration and deployment. The application is automatically built after each commit
There are two seperate worflows:
- `frontend.main.yml`: This workflow is responsible for building and deploying the frontend of the application to Azure.
- `backend.main.yml`: This workflow handles the backend, including deploying the Azure Function. The backend also includes testing steps before deployment to Azure.


## Testing

 Pytest was used for unit testing the backend's Azure Function, it is run on every push request ensuring that the code remains bug-free before deployment.

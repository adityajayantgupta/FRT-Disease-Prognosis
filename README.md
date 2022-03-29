# Future Ready Talent - Disease Prognosis
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

Microsoft Future Ready Talent Internship Project

Project URL - https://adityagupta4213.z13.web.core.windows.net/

![image](https://user-images.githubusercontent.com/19838832/160603066-4da09cf1-66bd-4d27-8745-0e3f5e5e4582.png)


## Problem Statement/Opportunity
People encounter a variety of medical symptoms on a regular basis but rarely bother further investigation or checkup. What if there was a way to predict their medical prognosis using the combination of their symptoms? A service which can give a better idea of what disease the user may be suffering from.

## Project Details 

Using the power of machine learning and computational analytics, this web application predicts the most likely disease given a set of symptoms. As opposed to looking up individual symptoms, users can input multiple symptoms simultaneously and get a predictive prognosis based on their combined analysis. 

The website is driven by a custom API that uses a combination of three different machine learning models trained on symptomatic diagnosis data to predict the most likely disease from given symptoms. The API is hosted on Azure App Service and runs as a Docker container in Azure Container Registry.

The frontend uses the power of said API and combines it with a user friendly experience. It is hosted using Azure Blob Storage.

## Working 

The project's core relies on the combination of trained machine learning models and a custom API that uses those model to predict the given input. 

- The machine learning models, as seen in [model.py](https://github.com/adityagupta4213/FRT-Disease-Prognosis/blob/main/model.py), use a symptomatic diagnosis dataset to train themselves on what different combinations of symptoms can lead to what kinds of diseases.

- The three models used for this process are *Support Vector Machine*, *Naive Bayes* and *Random Forest*. All three models are trained separately on the same dataset and the resulting models are saved as `pickle` files. This allows us to use these models for future prediction without having to train them all over again. 

- To process requests as a web service and return the predicted results, a Flask API is set up in [app.py](https://github.com/adityagupta4213/FRT-Disease-Prognosis/blob/main/app.py). The API uses the stored models and provides them the given input to predict the disease. Their results are then taken together and the `mode` of their predictions is returned as the final result. 

## Azure Technologies

The project uses the Azure App Service to host the custom API. This allows the API to have maximum availability and smooth access. 

The API is stored as a Docker container running in Azure Container Registry. It allows the API to run in a consistent and isolated environment, along with fast deployment and reliability. 

Finally the website itself is stored using Azure Blob Storage which allows it to be scalable, durable and have consistent availability.

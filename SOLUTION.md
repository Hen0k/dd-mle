# Solutions Description

## Task 1 Solution (mle_package implementation)

I started with adding the abstract class that a data science team member would have to inherit and implement the functionalities it must add and use some other methods that are already implemented. The ones that should be implemented by the data scientist are:

* model
* load
* save
* fit
* predict

The rest are already implemented by me and can help log prediction, and check if retraining is necessary.
These can also be re-implemented by the data science team. But the goal here is to ease the data science team's work.

### logging predictions

I am using pythons own logging functionality with a JSON formatter to log out every prediction made by the model.
This keeps track of few key things:

* input feature values
* input feature index
* models prediction
* timestamp

These are written out as dict object, one per line. There is also a handler that checks if the log file has exceeded a set memory size and will start a new file.

### trigger retraining

This method uses the log data created by the above functionality. It first reads all the log files and converts the data into a pandas format. Assuming all inferences are being done with data we already have, It compares the models predictions with the labels in our database corresponding to the inputs index. (side note: It took a log time to see that I already the labels. I was first going to implement a solution that check for data drift by comparing the statistical property of the features in production to the training data.) Whenever the accuracy dips below 70% it prints out a message recommending a retraining of the model.

## Task 2 Solution (extra tasks for ds and de modules)

* For the data engineering module, I chose to work on the second task. This asked to create a new users named Analyst that has read and write access to the tables. I added the SQL commands in the script file in `db_admin` directory. Now, when a fresh version of the container is started, the account is created with the other user accounts.
* For the data science module, I added the sales table data getter to the `fetch_data` module. This uses the available connection string and makes a query to fetch the sales data. It returns it as a pd.DataFrame.

### Task 3 Solution (deployment)

This is where I spent the majority of the time. In order to allow me to use the logging and monitoring features from the mle_package, I added the mle and ds packages to the deployment module. I needed the ds module for loading the model and making predictions.

I am using a Flask based API for handling requests. It then uses the model class built by the ds module to load the pre-trained model. It then takes in requests with POST method and passes the incoming data through the model. It uses the predict_with_logging method. It then responds with the models prediction. 

I decided to create a new docker-compose-prod.yml file since I didn't need some of the components in the de module. It also has a CI/CD configuration that publishes docker images to my hub account using GitHub Actions Workflow. 

### Future Work

* Add a WatchTower docker container on the deployment server to watch for changes on the docker images and update accordingly.

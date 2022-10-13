# DE Module

## Description

As the Machine Learning Engineer for this product, you need to provide the DS with a framework that they can use to develop their models, following good practices.

## Implementation Requirements

### Machine Learning Engineering Package

You should create a pip-installable package, called `machine_learning_engineering`, in an `./mle_package` folder.

In particular, you should be providing the Data Scientist with some guidance on how to implement their models in a way that is "production-ready".
As such, you should provide them with an `MLEModel` **abstract** class that they can extend to represent their models.

This class should provide several non-implemented methods (which raise an exception) representing the most important methods that the data scientist will have to implement in order for their model to be usable.

You should also provide a few implemented methods, which include error handling:

* `predict_with_logging` - this method uses the DS-implemented predict function, calls it over some new data, and logs the results to some storage (see _Storage_ section)
* `trigger_retraining` - this method should assess, based on the log-storage results, if the model's performance has decreased significantly, and if so, retrain it over a certain dataset.

#### Important Note

The Data Scientist is expecting to be able to install/use your package in a specific way, as specified in their Dockerfile (`ds/docker/Dockerfile`) and on their own data science package (`ds/ds_package`).
On a real project, the MLE work would come first, and guide the DS work - but for the purpose of this technical assessment, since we need to have an end-to-end system, some sort of reverse-engineering would always be required.
If you feel comfortable with it, you are more than welcome to implement a few changes to the DS package to better fit your needs.

### Testing

You should also provide a generic test for this model class (and any valid subclasses), that the data scientist can apply over their own implementation.
You should also provide a very basic instance of a valid class that passes this generic test. This test should go in the `tests` folder inside your package, and be runnable with `pytest`.

### Storage

You should implement some way to store the model's "live" predictions. The only requirement here is that it is compatible with your implementations of the `deployment` module, and the `predict_with_logging`/`trigger_retraining` functionalities (however you've chosen to implement them).

## Evaluation Criteria

The evaluation criteria for this module are intentionally loose. We are mostly interested in assessing if you have a notion of good `ML Ops` practices.

You can follow the requirements above, but we also accept alternative implementations with the same end goal - as long as these are properly documented and the end-to-end system specified in the Docker-compose file still runs!
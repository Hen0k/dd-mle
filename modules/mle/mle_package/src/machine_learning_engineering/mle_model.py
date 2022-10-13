from abc import (
    ABC,
    abstractmethod,
    abstractproperty,
)
import os
from typing import Any
import pandas as pd
from machine_learning_engineering.log_handler import get_rotating_log
from machine_learning_engineering.fetch_data import get_labels
import json
from datetime import datetime


logger_name = __name__
logger = get_rotating_log(filename="1.log", logger_name=logger_name)


class MLEModel(ABC):

    @abstractproperty
    def model(self):
        pass

    @abstractmethod
    def load(self, model_folder) -> Any:
        pass

    @abstractmethod
    def save(self, model_folder) -> None:
        pass

    @abstractmethod
    def fit(self, dataset: Any) -> dict:
        pass

    @abstractmethod
    def predict(self, features: pd.DataFrame) -> int:
        pass

    def predict_with_logging(self, idx: int, features: pd.DataFrame) -> int:
        """Logs every prediction on to a text file

        Parameters
        ----------
        features : pd.DataFrame
            Input features that are given to the model

        Returns
        -------
        int
            A 0 or 1 prediction
        """
        label = self.predict(features)
        features = features.to_dict(orient="records")
        timestamp = datetime.now().__str__()
        log_message = {
            **features[0], **{"predicted": label, "idx": idx, "timestamp": timestamp}}
        logger.info(log_message)
        # self.trigger_retraining()
        return label

    def logs_to_json(self, log_dir: str) -> list:
        """read the log files and convert them to a json object

        Parameters
        ----------
        log_dir : str
            path to the logs folder

        Returns
        -------
        list
            A list of dictionaries
        """
        file_names = os.listdir(log_dir)
        file_paths = [os.path.join(log_dir, f_name) for f_name in file_names]
        predictions = []
        for path in file_paths:
            with open(path, "r") as f:
                data = [json.loads(l) for l in f.readlines()]
                predictions += data

        return predictions

    def trigger_retraining(self, log_dir: str = "logs") -> int:
        """Execute analysis steps to check if there is a concept drift 
        and alert the data scientist to retrain the model. The following
        are the steps it takes.
        1. Get a list of the log files
        2. For each file parse the features and prediction and 
        append to a json
        3. Convert to pd.DataFrame
        4. Calculate features std of production data
        5. Calculate features std of training data
        6. Compare the result and if it is over a threshold

        Parameters
        ----------
        log_dir : str
            path to the logs folder

        Returns
        -------
        int
            A 0 or 1 prediction
        """
        predictions = self.logs_to_json(log_dir)
        predictions = pd.DataFrame(predictions)
        indices = predictions['idx'].tolist()
        true_labels = get_labels(indices)
        merged = predictions.merge(true_labels, on="idx")
        merged["predicted"] = merged["predicted"].astype(merged["label"].dtype)
        numerator = merged[merged["predicted"] == merged["label"]].shape[0]
        acc = numerator / merged.shape[0]
        print(f"Accuracy: {acc}")
        if acc < 0.60:
            print("Should probably retrain")
            return
        print("All good")

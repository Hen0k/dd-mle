import pytest
from machine_learning_engineering.mle_model import MLEModel
from typing import Any
import pandas as pd


        


def test_MLEModel_exception():
    """Test MLEModel Exception"""
    
    with pytest.raises(TypeError):
        model = MLEModel()


def test_valid_instance():
    """Test a valid class that implements the abstract MLEModel class"""
    class SimpleModel(MLEModel):
        ohe = None         # one-hot encoder for categorical features
        model = None       # the model itself

        def load(self, model_folder) -> Any:
            """Loads the model to memory. To be implemented by the data scientist.
            """
            

        def save(self, model_folder) -> None:
            """Saves the model to a given location. To be implemented by the data scientist.
            """
            

        def _one_hot_encode(self, dataset: pd.DataFrame):
            """One-hot encodes the categorical features in the dataset.
            """
            

        def fit(self, dataset: Any) -> dict:
            """
            Fits the model to the data. To be implemented by the data scientist.

            Note: For the purpose of this test, and since we are lazy, we are using a very simple
            AutoML approach, without any metrics reporting or care whatsoever :-) 

            NEVER do this on an actual project!!
            """
            

        def predict(self, features: pd.DataFrame) -> int:
            """Predicts the label of unseen data. To be implemented by the data scientist.
            """
    simple_model = SimpleModel()
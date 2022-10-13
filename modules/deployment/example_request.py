import requests

response = requests.post(
    "http://172.26.0.4:5000/predict",
    json={
        "idx": 15000,
        "features": {
            "attr_a": 1,
            "attr_b": "c",
            "scd_a": 0.55,
            "scd_b": 3
        }
    }
)

print(response.json()["label"])

# response = requests.post(
#     "http://172.26.0.4:5000/predict",
#     json={
#         "idx": 7,
#         "features": {
#             "attr_a": 3,
#             "attr_b": "c",
#             "scd_a": 0.3504786947163524,
#             "scd_b": 3
#         }
#     }
# )

# print(response.json()["label"])
from typing import List

import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


def createDataframe1(student_data: List[List[int]]) -> pd.DataFrame:
    student_id = []
    age = []

    for i in range(len(student_data)):
        student_id.append(student_data[i][0])
        age.append(student_data[i][1])

    df = pd.DataFrame({
        "student_id": student_id,
        "age": age
    })

    return df

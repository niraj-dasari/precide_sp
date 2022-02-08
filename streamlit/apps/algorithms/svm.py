

import pandas as pd
import numpy as np
import streamlit as st


pipl_lr = joblib.load(open(r'D:\projects\BEIT\precide\notebooks\Suicide prediction Prediction\svm_model.pkl', 'rb'))


review = """I received defective piece display is not working properly"""
review_vector = pipl_lr.vectorizer.transform([review]) # vectorizing
print(pipl_lr.classifier_linear.predict(review_vector))
import joblib

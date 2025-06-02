import joblib
import pickle

# Load joblib files
with open('model/rf_model.joblib', 'rb') as f:
    model = joblib.load(f)

with open('model/preprocessing.joblib', 'rb') as f:
    preprocessing = joblib.load(f)

with open('model/label_encoder.joblib', 'rb') as f:
    label_encoder = joblib.load(f)

# Save as pickle files
with open('model/rf_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/preprocessing.pkl', 'wb') as f:
    pickle.dump(preprocessing, f)

with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print("Conversion completed successfully!") 
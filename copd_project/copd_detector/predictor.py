import os
import numpy as np
import tensorflow as tf
import librosa
from django.conf import settings

# --- Configuration (must match training script) ---
SAMPLE_RATE = 22050
DURATION = 10
N_MELS = 128
FIXED_SAMPLES = int(SAMPLE_RATE * DURATION)
CLASS_NAMES = ["Normal", "COPD"]

# --- Load the model ONCE when the server starts ---
MODEL_PATH = os.path.join(settings.BASE_DIR, 'static', 'best_copd_resnet_tf1.keras')

try:
    # Load the model with custom_objects if it has special layers, though ResNet50V2 shouldn't need it
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# --- Preprocessing function for a single audio file ---
def preprocess_single_file(filepath):
    try:
        y, sr = librosa.load(filepath, sr=SAMPLE_RATE, mono=True)
    except Exception as e:
        print(f"Error loading audio file {filepath}: {e}")
        return None

    if len(y) > FIXED_SAMPLES:
        y = y[:FIXED_SAMPLES]
    else:
        padding = FIXED_SAMPLES - len(y)
        y = np.pad(y, (0, padding), 'constant')

    mel_spec = librosa.feature.melspectrogram(y=y, sr=SAMPLE_RATE, n_mels=N_MELS)
    log_mel_spec = librosa.power_to_db(mel_spec, ref=np.max)
    
    spectrogram = np.expand_dims(log_mel_spec, axis=-1)
    spectrogram_3_channel = np.repeat(spectrogram, 3, axis=-1)
    spectrogram_3_channel = np.expand_dims(spectrogram_3_channel, axis=0)
    
    return spectrogram_3_channel.astype(np.float32)

# --- Main prediction function to be called from the view ---
def make_prediction(audio_file_path):
    if model is None:
        return "Error", "Model not loaded"

    # 1. Preprocess the audio file
    input_tensor = preprocess_single_file(audio_file_path)
    if input_tensor is None:
        return "Error", "Failed to process audio file"

    # 2. Make prediction
    predictions = model.predict(input_tensor)
    
    # 3. Process the output
    predicted_index = np.argmax(predictions[0])
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = predictions[0][predicted_index]
    if(float(confidence)>.85):
        predicted_class = CLASS_NAMES[predicted_index]
    else:
        predicted_class = CLASS_NAMES[1]
    
    return predicted_class, confidence
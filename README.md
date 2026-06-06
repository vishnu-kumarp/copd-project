# 🫁 COPD Prediction System

> A machine learning-powered web application for early detection and risk assessment of Chronic Obstructive Pulmonary Disease (COPD), built with Django.

---

## 1. Project Overview

Chronic Obstructive Pulmonary Disease (COPD) is a progressive and life-threatening lung condition that affects millions of people worldwide. Early detection is critical for effective management and improved patient outcomes.

The **COPD Prediction System** is a Django-based web application that leverages machine learning algorithms to predict the likelihood of COPD in individuals based on clinical and demographic inputs. Users can enter patient data through a clean web interface and receive an instant risk prediction along with relevant health insights.

This project was developed as a final-year machine learning project to demonstrate the practical integration of predictive modeling with a full-stack web framework.

---

## 2. Key Features

### ⭐ Feature 1 — ML-Powered COPD Risk Prediction *(Most Important)*
At the core of this system is a trained machine learning model that analyzes patient data — including age, smoking history, lung function parameters, and symptoms — to predict COPD risk with meaningful accuracy. The model is integrated directly into the Django backend and returns real-time predictions on form submission.

### ⭐ Feature 2 — Interactive Patient Data Input Form *(Most Important)*
The application provides a user-friendly web form where healthcare professionals or patients can enter clinical parameters. The form is validated server-side and client-side, ensuring clean data is passed to the prediction engine every time.

---

### Additional Features

- **Prediction Result Dashboard** — Displays the prediction outcome (positive/negative risk) along with a confidence score or risk level indicator.
- **Responsive Web Interface** — Built with Django templates, accessible on both desktop and mobile browsers.
- **Admin Panel** — Django's built-in admin interface allows authorized users to manage prediction records and patient data.
- **Modular Codebase** — Clean separation of the ML model, Django views, and templates makes the project easy to extend or maintain.
- **Input Validation** — Robust server-side validation prevents erroneous or incomplete data from reaching the model.

---

## 3. Technology Stack

| Layer | Technology |
|---|---|
| **Backend Framework** | Django (Python) |
| **Machine Learning** | scikit-learn / (your model library) |
| **Language** | Python 3.x |
| **Frontend** | HTML5, CSS3, Django Templates |
| **Database** | SQLite (default Django DB) |
| **Model Serialization** | Pickle / Joblib |
| **Data Processing** | NumPy, Pandas |
| **Version Control** | Git |

> **Note:** Replace the ML library entry above with the exact library used (e.g., scikit-learn, XGBoost, TensorFlow) if different.

---

## 4. How It Works

```
User Inputs Patient Data
         │
         ▼
  Django View Receives Form Data
         │
         ▼
  Input Preprocessing (scaling, encoding)
         │
         ▼
  Pre-trained ML Model Makes Prediction
         │
         ▼
  Result Rendered on Web Page
  (COPD Risk: High / Low + Confidence Score)
```

1. The user navigates to the prediction form and enters patient details such as age, gender, smoking history, FEV1 (lung function), cough frequency, and other clinical indicators.
2. On submission, the Django view receives the data, preprocesses it (scaling, encoding categorical fields), and feeds it to the pre-trained ML model loaded from a serialized file (`.pkl` or `.joblib`).
3. The model outputs a prediction (COPD positive or negative) along with a risk score.
4. The result is displayed on a results page with a clear visual indicator of the risk level.

---

## 5. Installation Steps

### Prerequisites

- Python 3.8 or above
- pip (Python package manager)
- Virtual environment tool (recommended)

### Step-by-Step Setup

**1. Clone the repository**
```bash
git clone https://github.com/your-username/copd-prediction-system.git
cd copd-prediction-system
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply database migrations**
```bash
python manage.py migrate
```

**5. Create a superuser (optional, for admin access)**
```bash
python manage.py createsuperuser
```

**6. Run the development server**
```bash
python manage.py runserver
```

**7. Open the application**

Navigate to `http://127.0.0.1:8000/` in your browser.

---

## 6. Usage

1. Open the application in your browser.
2. Navigate to the **Prediction** page from the home screen.
3. Fill in the patient details in the form (age, smoking history, symptoms, lung function values, etc.).
4. Click **Predict** to submit the form.
5. View the prediction result — the system will display whether the patient is at **High Risk** or **Low Risk** for COPD.
6. Optionally, use the Django admin panel at `/admin` to view stored prediction records (login required).

---

## 7. Future Enhancements

- **Model Improvement** — Train on larger and more diverse clinical datasets to improve accuracy and reduce bias.
- **Doctor/Patient Login System** — Role-based authentication to separate patient and healthcare provider views.
- **Report Generation** — Allow users to export prediction results as a PDF health report.
- **REST API** — Expose the prediction engine as a REST API endpoint so it can integrate with hospital management systems or mobile apps.
- **Data Visualization** — Add charts and graphs to show input trends and model confidence visually.
- **Multi-language Support** — Localize the interface for non-English-speaking regions to improve accessibility.
- **Cloud Deployment** — Deploy the application on a cloud platform (e.g., AWS, Heroku, or Render) for public access.

---

## 8. Disclaimer

> ⚠️ **This project is developed strictly for educational and academic purposes only.**
>
> The COPD Prediction System is **not a certified medical device** and is **not intended to replace professional medical advice, diagnosis, or treatment.** The predictions generated by this system should **not** be used as the sole basis for any clinical decision. Always consult a qualified healthcare professional for medical guidance.
>
> The developers of this project take no responsibility for any outcomes resulting from the use or misuse of this application in any real-world medical context.

---

## 9. Conclusion

The COPD Prediction System demonstrates a practical application of machine learning in the healthcare domain. By combining a trained predictive model with a responsive Django web interface, the project makes early COPD risk screening more accessible and straightforward. The modular architecture ensures the system can be extended with better models, richer data, and additional features as the project grows.

This project highlights the potential of AI-assisted tools to support — not replace — medical professionals in identifying at-risk patients earlier and enabling timely intervention.

---

*Built with ❤️ using Django and Machine Learning*

# 🏥 Health Insurance Premium Prediction API

This project is a **Flask-based REST API** that predicts health insurance premiums using a **Machine Learning model** trained on a health insurance dataset.  

It provides endpoints to **train**, **test**, and **predict** insurance premiums based on user details like age, sex, BMI, children, and smoker status.  

---

## 📂 Project Structure
```
insurance_premium_api/
│── app.py                # Flask application with ML model APIs
│── model.pkl             # Saved trained model (generated after training)
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── Health_Insurance.csv  # Dataset (you upload this for training)
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/insurance_premium_api.git
   cd insurance_premium_api
   ```

2. Create a virtual environment & activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Run the Application
Start the Flask server:
```bash
python app.py
```

By default, the API will be available at:
```
http://127.0.0.1:5000/
```

---

## 🔑 API Endpoints

### 1️⃣ **Train the Model**
- **Endpoint:** `/train`
- **Method:** `POST`
- **Input:** Upload CSV file (health insurance dataset)
- **Output:** Model trained & saved with R², MSE, and MAE scores  

**Postman Example (Form-Data):**
```
Key: file
Value: Health_Insurance.csv
```

**Response:**
```json
{
  "message": "Model trained and saved successfully",
  "r2_score": 0.75,
  "mse": 340123.45,
  "mae": 893.21
}
```

---

### 2️⃣ **Test the Model**
- **Endpoint:** `/test`
- **Method:** `POST`
- **Input:** Upload test dataset (CSV)
- **Output:** Model evaluation metrics  

**Postman Example (Form-Data):**
```
Key: file
Value: test_data.csv
```

**Response:**
```json
{
  "message": "Model tested successfully",
  "r2_score": 0.72,
  "mse": 352100.55,
  "mae": 910.78
}
```

---

### 3️⃣ **Predict Premium**
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Input:** JSON object with details
- **Output:** Predicted premium  

**Request JSON:**
```json
{
  "age": 30,
  "sex": "male",
  "bmi": 25.5,
  "children": 2,
  "smoker": "no"
}
```

**Response:**
```json
{
  "predicted_premium": 4125.37
}
```

---

## 📊 Dataset Format

The CSV file should include these columns:
- `age` → Age of the person  
- `sex` → Male/Female  
- `bmi` → Body Mass Index  
- `children` → Number of children/dependents  
- `smoker` → Yes/No  
- `charges` → Insurance charges (Target Variable)

---

## 📦 Requirements
List of dependencies (in `requirements.txt`):
```
Flask
pandas
scikit-learn
pickle-mixin
```

---

## 🛠️ Tools Used
- **Python 3.12**
- **Flask** (Backend API Framework)
- **scikit-learn** (ML Model)
- **Pandas** (Data Handling)
- **Postman** (API Testing)

---

## 🎥 Demo
- API tested using **Postman**  
- You can record a short demo showing `/train`, `/test`, `/predict` usage.  

---

## ✍️ Author
Developed by **Shubham Sanap** during internship at **CodeSpyder Technologies Pvt. Ltd.**

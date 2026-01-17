# 💊 Drug Interaction Checker 

A simple **Streamlit-based web application** that allows users to select medications and check for **known drug–drug interactions** using a predefined interaction database.

⚠️ **Disclaimer:** This project is for **educational purposes only** and does **not** replace professional medical advice.

---

## 📌 Features

- 🧠 Clean, layered architecture (Data, Logic, UI)
- 🔍 Detects known interactions between commonly used medications
- 🖱️ Easy-to-use multiselect interface
- ⚠️ Clear warnings for detected interactions
- ✅ Success message when no interactions are found

---
### Key Components

- **DrugDatabase** – Stores known drug–drug interactions  
- **InteractionChecker** – Core logic for detecting interactions  
- **Streamlit UI** – User interface for selecting medications and viewing results  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mernasharoeem12/drug-interaction-checker.git
cd drug-interaction-checker
```

### 2️⃣ Install Dependencies
```bash
pip install streamlit
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

The app will automatically open in your default web browser.

---

## 🧪 Example Interactions Covered

- Aspirin ↔ Warfarin — Increased bleeding risk
- Metformin ↔ Contrast Dye — Risk of lactic acidosis
- Simvastatin ↔ Grapefruit Juice — Increased toxicity
- SSRIs ↔ Tramadol — Serotonin syndrome risk

> ⚠️ The interaction list is **not exhaustive** and is intended for demonstration purposes only.

---

## ⚠️ Medical Disclaimer

This software:

- Is **not** a medical device
- Should **not** be used for diagnosis or treatment decisions
- Does **not** replace consultation with a licensed healthcare professional

Always consult a doctor or pharmacist before making medication decisions.

---

## 🛠️ Possible Enhancements

- Add interaction severity levels (low / moderate / high)
- Expand the drug database or integrate a real API
- Improve UI with expandable interaction details
- Add unit tests
- Normalize case-insensitive drug matching

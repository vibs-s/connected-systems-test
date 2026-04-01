# Connected Systems Test Automation Framework

## 📌 Overview

This project demonstrates an end-to-end automated test scenario bridging an API backend and a web frontend using:

* **Python**
* **Behave (BDD)**
* **Playwright (UI Automation)**
* **Requests (API Testing)**
* **Allure (Reporting)**

The test simulates below **connected systems workflow**:

1. A pet is created via API (Inventory System - Petstore Swagger API)
2. The returned data is used dynamically in a UI checkout flow (Storefront - SauceDemo)

---

## 🧱 Project Structure

```
connected-systems-test/
│
├── test/
│   ├── features/
│   │   ├── inventory_to_storefront.feature
│   │   └── steps/
│   │       ├── api_steps.py
│   │       └── ui_steps.py
│   │
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   │
│   ├── utils/
│   │   ├── api_client.py
│   │   └── config.py
│
├── behave.ini
├── requirements.txt
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd connected-systems-test
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Install Playwright Browsers

```
playwright install
```

---

## ▶️ Running Tests

Run Behave:

```
behave
```

## 📊 Allure Reporting

### Install Allure (Mac)

```
brew install allure
```

---

### Run Tests with Allure

```
behave -f allure_behave.formatter:AllureFormatter -o reports/
```

---

### Generate Report

```
allure serve reports/
```

---

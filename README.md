# 🧠 FPL Scout Assistant

A personal Fantasy Premier League (FPL) data assistant to help you make smarter fantasy decisions using live data from the official FPL API.

---

## 📊 Features

- 🔝 View **top-performing players** by:
  - Total points
  - Form
  - Value (Points per £m)
  - Position (e.g., Midfielder, Defender)
- 📈 **Compare players** using charts and tables
- 🕵️‍♂️ Discover **differentials** (players under 10% ownership but high performance)
- 🎯 Highlight potential **captain picks**
- ⚙️ Optional CLI/GUI for interaction
- 💾 Export results to CSV (coming soon)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Leftinant/FplScout
cd fplScout
```

### 2. Create a Virtual Environment

Linux

```bash
python3 -m venv venv
source venv/bin/activate on linux
```

Windows

```bash
python3 -m venv venv
windows-source venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If venv gives an error, run:

```bash
sudo apt install python3.12-venv
```

### 4. Run the App

```bash
python fpl_scout.py
```

---

## 🛠️ Future Features

📅 Fixture difficulty consideration

📉 Track weekly price/form changes

📤 Export data to Excel or CSV

🧩 Interactive dashboard with Streamlit

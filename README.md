# 🗂️ API Collector  

A collection of Python scripts to fetch and process data from different public APIs.  
This repository is designed as a **portfolio of API extraction projects**, demonstrating skills in handling requests, authentication, pagination, and structured data storage.  

---

## 📌 Current Scripts  

### 1. `pexels.py`  
- **API:** [Pexels API]
- **Purpose:** Fetches images from the Pexels API.  
- **Features:**  
  - Uses API key stored in `.env` for secure authentication.  
  - Handles parameters (like search queries, orientation, size).  
  - Extracts photo details (URL, photographer, dimensions).  
  - Stores results in JSON/CSV.  

---

### 2. `spaceX.py`  
- **API:** [SpaceX API] 
- **Purpose:** Collects data about SpaceX rockets.  
- **Features:**  
  - Fetches latest and past names of rockets launched.   

---

### 3. `github.py`  
- **API:** [GitHub REST API]
- **Purpose:** Fetches repositories from GitHub and extracts key details.  
- **Features:**  
  - Fetches repositories based on a search keyword.  
  - Extracts repository name and number of watchers. 
  - Supports pagination (currently fetching first 30 repos by default).
  - Prints results in a readable format or can be saved for further processing.

---

## 🚀 Tech Stack  
- **Language:** Python  
- **Libraries:** `requests`, `json`, `dotenv`, `csv`  
- **Tools:** Environment variables (`.env`) for API key management  

---

## ⚙️ Setup & Usage  

1. Clone the repository  
2. Install dependencies
3. Set up environment variables
    - Create a .env file in the root directory
    - Add your API keys
4. Run a script

---

## 🤝 Contributing

This repository is for learning and portfolio purposes, but suggestions and improvements are welcome!
# Search Engine Java Frontend
A simple frontend application for interacting with a Flask-based search engine.

## Features
- Perform search queries
- Display search results
- Pagination support

## Installation
1. Install Java and set up your environment.
2. Install `json-20250107.jar` in the `lib` folder.
3. Run the API backend using Flask.
4. Compile and run the frontend:
    ```
    javac -cp .:lib/* src/*.java
    java -cp .:lib/* Main
    ```


javac -cp "lib/*;." src/*.java
java -cp "lib/*;src" Main

Here’s a detailed `README.md` for your project:  

---

## 🟢 **Search Engine Java Frontend**

A simple and elegant frontend application built using **Java Swing** to interact with a search engine powered by a **Flask API** using **FAISS**. This frontend supports search queries, result display, and pagination.  

---

## 📦 **Project Structure**

```bash
search-engine-java-frontend/
├── src/
│   ├── Main.java         # Entry point of the application
│   ├── SearchUI.java      # User Interface with Java Swing
│   ├── ApiClient.java     # API connection to Flask backend
│   ├── SearchResult.java  # Data model for search results
├── assets/
│   ├── style.css          # Optional CSS for styling (if using HTML rendering)
│   ├── background.jpg     # Optional background image
│   ├── search-icon.png    # Search button icon
├── lib/
│   ├── json-20250107.jar  # JSON library for parsing API response
└── README.md
```

---

## ⚙️ **Features**

- Perform search queries using the **Flask API**  
- Display search results with title, description, and URL  
- Pagination support to browse multiple pages of results  
- Modern and elegant UI with customizable colors and fonts  
- Error handling for API failures and invalid inputs  

---

## 🛠️ **Prerequisites**

Make sure you have the following installed:  

- **Java Development Kit (JDK)** (Version 11 or higher)  
- **Apache Maven** (For dependency management)  
- **Flask** (Running on Python for backend)  
- **FAISS** (Configured in the backend)  
- `json-20250107.jar` (Place this in the `/lib` directory)  

---

## 🚀 **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/search-engine-java-frontend.git
cd search-engine-java-frontend
```

### **2. Install JSON Library**
- Download `json-20250107.jar` from [Maven Repository](https://mvnrepository.com/artifact/org.json/json).
- Place it in the `lib/` directory.

---

## 🧑‍💻 **Run the Backend API**
Make sure the Flask API is running on port `5000`:
```bash
python app.py
# API will be available at http://localhost:5000/search
```

---

## 💻 **Compile and Run the Frontend**
Compile all Java files:
```bash
javac -cp ".;lib/json-20250107.jar" src/*.java
```

Run the application:
```bash
java -cp ".;lib/json-20250107.jar" Main
```

_Note: On Linux or macOS, use `:` instead of `;` for classpath:_  
```bash
javac -cp ".:lib/json-20250107.jar" src/*.java
java -cp ".:lib/json-20250107.jar" Main
```

---

## 🎨 **UI Customization**

### **1. Using FlatLaf for Modern UI**  
FlatLaf is a modern look and feel for Java Swing.  
- Install FlatLaf using Maven:  
```bash
mvn install org.flatlaf:flatlaf:3.3
```
- Apply it in `Main.java`:  
```java
import com.formdev.flatlaf.FlatLightLaf;

public class Main {
    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(new FlatLightLaf());
        } catch (Exception e) {
            e.printStackTrace();
        }
        SearchUI ui = new SearchUI();
        ui.setVisible(true);
    }
}
```

---

### **2. Customize Colors Using UIManager**  
You can directly style your UI using `UIManager.put()`:  
```java
UIManager.put("Button.background", Color.decode("#007bff")); // Blue Button
UIManager.put("Button.foreground", Color.WHITE);
UIManager.put("Label.font", new Font("Arial", Font.BOLD, 14));
UIManager.put("Panel.background", Color.decode("#f8f9fa")); // Light Gray Background
```

---

### **3. Using Images for Background and Icons**  
- Place your background image (`background.jpg`) and search icon (`search-icon.png`) in the `assets/` folder.  
- Display them using Swing components:  
```java
ImageIcon backgroundIcon = new ImageIcon("assets/background.jpg");
JLabel backgroundLabel = new JLabel(backgroundIcon);
frame.setContentPane(backgroundLabel);

searchButton.setIcon(new ImageIcon("assets/search-icon.png"));
```

---

## 🧪 **API Endpoint Example**

- API URL:  
```
http://localhost:5000/search?query=java&page=1&per_page=5
```
- Example Response:
```json
[
  {
    "url": "https://example.com",
    "title": "Learn Java",
    "description": "A complete Java learning guide.",
    "distance": 0.12
  },
  {
    "url": "https://java.com",
    "title": "Java Official Site",
    "description": "Download Java and related resources.",
    "distance": 0.15
  }
]
```

---

## 🚨 **Troubleshooting**

- **API Not Responding**  
  - Ensure your Flask backend is running on port `5000`.  
- **ClassNotFoundException**  
  - Confirm `json-20250107.jar` is in the `lib` folder and included in your classpath.  
- **UI Not Displaying**  
  - Ensure Java Swing is supported on your operating system.  

---

## 🧑‍🤝‍🧑 **Contributing**

Contributions are welcome!  
- Fork the repository  
- Create a feature branch (`git checkout -b feature/new-feature`)  
- Commit your changes (`git commit -m "Add new feature"`)  
- Push to the branch (`git push origin feature/new-feature`)  
- Open a pull request  

---

## 📜 **License**

This project is licensed under the **MIT License**.  

---

## 💬 **Contact**

For any issues, feel free to raise a GitHub issue or contact me at:  
📧 **your-email@example.com**  

---

This `README.md` file provides a comprehensive overview of your project. Let me know if you'd like further adjustments!
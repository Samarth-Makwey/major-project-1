# 📊 D.A.R.A. - Data Analysis and RESTful APIs

![D.A.R.A. Platform](./ss/Screenshot%202025-12-04%20121241.png)

> A modern, full-stack data analytics platform providing clean, structured datasets through fast and reliable REST APIs.

## 🚀 Live Deployment

| Component | URL |
|-----------|-----|
| **🌐 Frontend** | [https://dara-ev5w.onrender.com](https://dara-ev5w.onrender.com) |
| **⚙️ Backend** | [https://major-project-1-sxkx.onrender.com](https://major-project-1-sxkx.onrender.com) |

---

## 📖 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Available Datasets](#available-datasets)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### 🎯 Core Features

- **📊 Multiple Curated Datasets**: Netflix, Energy Consumption, Happiness Index, Olympics, and IPL data
- **🔗 RESTful API Endpoints**: Fast, reliable JSON API endpoints for data access
- **📚 Interactive Documentation**: Comprehensive API documentation with live examples
- **🎨 Modern UI**: Clean, responsive design built with React
- **⚡ High Performance**: Optimized data processing with Python and Pandas
- **🔒 CORS Enabled**: Secure cross-origin requests for frontend-backend communication
- **🌐 Deployed & Scalable**: Running on Render for reliability and scalability

---

## 🛠️ Tech Stack

### Frontend
- **React 19** - UI library for building interactive components
- **React Router DOM** - Client-side routing
- **Vite** - Lightning-fast build tool and development server
- **CSS3** - Modern styling with responsive design

### Backend
- **Python 3.x** - Core backend language
- **Flask** - Lightweight web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **Pandas** - Data processing and analysis
- **Gunicorn** - Production WSGI server
- **NumPy & SciPy** - Numerical computing

### Deployment
- **Render** - Cloud platform for hosting both frontend and backend
- **Git** - Version control

---

## 📁 Project Structure

```
major-project-1/
├── backend/
│   ├── app.py                              # Main Flask application
│   ├── netflix.py                          # Netflix dataset functions
│   ├── happiness.py                        # Happiness index functions
│   ├── energy.py                           # Energy consumption functions
│   ├── ipl.py                              # IPL dataset functions
│   ├── olympic_api_functions.py            # Olympics API functions
│   ├── olympic_advanced_insights.py        # Advanced Olympics analytics
│   ├── requirements.txt                    # Python dependencies
│   └── start.sh                            # Render start script
│
├── DARA-frontend/
│   ├── src/
│   │   ├── main.jsx                        # React entry point
│   │   ├── App.jsx                         # Main App component
│   │   ├── App.css                         # App styling
│   │   ├── components/
│   │   │   ├── Navbar/                     # Navigation bar
│   │   │   ├── Title/                      # Hero title section
│   │   │   ├── Features/                   # Features showcase
│   │   │   └── Footer/                     # Footer component
│   │   └── views/
│   │       ├── About/                      # About page
│   │       ├── Datasets/                   # Datasets listing page
│   │       └── Documentation/              # API documentation page
│   ├── index.html                          # HTML entry point
│   ├── package.json                        # Node dependencies
│   ├── vite.config.js                      # Vite configuration
│   └── .gitignore                          # Git ignore file
│
├── data/
│   ├── netflix_cleaned.csv                 # Netflix dataset
│   ├── happiness.csv                       # Happiness index data
│   ├── global_energy_consumption.csv       # Energy consumption data
│   └── (Olympics, IPL data loaded in backend)
│
└── README.md                               # This file
```

---

## 🎯 Getting Started

### Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **Git**
- **npm** or **yarn**

### Local Development Setup

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Samarth-Makwey/major-project-1.git
cd major-project-1
```

#### 2️⃣ Backend Setup

```bash
cd backend

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

The backend will be available at `http://localhost:5000`

#### 3️⃣ Frontend Setup

```bash
cd DARA-frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

---

## 📚 API Documentation

### Base URL

```
https://major-project-1-sxkx.onrender.com
```

### Available Endpoints

#### 🏥 **Health Check**

```http
GET /
```

**Response:**
```json
{
  "status": "ok",
  "message": "🏅 Olympic Data API - Welcome!",
  "datasets": ["netflix", "happiness", "energy", "olympics", "ipl"]
}
```

#### 📖 **API Documentation**

```http
GET /api/docs
```

Returns detailed documentation for all API endpoints.

#### 🎬 **Netflix Dataset**

```http
GET /api/netflix/
GET /api/netflix/genre/<genre>
GET /api/netflix/type/<type>
GET /api/netflix/top-rated
```

#### 😊 **Happiness Index**

```http
GET /api/happiness/all
GET /api/happiness/by-region/<region>
GET /api/happiness/top-countries
GET /api/happiness/by-year/<year>
```

#### ⚡ **Energy Consumption**

```http
GET /api/energy/
GET /api/energy/<country>
GET /api/energy/renewable
GET /api/energy/trends
```

#### 🏅 **Olympics**

```http
GET /api/olympics/
GET /api/medals/top-countries
GET /api/medals/country/<noc>
GET /api/athletes/top-decorated
GET /api/sports/physical-stats
```

#### 🏏 **IPL Dataset**

```http
GET /api/ipl/
GET /api/ipl/matches
GET /api/ipl/teams
GET /api/ipl/players
```

For complete endpoint documentation with parameters and examples, visit:
🔗 [API Documentation](https://dara-ev5w.onrender.com/documentation)

---

## 📊 Available Datasets

### 1. 🎬 **Netflix Dataset**
- **Records**: 1,000+ titles
- **Fields**: Title, Type, Director, Cast, Country, Release Date, Rating, Duration, Genres, Description
- **Use Cases**: Content analysis, genre trends, production insights

### 2. 😊 **World Happiness Index**
- **Records**: 160+ countries
- **Fields**: Country, Region, Happiness Rank, Happiness Score, Economy, Health, Freedom, Generosity
- **Use Cases**: Socioeconomic analysis, happiness trends, country comparisons

### 3. ⚡ **Global Energy Consumption**
- **Records**: Comprehensive global data
- **Fields**: Country, Year, Total Consumption, Renewable %, Non-Renewable %
- **Use Cases**: Energy trends, sustainability analysis, renewable energy insights

### 4. 🏅 **Olympics**
- **Records**: 130+ years of Olympic history
- **Fields**: Athlete, Sport, Country, Medal, Year, Season, Games Location
- **Use Cases**: Olympic history, athlete performance, country dominance analysis

### 5. 🏏 **IPL (Indian Premier League)**
- **Records**: 16+ seasons of cricket data
- **Fields**: Teams, Players, Matches, Runs, Wickets, Strike Rates
- **Use Cases**: Cricket statistics, player performance, team analysis

---

## 📸 Screenshots

### Home Page
![Home Page](./ss/Screenshot%202025-12-04%20121241.png)

### Datasets Page
![Datasets](./ss/Screenshot%202025-12-04%20121258.png)

### API Documentation
![Documentation](./ss/Screenshot%202025-12-04%20121327.png)
![About](./ss/Screenshot%202025-12-04%20121405.png)

---

## 🚀 Deployment

### Frontend Deployment (Render)

1. Create a Render account at [render.com](https://render.com)
2. Connect your GitHub repository
3. Create a new Web Service
4. Configure:
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npm run preview` (or use a static site configuration)
   - **Environment**: Node
5. Deploy!

### Backend Deployment (Render)

1. In Render dashboard, create a new Web Service
2. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Environment**: Python 3
3. Add environment variables if needed
4. Deploy!

---

## 🔧 Configuration

### Environment Variables

#### Backend (`.env` or in Render dashboard)

```env
FLASK_ENV=production
FLASK_APP=app.py
PORT=5000
```

#### Frontend

Update the API base URL in `src/views/Documentation/Documentation.jsx`:
```javascript
const API_BASE_URL = 'https://major-project-1-sxkx.onrender.com';
```

---

## 📦 Dependencies

### Backend (`requirements.txt`)

```
Flask==3.0.3
Flask-Cors==5.0.0
pandas==2.2.3
numpy==2.2.4
gunicorn==23.0.0
requests==2.32.3
scikit-learn==1.6.1
```

### Frontend (`package.json`)

```json
{
  "dependencies": {
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-router-dom": "^7.9.6"
  }
}
```

---

## 🐛 Troubleshooting

### Frontend won't load documentation

- **Check**: Ensure backend is deployed and running
- **Solution**: Update API URL in `Documentation.jsx` to your backend URL

### CORS errors

- **Check**: Backend should have `CORS()` enabled
- **Solution**: Verify `Flask-CORS` is initialized in `app.py`

### Backend endpoints returning 404

- **Check**: Ensure CSV files are in the correct location
- **Solution**: Verify file paths in data loading functions

---

## 🎓 Learning Resources

- [React Documentation](https://react.dev)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Pandas Documentation](https://pandas.pydata.org/docs)
- [Render Deployment Guide](https://render.com/docs)

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License - see the LICENSE file for details.

---

## 👥 Authors

- **Samarth-Makwey** - Project Creator & Maintainer

---

## 💬 Support

For issues, questions, or suggestions:

- 📧 Open an Issue on GitHub
- 💡 Check existing issues for solutions
- 🔗 Visit the [Live Project](https://dara-ev5w.onrender.com)

---

## 🎉 Acknowledgments

- Flask and React communities for amazing frameworks
- Render for reliable cloud hosting
- All dataset providers and contributors

---

**Made with ❤️ by the D.A.R.A. team**

Last Updated: December 4, 2025

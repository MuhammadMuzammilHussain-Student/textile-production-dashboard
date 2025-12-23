# 📊 Textile Production Dashboard with Kimi K2 AI

A real-time manufacturing analytics dashboard powered by FastAPI and Kimi K2 artificial intelligence. Monitor textile production KPIs, view predictive insights, and make data-driven decisions.

## ✨ Features

### Core Metrics
- **Yield Rate**: Real-time production yield percentage
- **On-Time Delivery**: Order fulfillment timeliness
- **Wastage Rate**: Material waste monitoring
- **Fill Rate**: Order completion metrics

### AI-Powered Insights
- **Kimi K2 Predictive Intelligence**: Analyzes current production metrics
- **Risk Assessment**: Automatic risk level detection (Low/Medium/High)
- **Actionable Recommendations**: AI-generated suggestions for optimization

### Data Visualization
- **Production Metrics Trend**: 7-day historical trend lines
- **Quality Metrics**: Defect rate, consistency, thread break analysis
- **Shift Performance**: Multi-shift performance comparison
- **Equipment Status**: Real-time loom operation status

## 🚀 Live Demo

**Visit the dashboard**: https://textile-production-dashboard.onrender.com/

## 🛠 Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | FastAPI 0.100+ (Python) |
| Server | Uvicorn ASGI |
| Frontend | HTML5, CSS3, JavaScript |
| Charts | Chart.js |
| Hosting | Render.com (Free Tier) |
| AI Integration | Kimi K2 (Moonshot API) |
| Version Control | GitHub |
| Repository | `textile-production-dashboard` |

## 📁 Project Structure

```
textile-production-dashboard/
├── main.py                 # FastAPI application
├── index.html             # Dashboard UI
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
├── README.md             # Documentation
└── .gitignore
```

## 🔧 Installation & Setup

### Local Development

```bash
# Clone the repository
git clone https://github.com/MuhammadMuzammilHussain-Student/textile-production-dashboard
cd textile-production-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export KIMI_API_KEY="your-api-key-here"

# Run the application
python main.py

# Visit http://localhost:8000
```

### Environment Variables

```bash
KIMI_API_KEY=sk-xxxxx  # Your Kimi API key from https://www.kimi.com/coding
PORT=8000             # Optional: Default is 8000
```

## 📊 API Endpoints

### `GET /`
Serves the dashboard HTML interface.

### `GET /api/kpis`
Returns current textile KPI metrics.

**Response**:
```json
{
  "yield_pct": 94.2,
  "on_time_delivery": 88.5,
  "total_wastage": 5.8,
  "order_fill_rate": 91.2
}
```

### `GET /api/predictive-insights`
Returns AI-powered predictions and risk assessment.

**Response**:
```json
{
  "prediction": "Current yield at 94.2% is excellent...",
  "risk_level": "Low"
}
```

## 🌐 Cloud Deployment

This project is deployed on Render.com with automatic CI/CD:

1. **Build Command**: `pip install -r requirements.txt`
2. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. **Auto-Deploy**: Triggered on GitHub main branch commits
4. **Instance Type**: Free (auto-sleeps after 15 min inactivity)

## 🤖 Kimi K2 Integration

The dashboard uses Kimi K2 for:
- Natural language analysis of production data
- Predictive wastage assessment
- Risk level calculation
- Actionable recommendations

**API Endpoint**: `https://api.moonshot.cn/v1/chat/completions`
**Model**: `moonshot-v1-8k`

## 📈 Dashboard Sections

### 1. KPI Cards
Four prominent metric cards showing current performance:
- Color-coded values (green for good, red for caution)
- Responsive grid layout
- Hover animations

### 2. Kimi K2 Predictive Insight
AI-analyzed production insights with:
- Brief prediction text
- Risk level badge
- Gradient background styling

### 3. Production Metrics Trend
Multi-line chart showing 7-day trends:
- Yield percentage (green line)
- On-time delivery (blue line)
- Wastage rate (red line)
- Interactive legend

### 4. Detailed Metrics Boxes
- Production Status (loom operations)
- Quality Metrics (defect rate, consistency)
- Shift Performance (morning/evening/night)

## 🔐 Security

- API keys stored in environment variables
- No secrets committed to repository
- HTTPS support on live deployment
- CORS-enabled for frontend integration

## 📝 Dependencies

```
fastapi==0.100.0
uvicorn==0.24.0
pydantic==2.5.0
pandas==2.1.0
openpyxl==3.10.10
httpx==0.25.0
```

## 🚢 Deployment Instructions

### Via Render.com

1. Push code to GitHub
2. Connect repository to Render
3. Configure build/start commands
4. Set `KIMI_API_KEY` in environment variables
5. Deploy with one click

### Manual

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 📚 Future Enhancements

- [ ] Database integration (PostgreSQL)
- [ ] Real-time data ingestion from IoT sensors
- [ ] Advanced analytics dashboards
- [ ] Multi-user authentication
- [ ] Email alerts for anomalies
- [ ] Mobile app
- [ ] Historical data export (CSV/PDF)
- [ ] Custom report generation
- [ ] Predictive maintenance scheduling
- [ ] Machine learning model integration

## 👨‍💻 Author

**Muhammad Muzammil Hussain**
- GitHub: [@MuhammadMuzammilHussain-Student](https://github.com/MuhammadMuzammilHussain-Student)
- Email: [Your Email]

## 📄 License

MIT License - Feel free to use this project for commercial and personal purposes.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For issues, questions, or suggestions, please:
- Open a GitHub Issue
- Contact via email
- Check existing documentation

## 🎯 Project Goals

✅ Real-time textile production monitoring
✅ AI-powered predictive analytics
✅ Cloud deployment with auto-scaling
✅ Responsive dashboard UI
✅ RESTful API design
✅ Production-ready code

---

**Last Updated**: December 23, 2025
**Status**: ✅ Production Ready

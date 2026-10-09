# AI Resume Analyzer

A full-stack web application that uses AI to analyze resume compatibility with job descriptions. Built with React, Vite, Express, and the Groq API.

## Project Evolution

This project began as a Python script (`resume_parse.py`) that demonstrated the core resume parsing and matching logic using the Groq API. It was later evolved into this full-stack web application to provide a more user-friendly, interactive experience with modern UI/UX enhancements.

## Features

- **Modern Drag-and-Drop Interface**: Intuitive file upload with visual feedback
- **AI-Powered Analysis**: Uses Groq's LLM to extract resume details and match against job requirements
- **Real-time Matching**: Get instant compatibility scores and detailed feedback
- **Responsive Design**: Works on desktop and mobile devices
- **Visual Progress Indicators**: Circular progress charts showing match percentages
- **Detailed Breakdown**: See matched skills, missing skills, strengths, and areas for growth

## How It Works

1. **Upload Resume**: Drag and drop or select a PDF resume file
2. **Enter Job Description**: Paste the target job description or requirements
3. **Get Analysis**: Click "Analyze Compatibility" to start the AI-powered evaluation
4. **View Results**: See your match score, detailed feedback, and eligibility status

## Technical Stack

### Frontend (Client)
- **React** with **Vite** for fast development
- **Tailwind CSS** for modern, responsive styling
- **Hooks**: useState, useRef, useCallback for state management

### Backend (Server)
- **Node.js** with **Express** for REST API
- **pdf-parse** for PDF text extraction
- **Groq SDK** for LLM-powered resume analysis and matching
- **Multer** for handling file uploads
- **CORS** for frontend-backend communication

### API Endpoints
- `POST /api/upload-resume`: Main endpoint for resume analysis
  - Accepts: PDF file + job description
  - Returns: Parsed resume data, match score, skills analysis, explanation, and eligibility

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   # Install frontend dependencies
   cd client
   npm install
   
   # Install backend dependencies  
   cd ../server
   npm install
   ```
3. **Configure environment variables**:
   - Create `.env` files in both `client/` and `server/` directories
   - Add your Groq API key to the server's `.env`: `GROQ_API_KEY=your_key_here`
4. **Start the development servers**:
   ```bash
   # Start backend (port 5000)
   cd server
   npm run dev
   
   # In another terminal, start frontend (port 5175)
   cd ../client
   npm run dev
   ```
5. **Open your browser** to `http://localhost:5175`

## Project Structure

```
Resume_Parser/
├── client/                 # Frontend React/Vite application
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── MatchResults.jsx    # Results display with circular progress
│   │   │   └── ResumeUploadForm.jsx # Upload form with drag-and-drop
│   │   ├── main.jsx        # Entry point
│   │   └── index.css       # Global styles
│   ├── index.html          # HTML template
│   ├── package.json        # Frontend dependencies
│   ├── vite.config.js      # Vite configuration with Tailwind
│   └── tailwind.config.js  # Tailwind CSS configuration
│
├── server/                 # Backend Express application
│   ├── server.js           # Main server file with API routes
│   ├── package.json        # Backend dependencies
│   └── .env                # Environment variables (Groq API key)
│
├── .env                    # Root environment variables
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

## Key Features Explained

### Resume Upload Form
- Drag-and-drop area with hover and drag feedback
- File validation (PDF only, 5MB limit)
- Visual file preview with name and size
- Remove file functionality
- Loading states and error handling
- Modern gradient design with smooth animations

### Match Results Display
- Circular SVG progress indicator showing match percentage
- Color-coded scoring (green ≥80, yellow 70-79, red <70)
- Eligibility status (✓/✗) based on 70-point threshold
- Skills breakdown in flexible grid layout
- Strengths and growth areas sections
- Detailed AI-generated explanation

### Backend Processing
1. Receives PDF file and job description
2. Extracts text from PDF using pdf-parse
3. Uses Groq to parse resume into structured JSON
4. Uses Groq to compare resume against job description
5. Returns comprehensive analysis including:
   - Match score (0-100)
   - Matched and missing skills
   - Strengths and weaknesses
   - Detailed explanation
   - Eligibility flag (score ≥ 70)

## Environment Variables

Create `.env` files in both directories:

**server/.env**:
```
GROQ_API_KEY=your_groq_api_key_here
PORT=5000
```

**client/.env** (if needed for proxy):
```
VITE_API_URL=http://localhost:5000
```

## Dependencies

### Frontend
- react
- react-dom
- vite
- @vitejs/plugin-react
- tailwindcss
- @tailwindcss/vite

### Backend
- express
- cors
- dotenv
- multer
- pdf-parse
- groq-sdk

## Usage Tips

- Ensure your PDF resume contains selectable text (not scanned images)
- Be specific in your job description for better matching
- The analysis takes a few seconds - please wait for results
- Scores are meant as helpful guidance, not definitive hiring decisions
- You can analyze multiple resumes against the same job description

## Customization

To modify the analysis criteria, edit the system prompts in `server/server.js`:
- `parseResumeWithGroq()` function for resume parsing
- `matchResumeWithGroq()` function for job matching

The scoring weights in the matching prompt can be adjusted to emphasize different factors (technical skills, experience, etc.).

---

**Note**: This application demonstrates AI-assisted resume analysis and should be used as a tool to support, not replace, human judgment in recruitment processes.
# 🎁 Wish List Application

A full-stack application that allows users to submit a wish list through a modern web interface, which is then delivered instantly via email to the recipient.

## 🚀 Tech Stack
- **Frontend**: React.js
- **Backend**: Python (FastAPI)
- **Email**: Gmail SMTP
- **Styling**: Custom CSS

## 🛠️ Setup Instructions

### 1. Backend Setup
1. Navigate to the backend directory:
   \`\`\`bash
   cd backend
   \`\`\`
2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Configure environment variables:
   Create a `.env` file in the `backend/` folder:
   \`\`\`text
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   \`\`\`
   *(Note: Use a Google App Password, not your regular password).*
4. Start the server:
   \`\`\`bash
   python -m uvicorn main:app --reload
   \`\`\`

### 2. Frontend Setup
1. Navigate to the frontend directory:
   \`\`\`bash
   cd frontend
   \`\`\`
2. Install dependencies:
   \`\`\`bash
   npm install
   \`\`\`
3. Start the application:
   \`\`\`bash
   npm start
   \`\`\`

## 📧 How it Works
- The user fills out a form with their Name, Items, Priority, and a Link.
- React sends this data as a JSON payload to the FastAPI `/submit-wishlist` endpoint.
- FastAPI validates the data and uses `smtplib` to send a formatted HTML email to the designated recipient.

## 📌 Project Structure
- `backend/`: Python FastAPI source code and configuration.
- `frontend/`: React.js source code and styling.
- `docs/`: Design specs and implementation plans.

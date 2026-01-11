import axios from 'axios';

 const api = axios.create({
    baseURL: 'http://localhost:8000/', // Your backend URL
    timeout: 60000, // 30 seconds (AI responses can take time)
    headers: {
      'Content-Type': 'application/json',
      // Add authentication if needed
      // 'Authorization': `Bearer ${yourToken}`
    }
  });

export default api;
import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import PostReview from "./components/Dealers/PostReview";
import Dealers from './components/Dealers/Dealers';

function App() {
  // Retrieve the backend URL from the environment variables
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  console.log("Backend URL:", backendUrl); // For debugging purposes

  return (
    <Routes>
      {/* Login route */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Register route */}
      <Route path="/register" element={<Register />} />

      {/* Default route (optional, redirect to login or another page) */}
      <Route path="*" element={<LoginPanel />} />

      <Route path="/postreview/:id" element={<PostReview />} />

      {/* Dealers route - optionally pass the backend URL as a prop */}
      <Route path="/dealers" element={<Dealers backendUrl={backendUrl} />} />
    </Routes>
  );
}

export default App;

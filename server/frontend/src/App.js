import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import PostReview from "./components/Dealers/PostReview";
import Dealers from './components/Dealers/Dealers';

function App() {
  return (
    <Routes>
      {/* Login route */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Register route */}
      <Route path="/register" element={<Register />} />

      {/* Default route (optional, redirect to login or another page) */}
      <Route path="*" element={<LoginPanel />} />

      <Route path="/postreview/:id" element={<PostReview/>} />

      <Route path="/dealers" element={<Dealers/>} />

    </Routes>
  );
}

export default App;

import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";

function App() {
  return (
    <Routes>
      {/* Login route */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Register route */}
      <Route path="/register" element={<Register />} />

      {/* Default route (optional, redirect to login or another page) */}
      <Route path="*" element={<LoginPanel />} />
    </Routes>
  );
}

export default App;

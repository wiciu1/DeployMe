import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute.jsx";
import {ACCESS_TOKEN, REFRESH_TOKEN} from "./constants.js";
import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import NotFound from "./components/NotFound.jsx";
import { ToastContainer } from "react-toastify";
import Header from './components/Header/Header.jsx';
import ReverseProtectedRoute from "./components/ReverseProtectedRoute.jsx";
import {useEffect} from "react";
import {useAuth} from "./components/AuthContext.jsx";

function Logout() {
  const { logout } = useAuth();

  useEffect(() => {
    logout();
  }, [logout]);

  return <Navigate to="/login" />;
}


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          } />

          <Route path="/login" element={
            <ReverseProtectedRoute>
              <Login />
            </ReverseProtectedRoute>
          } />

          <Route path="/register" element={
            <ReverseProtectedRoute>
              <Register />
            </ReverseProtectedRoute>
          } />

          <Route path="/logout" element={<Logout />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
        <ToastContainer position="top-center" />
      </BrowserRouter>
    </div>
  )
}

export default App
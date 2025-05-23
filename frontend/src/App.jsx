import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute.jsx";
import {ACCESS_TOKEN, REFRESH_TOKEN} from "./constants.js";
import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import NotFound from "./components/NotFound.jsx";
import { ToastContainer } from "react-toastify";
import Header from './components/Header/Header.jsx';

function Logout() {
  localStorage.removeItem(ACCESS_TOKEN);
  localStorage.removeItem(REFRESH_TOKEN);
  return <Navigate to="/login" />
}


function App() {
  return (
      <div className="App">
          <BrowserRouter>
          <Header />
          <Routes>
            <Route
              path="/" element={
                <ProtectedRoute>
                  <Home/>
                </ProtectedRoute>
              }
            />
                <Route path="/login" element= {<Login />} />
            <Route path="/logout" element={ <Logout />} />
            <Route path="/register" element={ <Register />} />
            <Route path="*" element={ <NotFound/> } />
      </Routes>
      <ToastContainer position="top-center"/>
    </BrowserRouter>
      </div>

  )
}

export default App
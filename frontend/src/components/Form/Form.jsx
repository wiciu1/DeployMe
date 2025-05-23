import { useState } from "react";
import api from "../../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../../constants";
import { toast } from "react-toastify";
import { useAuth } from "../AuthContext.jsx";

import "./Form.css";

function Form({ route, method }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [email, setEmail] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const {setIsAuthenticated} = useAuth();

  const name = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();
    const data = {username, password};

    // Add to data if it's register
    if (method === 'register') {
      data.email = email;
      data.password2 = confirmPassword;
      data.bio = "";
    }
    try {
      const response = await api.post(route, data);
      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, response.data.access);
        localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
        setIsAuthenticated(true);
        navigate("/");
        toast.success("Successfully logged in.")
      } else if(method === "register"){
        toast.success("Created account successfully.")
        navigate("/login");
      }
    } catch (err) {
      if (err && err.response && err.response.data) {
        const errors = err.response.data;
        if (errors.detail) {
          toast.error(errors.detail);
        } else {
          Object.keys(errors).forEach((field) => {
            const fieldErrors = errors[field];

            fieldErrors.forEach((msg) => {
              toast.error(`${field}: ${msg}`);
            });
        });
        }
      }
      else {
          toast.error("An error occured.");
        }
    } finally {
      setLoading(false);
    }
  };

  return (
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-md-4">
            <img src="/images/deployme-banner.png"/>
            <form onSubmit={handleSubmit} className="p-4 rounded shadow form-container">
              <h1 className="text-center mb-4 form-header">{name}</h1>

              <div className="mb-3">
                <input
                    type="text"
                    className="form-control"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                    required
                />
              </div>

              {method === "register" && (
                  <div className="mb-3">
                    <input
                        type="email"
                        className="form-control"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder="Email"
                        required
                    />
                  </div>
              )}

              <div className="mb-3">
                <input
                    type="password"
                    className="form-control"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
              </div>

              {method === "register" && (
                  <div className="mb-3">
                    <input
                        type="password"
                        className="form-control"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        placeholder="Confirm Password"
                        required
                    />
                  </div>
              )}

              <button
                  type="submit"
                  className="btn btn-primary w-100"
                  disabled={loading}
              >
                {loading ? "Loading..." : name}
              </button>
              <br/>
              <br/>
               {method === 'login' && (
                   <div className="row justify-content-center">
                     <p>Don't have an account? <a href="/register" className="anchor">Create one</a></p>
                   </div>
               )}
              {method === 'register' && (
                   <div className="row justify-content-center">
                     <p>Do you have account? <a href="/login" className="anchor">Login here</a></p>
                   </div>
               )}
            </form>
                 </div>
                 </div>
                 </div>
  );
}

export default Form;

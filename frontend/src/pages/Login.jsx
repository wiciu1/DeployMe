import Form from "../components/Form/Form.jsx"
import { useAuth } from "../components/AuthContext.jsx";
import {useNavigate} from "react-router-dom";
import {useEffect} from "react";

function Login() {
  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (isAuthenticated) {
      navigate("/");
    }
  }, [isAuthenticated, navigate]);

  return <Form route="/api/token/" method="login" />;
}

export default Login;
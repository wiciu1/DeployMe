import {jwtDecode} from "jwt-decode"
import api from "../api"
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"
import {useState, useEffect } from "react"
import axios from "axios";
import {Navigate} from "react-router-dom";

function ProtectedRoute({children}) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        if(!refreshToken) {
            throw new Error("No refresh token.");
        }

        // Try to send request to backend
        try {
            const response = await api.post(
                "/api/token/refresh/",
                { refresh: refreshToken, });

            if (response && response.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                axios.defaults.headers.common.Authorization = `Bearer ${response.data.access}`;
                setIsAuthorized(true);

            } else {
                setIsAuthorized(false);
            }
        } catch (e) {
            localStorage.removeItem(ACCESS_TOKEN);
            localStorage.removeItem(REFRESH_TOKEN);
            setIsAuthorized(false);
            throw e;
        }
    }

    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);

        if(!token) {
            setIsAuthorized(false);
            return;
        }

        const decoded = jwtDecode(token);
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        if (tokenExpiration < now) {
            await refreshToken();
        } else {
            setIsAuthorized(true)
        }
    }

     useEffect(() => {
        auth().catch((e) => () => {
            setIsAuthorized(false);
            console.log(e)
        }) ;
    }, []);


    if(isAuthorized === null) {
        return <div>Loading...</div>
    }

    return isAuthorized ? children : <Navigate to="/login" />

}


export default ProtectedRoute;
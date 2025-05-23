import { createContext, useContext, useState, useEffect } from 'react';
import axios from "axios";
import api from "../api"
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"
import {jwtDecode} from "jwt-decode";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(null);

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
                    setIsAuthenticated(true);

                } else {
                    setIsAuthenticated(false);
                }
            } catch (e) {
                localStorage.removeItem(ACCESS_TOKEN);
                localStorage.removeItem(REFRESH_TOKEN);
                setIsAuthenticated(false);
                throw e;
            }
        }

        const checkAuth = async () => {
            const token = localStorage.getItem(ACCESS_TOKEN);

            if(!token) {
                setIsAuthenticated(false);
                return;
            }

            const decoded = jwtDecode(token);
            const tokenExpiration = decoded.exp;
            const now = Date.now() / 1000;

            if (tokenExpiration < now) {
                await refreshToken();
            } else {
                setIsAuthenticated(true)
            }
        }

        useEffect(() => {
            checkAuth();
        }, []);

        const logout = () => {
          localStorage.removeItem(ACCESS_TOKEN);
          localStorage.removeItem(REFRESH_TOKEN);
          setIsAuthenticated(false);
        };

        return (
        <AuthContext.Provider
            value={{ isAuthenticated, setIsAuthenticated, checkAuth, logout }}
            >
            {children}
        </AuthContext.Provider>
        );
}
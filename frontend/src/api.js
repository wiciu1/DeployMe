import axios from 'axios';
import { ACCESS_TOKEN, REFRESH_TOKEN } from './constants.js'

// Configure custom api fetcher. Link base url
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// Add a request interceptor
api.interceptors.request.use(
    (config) =>  {
        // Get Access Token from localStorage
        const token = localStorage.getItem(ACCESS_TOKEN);
        // If found, add bearer header
        if(token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// Add a response interceptor
api.interceptors.response.use(
    // Status 200: Token didn't expire yet
    (response) => {
        return response;
    },
    async (error) => {
        // If response is 401: (Not authorized, (?) token expired): Try to refresh token
        if (error.response && error.response.status === 401) {
            const refreshToken = localStorage.getItem(REFRESH_TOKEN);

            if (refreshToken) {
                try {
                    const { data } = await axios.post(
                        "/api/token/refresh/",
                        { refresh: refreshToken}
                    );

                    localStorage.setItem('access', data.access);

                    // Redo response
                    error.config.headers.Authorization = `Bearer ${data.access}`;
                    return api(error.config);

                } catch (e) {
                    console.log("Token refresh failed.", e);
                    localStorage.clear();
                }
            }
        }
        // Error not linked to 401, probably app error.
        return Promise.reject(error);
}
);

export default api;
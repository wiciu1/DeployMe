import JobOffersList from "../components/JobOffersList.jsx";
import {useAuth} from "../components/AuthContext.jsx";
import {Navigate} from "react-router-dom";

function Home() {
    const { isAuthenticated} = useAuth();

    if (!isAuthenticated) {
        return <Navigate to="/login"/>
    }
    return <JobOffersList />
}

export default Home
import JobOffersList from "../components/JobOffersList.jsx";
import { useAuth } from "../components/AuthContext.jsx";
import { Navigate } from "react-router-dom";
import Filters from "../components/Filters/Filters.jsx";
import { useState } from "react";

function Home() {
    const { isAuthenticated } = useAuth();
    const [filters, setFilters] = useState({});
    if (!isAuthenticated) {
        return <Navigate to="/login" />;
    }

    return (
        <div className="container mt-4">
            <div className="row">
                <div className="col-md-3">
                    <Filters onFilterChange={setFilters}/>
                </div>
                <div className="col-md-9">
                    <JobOffersList filters={filters}/>
                </div>
            </div>
        </div>
    );
}

export default Home;
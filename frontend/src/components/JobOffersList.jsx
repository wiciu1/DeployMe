import {useEffect, useState} from "react";
import api from "../api.js";
import JobOfferCard from "../components/JobOfferCard/JobOfferCard.jsx";
import ReactPaginate from "react-paginate";
import Pagination from "./Pagination/Pagination.jsx";

function JobOffersList({filters}) {
    const [offers, setOffers] = useState([]);
    const [loading, setLoading] = useState(false);

    // Pagination
    const [page, setPage] = useState(1);
    const pageSize = 30;
    const [count, setCount] = useState(0);

    const buildQueryParams = (page, filters) => {
        const params = new URLSearchParams();
        params.set('page', page);
        params.set('page_size', pageSize);

        Object.entries(filters).forEach(([key, value]) => {
            if (value !== undefined && value !== '' && value !== null) {
                params.set(key, value);
            }
        });

        return params.toString();
    };


    const fetchOffers = async (page = 1, filters = {}) => {
        try {
            setLoading(true);
            const queryParams = buildQueryParams(page, filters);
            const response = await api.get(`/api/get-job-offers/?${queryParams}`);
            setOffers(response.data.results);
            setPage(page);
            setCount(response.data.count);
        } catch (e) {
            alert(e);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        fetchOffers(1, filters);
    }, [filters]);

    const totalPages = Math.ceil(count / pageSize);

    const handlePageClick = (e) => {
        const selectedPage = e.selected + 1;
        window.scrollTo({top: 0, behavior: "smooth"});
        fetchOffers(selectedPage, filters);
    }

    return (
        <div>
            <h2 className="text-white mb-4">Job Offers: ({count})</h2>
            {loading && (
                <div className="text-center py-5">
                    <div className="spinner-border text-primary" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </div>
                </div>
            )}

            {!loading && offers.length === 0 && (
                <div className="alert alert-info">Found 0 offers with given criteria</div>)}

            {offers.map((offer) => (
                <JobOfferCard
                    key={offer.id}
                    url={offer.url}
                    title={offer.title}
                    company_name={(offer.company === 'undefined') ? '' : offer.company}
                    location={offer.location}
                    seniority={offer.seniority}
                    salary={(offer.salary === 'undefined') ? '' : offer.salary}
                    technologies={offer.technologies}
                    portal={offer.portal}
                    created_at={offer.created_at}
                />
            ))}
            <Pagination
                pageCount={totalPages}
                onPageChange={handlePageClick}
                currentPage={page}
            />
        </div>

    )
}

export default JobOffersList;
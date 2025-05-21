import {useEffect, useState} from "react";
import api from "../api.js";
import JobOfferCard from "../components/JobOfferCard/JobOfferCard.jsx";
import ReactPaginate from "react-paginate";
import Pagination from "./Pagination/Pagination.jsx";

function JobOffersList() {
    const [offers, setOffers] = useState([]);
    const [loading, setLoading] = useState(false);

    // Pagination
    const [page, setPage] = useState(1);
    const pageSize = 30;
    const [count, setCount] = useState(0);

        const fetchOffers = async (page = 1) => {
            try {
                setLoading(true);
                const response = await api.get(`/api/get-job-offers/?page=${page}&page_size=${pageSize}`);
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
        fetchOffers(1);
    }, []);

    const totalPages = Math.ceil(count / pageSize);

    const handlePageClick = (e) => {
        const selectedPage = e.selected + 1;
        window.scrollTo({top: 0, behavior: "smooth"});
        fetchOffers(selectedPage);
    }

    return (
        <div>
            <h2 className="text-white mb-4">Job Offers</h2>
            {loading && (
                <div className="text-center py-5">
                    <div className="spinner-border text-primary" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </div>
                </div>
            )}
            {offers.map((offer) => (
                <JobOfferCard
                    key={offer.id}
                    url={offer.url}
                    title={offer.title}
                    company_name={offer.company}
                    location={offer.location}
                    seniority={offer.seniority}
                    salary={offer.salary}
                    technologies={offer.technologies}
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

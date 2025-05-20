import {useEffect, useState} from "react";
import api from "../api.js";

function JobOffersList() {
    const [offers, setOffers] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchOffers = async () => {
            try {
                setLoading(true);
                const response = await api.get('/api/get-job-offers/');
                setOffers(response.data);

            } catch (e) {
                alert(e);
            } finally {
                setLoading(false);
            }
        }
        fetchOffers();
    }, []);

    return (
    <div>
        <h2>Job Offers</h2>
        <ul>
            {offers.map((offer) => (
                <li key={offer.id}>
                    <strong>{offer.title}</strong> – {offer.company_name}
                </li>
            ))}
        </ul>
    </div> )

}

export default JobOffersList;
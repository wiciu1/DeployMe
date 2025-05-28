
import "./JobOfferCard.css"

function JobOfferCard({ title, url, company_name, location, seniority, salary, technologies, portal, created_at }) {
    return (
        <div className="card mb-4 shadow-sm border-0 custom-bg p-3">
            <div className="card-body">

                <div className="d-flex justify-content-between align-items-center mb-3 flex-wrap">
                    <div>
                        <h5 className="card-title custom-title mb-1">
                            <a href={url} className="text-decoration-none" target="_blank">{title}</a>
                        </h5>
                        {company_name && (
                            <>
                                <br/>
                                <h6 className="card-subtitle mb-0">{company_name}</h6>
                            </>
                        )}

                    </div>

                    <div className="d-flex flex-column align-items-end mt-2">
                        <div className="text-success fw-bold fs-5">{salary}</div>
                        <div className="d-flex align-items-center gap-2">
                            <span className="custom-subtitle">Added: {created_at}</span>
                            <i className="bi bi-bookmark fs-3"></i>
                        </div>
                    </div>
                </div>
                <br/>

                <div className="d-flex mb-3 gap-2 flex-wrap">
                    <span className="badge bg-secondary"><i className="bi bi-geo-alt"></i> {location}</span>
                    <span className="badge bg-secondary">{seniority}</span>
                </div>

                <div className="d-flex mb-3 gap-2 flex-wrap">
                    <span className="badge bg-primary">{portal}</span>
                </div>

                    <div className="d-flex justify-content-end flex-wrap gap-2">
                        {technologies.map((tech, index) => (
                            <span key={index} className="badge bg-light text-dark border">{tech.name}</span>
                        ))}

                    </div>

                </div>
            </div>
            );
            }

            export default JobOfferCard;
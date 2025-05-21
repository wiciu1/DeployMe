
import "./JobOfferCard.css"

function JobOfferCard({ title, url, company_name, location, seniority, salary, technologies }) {
    const cleanTechnologies = technologies.replace(/\[|\]|'/g, "").split(', ').map(item => item.trim());
    return (
        <div className="card mb-4 shadow-sm border-0 custom-bg p-3">
            <div className="card-body">

                <div className="d-flex justify-content-between align-items-center mb-3 flex-wrap">
                    <div>
                        <h5 className="card-title custom-title mb-1">
                            <a href={url} className="text-decoration-none" target="_blank">{title}</a>
                        </h5>
                        <br/>
                        <h6 className="card-subtitle mb-0">{company_name}</h6>
                    </div>

                    <div className="d-flex align-items-center gap-3 mt-2 mt-sm-0">
                        <div className="text-success fw-bold fs-5">{salary}</div>
                        <span style={{cursor: "pointer", fontSize: "1.5rem", color: "gray"}}>❤</span>
                    </div>
                </div>
                <br/>

                <div className="d-flex mb-3 gap-2 flex-wrap">
                    <span className="badge bg-secondary"><i className="bi bi-geo-alt"></i> {location}</span>
                    <span className="badge bg-secondary">{seniority}</span>
                </div>

                <div className="d-flex justify-content-end flex-wrap gap-2">
                    {cleanTechnologies.map((tech, index) => (
                     <span key={index} className="badge bg-light text-dark border">{tech}</span>
                    ))}
                </div>

            </div>
        </div>
    );
}

export default JobOfferCard;
import { useState } from "react";

function Filters({onFilterChange}) {
    const [formData, setFormData] = useState({
        salary: '',
        seniority: [],
        location: '',
        technologies: [],
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;

        if (type === "checkbox") {
            setFormData(prev => {
                const newSeniority = checked
                    ? [...prev.seniority, value]
                    : prev.seniority.filter(lvl => lvl !== value);

                return { ...prev, seniority: newSeniority };
            });
        } else if (name === "technologies") {
            const options = Array.from(e.target.selectedOptions, option => option.value);
            setFormData(prev => ({ ...prev, technologies: options }));
        } else {
            setFormData(prev => ({ ...prev, [name]: value }));
        }
    };


    const handleSubmit = (e) => {
        e.preventDefault();
        const filters = {
            ...(formData.salary_min && { salary_min: formData.salary_min }),
            ...(formData.salary_max && { salary_max: formData.salary_max }),
            ...(formData.seniority.length > 0 && { seniority: formData.seniority.join(',') }),
            ...(formData.location && { location: formData.location }),
            ...(formData.technologies.length > 0 && { technologies: formData.technologies.join(',') })
        };
        onFilterChange(filters);
    };

    const handleReset = () => {
        setFormData({
            salary: '',
            seniority: [],
            location: "",
            technologies: []
        });
        onFilterChange({});
    };
    return (
        <div className="card mb-4 shadow-sm border-0 custom-bg p-3">
            <div className="card-body">
                <h5 className="card-title">Job offers filters</h5>
                <form onSubmit={handleSubmit} onReset={handleReset}>

                    <div className="mb-3">
                        <label className="form-label">Seniority</label>
                        <div className="form-check">
                            <input
                                className="form-check-input"
                                type="checkbox"
                                value="trainee"
                                id="trainee"
                                checked={formData.seniority.includes('trainee')}
                                onChange={handleChange}
                            />
                            <label className="form-check-label" htmlFor="trainee">
                                Trainee
                            </label>
                        </div>
                        <div className="form-check">
                            <input
                                className="form-check-input"
                                type="checkbox"
                                value="junior"
                                id="junior"
                                checked={formData.seniority.includes('junior')}
                                onChange={handleChange}
                            />
                            <label className="form-check-label" htmlFor="junior">
                                Junior
                            </label>
                        </div>
                    </div>

                    <div className="mb-3">
                        <label htmlFor="location" className="form-label">Location</label>
                        <select
                            className="form-select"
                            id="location"
                            name="location"
                            value={formData.location}
                            onChange={handleChange}
                        >
                            <option value="">All</option>
                            <option value="remote">Remote</option>
                            <option value="warszawa">Warszawa</option>
                            <option value="krakow">Kraków</option>
                            <option value="wroclaw">Wrocław</option>
                            <option value="gdansk">Gdansk</option>
                        </select>
                    </div>

                    <div className="mb-3">
                        <label htmlFor="technologies" className="form-label">Technologies</label>
                        <select
                            className="form-select"
                            id="technologies"
                            name="technologies"
                            multiple
                            value={formData.technologies}
                            onChange={handleChange}
                        >
                            <option value="python">Python</option>
                            <option value="javascript">JavaScript</option>
                            <option value="java">Java</option>
                            <option value="c++">C++</option>
                            <option value="c">C</option>
                            <option value="html">HTML</option>
                            <option value="php">PHP</option>
                        </select>
                    </div>

                    <div className="d-grid gap-2 d-md-flex justify-content-md-end">
                        <button type="reset" className="btn btn-outline-secondary me-md-2">
                            Clear Filters
                        </button>
                        <button type="submit" className="btn btn-primary">
                            Filter
                        </button>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Filters;


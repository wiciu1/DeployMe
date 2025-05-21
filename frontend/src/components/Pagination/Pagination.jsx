import React from "react";
import ReactPaginate from "react-paginate";
import "./Pagination.css";

const Pagination = ({ pageCount, onPageChange, currentPage }) => {
  return (
    <ReactPaginate
      previousLabel={'<'}
      nextLabel={">"}
      breakLabel={"..."}
      pageCount={pageCount}
      marginPagesDisplayed={1}
      pageRangeDisplayed={4}
      onPageChange={onPageChange}
      forcePage={currentPage - 1}
      containerClassName={"pagination"}
      pageClassName={"page-item"}
      pageLinkClassName={"page-link"}
      previousClassName={"page-item"}
      previousLinkClassName={"page-link"}
      nextClassName={"page-item"}
      nextLinkClassName={"page-link"}
      breakClassName={"break-link"}
      breakLinkClassName={"page-link"}
      activeClassName={"active"}
      disabledClassName={"disabled"}
    />
  );
};

export default Pagination;
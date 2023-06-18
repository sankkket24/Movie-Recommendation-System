import React from 'react';

const SearchBar = ({ handleChange }) => {
  return (
    <div className="input-group mb-3">
      <input
        type="text"
        className="form-control"
        placeholder="Search"
        onChange={handleChange}
      />
      <div className="input-group-append">
        <button className="btn btn-primary" type="button">
          Search
        </button>
      </div>
    </div>
  );
};

export default SearchBar;

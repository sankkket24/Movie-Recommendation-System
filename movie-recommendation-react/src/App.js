import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.post('/title', { title: searchTerm });
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };

  const handleChange = (event) => {
    setSearchTerm(event.target.value);
  };

  return (
    <div className="container">
      <div className="row">
        <div className="col">
          <div className="input-group my-3">
            <input
              type="text"
              className="form-control"
              placeholder="Search movies..."
              value={searchTerm}
              onChange={handleChange}
            />
            <button className="btn btn-primary" onClick={handleSearch}>
              Search
            </button>
          </div>
          <div>
            {searchResults.length > 0 ? (
              <ul className="list-group">
                {searchResults.map((movie, index) => (
                  <li className="list-group-item" key={index}>
                    {movie.title}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No results found.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;


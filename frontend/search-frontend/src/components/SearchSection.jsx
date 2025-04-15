import React, { useState,useEffect } from 'react';
import './SearchSection.css';

export function SearchSection({ onSearch, query: parentQuery }) {
  const [query, setQuery] = useState(parentQuery || '');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setQuery(parentQuery || '');
    if (parentQuery) {
      fetchSearch(parentQuery);
    }
  }, [parentQuery]);

  const fetchSearch = async (q) => {
    setLoading(true);
    try {
      const res = await fetch(`http://localhost:5000/search_links?query=${encodeURIComponent(q)}`);
      const data = await res.json();
      setResults(data.results?.slice(0, 5) || []);
    } catch (err) {
      console.error('Search failed:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = () => {
    if (!query.trim()) return;
    onSearch(query);
  };

  return (
    <div className="search-section">
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search here..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {loading && <p className="loading-text">Searching...</p>}

      <div className="search-results">
        {results.map((item, index) => (
          <div
            key={index}
            className="result-tile"
            onClick={() =>  window.location.href = item.url}
          >
            <h3 className="result-title">{item.title}</h3>
            <p className="result-desc">{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

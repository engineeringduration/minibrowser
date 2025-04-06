import { useState } from 'react';
import './SearchSection.css';

export function SearchSection() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);

    try {
      const res = await fetch(`http://127.0.0.1:5000/search?query=${query}`);
      const data = await res.json();

      setResults(data.results?.slice(0, 5) || []);
    } catch (err) {
      console.error('Search failed:', err);
    } finally {
      setLoading(false);
    }
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
            onClick={() => window.location.href = item.url}

          >
            <h3 className="result-title">{item.title}</h3>
            <p className="result-desc">{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

import { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import './App.css';
import { Header } from './components/Header';
import { SearchSection } from './components/SearchSection';
import { AIResponseSection } from './components/AIResponseSection';

function App() {
  const [query, setQuery] = useState('');
  const [searchParams, setSearchParams] = useSearchParams();

  useEffect(() => {
    const savedQuery = searchParams.get('q');
    if (savedQuery) {
      setQuery(savedQuery);
    }
  }, [searchParams]);

  const handleSearch = (newQuery) => {
    setQuery(newQuery);
    setSearchParams({ q: newQuery });
  };

  return (
    <div className="app">
      <Header />
      <div className="main-content">
        <SearchSection onSearch={handleSearch} query={query} />
        <AIResponseSection query={query} />
      </div>
    </div>
  );
}

export default App;

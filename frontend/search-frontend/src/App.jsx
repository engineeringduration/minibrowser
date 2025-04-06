import './App.css';
import { Header } from './components/Header';
import { SearchSection } from './components/SearchSection';
import { AIResponseSection } from './components/AIResponseSection';


function App() {
  return (
    <div className="app">
      <Header />
      <div className="main-content">
        <SearchSection />
        <AIResponseSection />
</div>

    </div>
  );
}

export default App;

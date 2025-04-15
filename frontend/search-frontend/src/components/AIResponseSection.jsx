import { useEffect, useState } from 'react';
import './AIResponseSection.css';

// Helper to format AI response with bold and clickable links
function formatAiText(text) {
  if (!text) return '';

  // Bold: **text**
  text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

  // Links: [text](url)
  text = text.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

  return text;
}

export function AIResponseSection({ query }) {
  const [aiAnswer, setAiAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchAiAnswer = async () => {
      if (!query.trim()) {
        setAiAnswer('');
        return;
      }

      setLoading(true);
      try {
        const res = await fetch(`http://localhost:5000/ai_answer?query=${encodeURIComponent(query)}`);
        const data = await res.json();

        const formatted = formatAiText(data.ai_answer || 'No AI answer available.');
        setAiAnswer(formatted);
      } catch (err) {
        console.error('Error fetching AI answer:', err);
        setAiAnswer('❌ Failed to fetch AI answer.');
      } finally {
        setLoading(false);
      }
    };

    fetchAiAnswer();
  }, [query]);

  return (
    <div className="ai-section">
      <h3>AI-Generated Answer</h3>
      <div className="ai-box">
        {loading ? (
          <p className="loading-text">Generating AI response...</p>
        ) : (
          <div
            className="ai-answer-content"
            dangerouslySetInnerHTML={{ __html: aiAnswer }}
          ></div>
        )}
      </div>
    </div>
  );
}

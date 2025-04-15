function formatAiText(text) {
    if (!text) return '';
  
    // Convert **bold** to <strong>
    text = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  
    // Convert [text](url) to <a href="url">text</a>
    text = text.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
  
    return text;
  }
  
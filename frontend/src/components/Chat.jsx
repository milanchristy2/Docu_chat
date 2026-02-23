import { useState } from "react";
import { queryDocument } from "../services/api";

function Chat({ documentId }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const chatId = "3fa85f64-5717-4562-b3fc-2c963f66afa6";

  const handleAsk = async () => {
    if (!question.trim()) return;
    if (!documentId) {
      setError("Please upload a document first.");
      return;
    }

    setLoading(true);
    setError("");
    setAnswer("");
    
    try {
      const result = await queryDocument(chatId, question, documentId);
      setAnswer(result.content || result.answer || "");
    } catch {
      setError("Failed to get response. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div className="card p-4 shadow-sm">
      <h4 className="mb-3">Ask a Question</h4>

      <textarea
        className="form-control mb-3"
        rows="4"
        placeholder="Type your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button 
        className="btn btn-success w-100 mb-4" 
        onClick={handleAsk}
        disabled={loading}
      >
        {loading ? "Loading..." : "Ask"}
      </button>

      {error && <div className="alert alert-danger">{error}</div>}
      {answer && (
        <div className="card bg-light p-3">
          <h5 className="text-primary">Answer:</h5>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default Chat;

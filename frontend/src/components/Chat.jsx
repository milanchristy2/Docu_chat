import { useState } from "react";
import { queryDocument } from "../services/api";

function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const chatId = "3fa85f64-5717-4562-b3fc-2c963f66afa6";

  const handleAsk = async () => {
    if (!question.trim()) return;

    const response = await queryDocument(chatId, question);
    setAnswer(response.content);
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

      <button className="btn btn-success w-100 mb-4" onClick={handleAsk}>
        Ask
      </button>

      {answer && (
        <>
          <h5>Answer:</h5>
          <div className="border rounded p-3 bg-light">
            {answer}
          </div>
        </>
      )}
    </div>
  );
}

export default Chat;

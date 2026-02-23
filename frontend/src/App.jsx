import { useState } from "react";
import Navbar from "./components/Navbar";
import Upload from "./components/Upload";
import Chat from "./components/Chat";

function App() {
  const [documentId, setDocumentId] = useState(null);

  return (
    <div className="min-vh-100 bg-light">

      <Navbar />

      <div className="container-fluid py-4 px-5">
        <Upload onUploadSuccess={setDocumentId} />
        <Chat documentId={documentId} />
      </div>

    </div>
  );
}

export default App;

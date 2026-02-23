import { useState } from "react";
import { uploadDocument } from "../services/api";

function Upload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const result = await uploadDocument(file);
    setMessage("Uploaded successfully");
    if (onUploadSuccess) {
      onUploadSuccess(result.document_id);
    }
  };

  return (
    <div className="card p-4 mb-4 shadow-sm">
      <h4 className="mb-3">Upload Document</h4>

      <div className="input-group">
        <input
          type="file"
          className="form-control"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button className="btn btn-primary" onClick={handleUpload}>
          Upload
        </button>
      </div>

      {message && (
        <div className="alert alert-success mt-3">
          {message}
        </div>
      )}
    </div>
  );
}

export default Upload;

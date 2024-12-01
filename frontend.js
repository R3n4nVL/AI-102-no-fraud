import React, { useState } from "react";

function DocumentUploader() {
  const [file, setFile] = useState(null);
  const [analysisResult, setAnalysisResult] = useState("");

  const handleFileUpload = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      body: formData,
    });
    const result = await response.json();
    setAnalysisResult(result.analysis);
  };

  return (
    <div>
      <h1>Upload Documento</h1>
      <input type="file" onChange={handleFileUpload} />
      <button onClick={handleSubmit}>Analisar Documento</button>
      <div>
        <h2>Resultado da Análise</h2>
        <p>{analysisResult}</p>
      </div>
    </div>
  );
}

export default DocumentUploader;

import React from "react";

const PDFViewer = ({ pdfName }) => {
    // Path to the PDF file in the public folder
    const pdfUrl = `/${pdfName}`;

    return (
        <div style={{ textAlign: 'center', margin: '20px' }}>
            <iframe
                src={pdfUrl}
                title="PDF Document"
                style={{ width: '90%', height: '600px', border: '1px solid #ccc' }}
            ></iframe>
            {/* No download button as per your requirements */}
        </div>
    );
};

export default PDFViewer;
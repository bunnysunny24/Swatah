import React from "react";

const SwatahViewer = () => {
    const resumeUrl = "/pdf/udit_qr.pdf"; // URL of the Swatah in the public/pdf folder

    // Responsive styles based on screen size
    const containerStyle = {
        textAlign: 'center',
        margin: '20px',
        padding: '0 10px'
    };
    
    const iframeContainerStyle = {
        width: '100%',
        maxWidth: '1000px',
        margin: '0 auto'
    };
    
    const iframeStyle = {
        width: '100%',
        height: '800px', 
        border: '1px solid #ccc',
        borderRadius: '8px',
        boxShadow: '0 4px 8px rgba(0,0,0,0.1)'
    };
    
    // Adjust height for mobile devices
    if (window.innerWidth <= 768) {
        iframeStyle.height = '500px';
    }

    return (
        <div style={containerStyle}>
            <div style={iframeContainerStyle}>                <iframe
                    src={resumeUrl}
                    title="Swatah"
                    style={iframeStyle}
                    frameBorder="0"
                ></iframe>
            </div>
            <div style={{ marginTop: '20px' }}>                <a href={resumeUrl} download="udit_swatah.pdf">
                    <button style={{ 
                        padding: '12px 24px', 
                        fontSize: '16px', 
                        cursor: 'pointer',
                        backgroundColor: '#4285f4',
                        color: 'white',
                        border: 'none',
                        borderRadius: '4px',
                        fontWeight: 'bold',
                        transition: 'background-color 0.3s'
                    }}>Download PDF</button>
                </a>
            </div>
        </div>
    );
};

export default SwatahViewer;
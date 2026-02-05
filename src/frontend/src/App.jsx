import React, { useState } from 'react';

const Homepage = () => {
  const [healthMessage, setHealthMessage] = useState(null);
  const [syllabiMessage, setSyllabiMessage] = useState(null);

  const checkBackendHealth = async () => {
    try {
      // Assumes your backend is running on the same host/port or proxy is set up
      const response = await fetch('/api/health');
      const data = await response.json();

      // Checks for the specific Flask jsonify({'status': 'ok'}) response
      if (data.status === 'ok') {
        setHealthMessage('backend link healthy');
      } else {
        setHealthMessage('Unexpected response status');
      }
    } catch (error) {
      console.error('Health check failed:', error);
      setHealthMessage('Error connecting to backend');
    }
  };
    const testDefaultProcessor = async () => {
        try {
            const response = await fetch('/api/syllabus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    name:'syllabus name test'
                })
            })

            const data = await response.json();
            if (data.response = 'syllabus name test') {
                setSyllabiMessage(data.response);
            }
            else {
                setSyllabiMessage('something failed :(');
            }

        } catch(error) {
            console.error('Health check failed:', error);
            setSyllabiMessage('Failed returning :(');
        }
    };
  return (
    <div style={styles.container}>
      {/* App Name */}
      <h1 style={styles.header}>Syllabye</h1>

      {/* Warning/Disclaimer */}
      <div style={styles.disclaimerBox}>
        <p style={styles.disclaimerText}>
          This is just a template starting page that should be replaced asap.
        </p>
      </div>

      {/* Health Check Button */}
      <button onClick={checkBackendHealth} style={styles.button}>
        Test /health Route
      </button>

      {/* Conditional Success Message */}
      {healthMessage && (
        <p style={styles.successMessage}>
          {healthMessage}
        </p>
      )}
    {/*      Syllabus backend test button */}
    <button onClick={testDefaultProcessor} style={styles.button}>
          Test /syllabus Route
        </button>

        {/* Conditional Success Message */}
        {syllabiMessage && (
          <p style={styles.successMessage}>
            {syllabiMessage}
          </p>
        )}
    </div>
  );
};

// Basic inline styles for quick visualization
const styles = {
  container: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
      fontFamily: 'Arial, sans-serif',
      backgroundColor: '#f4f4f9',
    },
    header: {
      fontSize: '3rem',
      marginBottom: '20px',
      color: '#333',
    },
    disclaimerBox: {
      backgroundColor: '#ffdddd',
      border: '1px solid #ffcccc',
      padding: '15px',
      borderRadius: '5px',
      marginBottom: '30px',
    },
    disclaimerText: {
      color: '#d8000c',
      margin: 0,
      fontWeight: 'bold',
    },
    button: {
      padding: '12px 24px',
      fontSize: '1rem',
      backgroundColor: '#007bff',
      color: 'white',
      border: 'none',
      borderRadius: '4px',
      cursor: 'pointer',
      transition: 'background-color 0.2s',
    },
    successMessage: {
      marginTop: '20px',
      color: 'green',
      fontSize: '1.2rem',
      fontWeight: 'bold',
    },
};

export default Homepage;
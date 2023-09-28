import React, { useState, useEffect } from 'react';
import axios from '../api/axios';

const ShortenURL = () => {
  const [longUrl, setLongUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [task_id, setTaskId] = useState(null); // Assuming task_id is stored in state

  useEffect(() => {
    let pollCount = 0;
    const maxPollCount = 20; // Maximum poll count, each poll will be 2 seconds, so 20 polls will make 40 seconds.

    const pollTaskStatus = async () => {
      try {
        const response = await axios.get('/task/' + task_id);
        if (response.data.status === 'completed') {
          setIsLoading(false);
          setShortUrl(response.data.short_url);
        } else if (pollCount < maxPollCount) {
          pollCount++;
          setTimeout(pollTaskStatus, 2000); // Poll every 2 seconds
        } else {
          setErrorMessage('Timed out, please retry again');
        }
      } catch (error) {
        setErrorMessage('An error occurred while polling');
      }
    };

    if (task_id) {
      pollTaskStatus();
    }

    return () => {
      // Clean up function to clear any pending timeouts if the component unmounts
      clearTimeout(pollTaskStatus);
    };
  }, [task_id]); // Dependency array to run the effect when task_id changes

  const handleResponse = (response) => {
    if (response.status === 'completed') {
      setShortUrl(response.short_url);
    }else {
      setTaskId(response.task_id);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setErrorMessage('');

    try {
      const response = await axios.post('/', { full_url: longUrl });
      handleResponse(response.data);
    } catch (error) {
      if (error.response.status === 409) {
        setShortUrl(error.response.data.detail.short_url);
        setIsLoading(false);
        setErrorMessage(error.response.data.detail.error);
      } else if(error.response.status !== 500){
        setErrorMessage(error.response.data.detail.error);
        setIsLoading(false);
      }else {
        setErrorMessage('An error occurred. Please try again later.');
        setIsLoading(false);
      }
    }

  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md">
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label
              htmlFor="longUrl"
              className="block mb-2 text-lg font-medium text-gray-700"
            >
              Enter a URL to shorten:
            </label>
            <input
              type="text"
              id="longUrl"
              className="w-full px-4 py-2 text-lg text-gray-700 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
              value={longUrl}
              onChange={(e) => setLongUrl(e.target.value)}
              required
            />
          </div>
          <div className="mb-4">
            <button
              type="submit"
              className="w-full px-6 py-3 text-lg font-medium text-white bg-indigo-500 rounded-md hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              disabled={isLoading}
            >
              {isLoading ? 'Shortening...' : 'Shorten URL'}
            </button>
          </div>
          {errorMessage && (
            <div className="mb-4 text-red-500 text-center">{errorMessage}</div>
          )}
          {shortUrl && (
            <div className="mb-4">
              <label
                htmlFor="fullUrl"
                className="block mb-2 text-lg font-medium text-gray-700"
              >
                Full URL:
              </label>
              <input
                type="text"
                id="fullUrl"
                className="w-full px-4 py-2 text-lg text-gray-700 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
                value={longUrl}
                readOnly
                onClick={(e) => e.target.select()}
              />
              <label
                htmlFor="shortUrl"
                className="block mt-4 mb-2 text-lg font-medium text-gray-700"
              >
                Short URL:
              </label>
              <input
                type="text"
                id="shortUrl"
                className="w-full px-4 py-2 text-lg text-gray-700 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
                value={shortUrl}
                readOnly
                onClick={(e) => e.target.select()}
              />
            </div>
          )}
        </form>
      </div>
    </div>
  );
};

export default ShortenURL;
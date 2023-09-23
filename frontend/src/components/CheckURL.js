import React, { useState } from 'react';
import axios from '../api/axios';

const CheckURL = () => {
  const [shortUrl, setShortUrl] = useState('');
  const [longUrl, setLongUrl] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const handleCheckUrl = async () => {
    setIsLoading(true);
    setErrorMessage('');
    try {
      const response = await axios.get(`/short_url/${shortUrl}`);
      setLongUrl(response.data.full_url);

    } catch (error) {
      if (error.response && error.response.status === 404) {
        setErrorMessage('URL not found.');
      } else {
        setErrorMessage('An error occurred. Please try again later.');
      }
    }

    setIsLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md">
        <form>
          <div className="mb-4">
            <label
              htmlFor="shortUrl"
              className="block mb-2 text-lg font-medium text-gray-700"
            >
              Enter a short URL to check:
            </label>
            <input
              type="text"
              id="shortUrl"
              className="w-full px-4 py-2 text-lg text-gray-700 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
              value={shortUrl}
              onChange={(e) => setShortUrl(e.target.value)}
              required
            />
          </div>
          <div className="mb-4">
            <button
              type="button"
              className="w-full px-6 py-3 text-lg font-medium text-white bg-indigo-500 rounded-md hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              onClick={handleCheckUrl}
              disabled={isLoading}
            >
              {isLoading ? 'Checking...' : 'Check URL'}
            </button>
          </div>
          {errorMessage && (
            <div className="mb-4 text-red-500 text-center">{errorMessage}</div>
          )}
          {longUrl && (
            <div className="mb-4">
              <label
                htmlFor="longUrl"
                className="block mb-2 text-lg font-medium text-gray-700"
              >
                Long URL:
              </label>
              <input
                type="text"
                id="longUrl"
                className="w-full px-4 py-2 text-lg text-gray-700 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
                value={longUrl}
                readOnly
              />
              <button
                type="button"
                className="mt-2 px-6 py-3 text-lg font-medium text-white bg-indigo-500 rounded-md hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                onClick={() => window.open(longUrl, '_blank')}
              >
                Visit
              </button>
            </div>
          )}
        </form>
      </div>
    </div>
  );
};

export default CheckURL;
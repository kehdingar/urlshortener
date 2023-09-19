import React, { useState } from 'react';
import axios from '../api/axios'

const ShortenURL = () => {
  const [longUrl, setLongUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');


  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setErrorMessage('');

    try {
      const response = await axios.post('/urls', { full_url: longUrl });
      setShortUrl(response.data.short_url);
    } catch (error) {      
      if (error.response && error.response.status === 400) {
        setErrorMessage(error.response.data.detail);
        console.log(error.response)
        console.log(error)
      } else {
        setErrorMessage('An error occurred. Please try again later.');
        console.log(error)
      }
    }

    setIsLoading(false);
    console.log("The RESPONSE Check.......")
    console.log(shortUrl)
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
import React, { useState } from 'react';
import ShortenURL from './ShortenURL';
import CheckURL from './CheckURL';

const URLShortener = () => {
  const [isCheckingURL, setIsCheckingURL] = useState(false);

  const handleToggleComponent = () => {
    setIsCheckingURL((prevState) => !prevState);
  };

  return (
    <div className="relative">
      <button
        className="absolute top-4 right-4 px-4 py-2 text-sm font-medium text-white bg-indigo-500 rounded-md hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        onClick={handleToggleComponent}
      >
        {isCheckingURL ? 'Shorten URL' : 'Check URL'}
      </button>

      {/* Add the CSS class to the components and toggle it */}
      {isCheckingURL ?  <CheckURL/> : <ShortenURL/> }
    </div>
  );
};

export default URLShortener;
import React from 'react';
import './index.css';
import App from './App';
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider, Link, } from "react-router-dom";


function ErrorPage() {
  return (
    <div className='min-h-screen bg-indigo-500 flex justify-center items-center'>
      <div className='py-12 px-12 bg-white rounded-2xl shadow-xl z-20'>
        <h1 className="text-3xl font-bold text-center">Oops! Nothing found</h1>
        <p className="text-1xl font-bold text-center my-7">Home <Link to="/"><span className="text-1xl underline">Here</span></Link></p>
      </div>
    </div>
  )
}

const router = createBrowserRouter([
  {
    path: "/",
    element:
        <App />
  },
  {
    path: "*",
    element: <ErrorPage />
  },
]);

createRoot(document.getElementById("root")).render(
  <>
    <RouterProvider router={router} />
  </>
);


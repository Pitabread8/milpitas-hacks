"use client"
import Image from 'next/image'

import React, { useState, useEffect } from 'react';

const Chat = () => {
  const [textData, setTextData] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({});

  const handleFormDataChange = (event) => {
    setFormData({...formData, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    try {
      const urlParams = new URLSearchParams(formData);
      const response = await fetch(`http://localhost:5000/api/summarize?${urlParams.toString()}`);
      const data = await response.json();
      setTextData(data.text);
    } catch (error) {
      console.error('Error fetching text data:', error);
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}
        className="w-full rounded-md border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"    
      >
        <label>
          Url Input
          <input type="text" name="url" onChange={handleFormDataChange} style={{ color: 'black' }}/>
        </label>
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          style={{ marginLeft: '16px' }}
        >
          Submit
        </button>
      </form>
      {isLoading? (
        <p>Loading text data...</p>
      ) : error? (
        <p>Error: {error.message}</p>
      ) : (
        <textarea
          type="text"
          className="w-full rounded-md border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
          readOnly={true}
          value={textData}
        />
      )}
    </div>
  );
};

// export default Chat;

export default function Home() {
  return (
    <>
      <div className="font-serif">
        <div className="text-[#EEEEEE] h-screen w-screen flex justify-center items-center flex-col gap-2">
          <h1 className="text-[#EEEEEE] text-[150px] italic fade-up-right">The Truth Project</h1>
          <p className="py-2 w-2/3 text-center text-2xl leading-loose">Empower yourself with knowledge. Our website detects the political bias in the news you consume and offers concise summaries, helping you stay informed without bias.</p>
        </div>
        <div className="bg-white h-screen w-screen flex flex-row items-start pt-16 justify-center">
          <div className="pl-12">
            <h1 className="text-6xl text-left">Get Your News, Quick.</h1>
            <Chat />
          </div>
          <Image
            className="pr-12"
            src="/image.png"
            width={500}
            height={500}
            alt="Image"
          />
        </div>
      </div>
    </>
  );
}

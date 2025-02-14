// src/Home.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const navigate = useNavigate();

    return (
        <div>
            <h1>Home Page</h1>
            <button onClick={() => navigate('/about')}>Go to About</button>
            <button onClick={() => navigate('/contact')}>Go to Contact</button>
        </div>
    );
};

export default Home;

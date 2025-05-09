import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import './MoviesPage.css'; // ✅ CSS 파일 import

const MoviesPage = () => {
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('/movies/')
      .then(res => setMovies(res.data))
      .catch(err => {
        console.error('영화 목록 불러오기 실패:', err);
        setError('영화 목록을 불러오는 데 실패했습니다.');
      });
  }, []);

  return (
    <div className="movies-page">
      <h2 style={{ fontSize: '1.75rem', fontWeight: 'bold', marginBottom: '1rem' }}>
        🎬 지금 볼 수 있는 영화
      </h2>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <div className="movies-grid">
        {movies.map((movie) => (
          <div key={movie.id} className="movie-card">
            <img
              src={movie.thumbnail_url}
              alt={movie.title}
              className="movie-thumbnail"
            />
            <div className="movie-info">
              <h3>{movie.title}</h3>
              <p>{movie.release_date}</p>
              <p style={{ color: '#facc15' }}>⭐ {movie.average_rating}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MoviesPage;
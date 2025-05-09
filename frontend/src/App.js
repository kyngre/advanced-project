import React, { useEffect, useState } from 'react';
import axios from './api/axios';

function App() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    axios.get('/movies/')
      .then(response => {
        setMovies(response.data);
      })
      .catch(error => {
        console.error('영화 목록 가져오기 실패:', error);
      });
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>🎬 영화 목록</h1>
      {movies.length === 0 ? (
        <p>영화를 불러오는 중...</p>
      ) : (
        movies.map(movie => (
          <div key={movie.id} style={{ border: '1px solid #ccc', marginBottom: '1rem', padding: '1rem' }}>
            <h2>{movie.title}</h2>
            <p>{movie.description}</p>
            <p><strong>개봉일:</strong> {movie.release_date}</p>
            <p><strong>평균 평점:</strong> {movie.average_rating_cache}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;

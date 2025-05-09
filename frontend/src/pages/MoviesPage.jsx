import React, { useEffect, useState } from 'react';
import axios from '../api/axios'; // ← 반드시 로컬 axios 인스턴스 사용

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
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">🎬 영화 목록</h2>

      {error && <p className="text-red-500">{error}</p>}

      <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
        {movies.map((movie) => (
          <div key={movie.id} className="bg-white shadow rounded-lg overflow-hidden">
            <img
              src={movie.thumbnail_url}
              alt={movie.title}
              className="w-full h-48 object-cover"
            />
            <div className="p-4">
              <h3 className="font-semibold text-lg truncate">{movie.title}</h3>
              <p className="text-sm text-gray-500">{movie.release_date}</p>
              <p className="text-yellow-500 font-semibold">⭐ {movie.average_rating}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MoviesPage;
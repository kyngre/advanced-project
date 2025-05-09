import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from '../api/axios';

const MovieDetailPage = () => {
  const { id } = useParams(); // URL에서 영화 ID 추출
  const [movie, setMovie] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get(`/movies/${id}/`)
      .then(res => setMovie(res.data))
      .catch(() => setError('영화 정보를 불러오지 못했습니다.'));
  }, [id]);

  if (error) return <div className="p-6 text-red-500">{error}</div>;
  if (!movie) return <div className="p-6 text-white">로딩 중...</div>;

  return (
    <div className="p-6 text-white">
      <h2 className="text-2xl font-bold mb-4">{movie.title}</h2>
      <img
        src={movie.thumbnail_url}
        alt={movie.title}
        className="w-full max-w-md rounded-lg mb-4"
      />
      <p className="text-gray-300 mb-2">{movie.release_date}</p>
      <p className="text-yellow-400 mb-4">⭐ {movie.average_rating} / 5</p>
      <p className="mb-6">{movie.description}</p>

      {/* OTT 로고 표시 */}
      <div className="flex gap-3 mt-4">
        {movie.ott_services?.map((ott) => (
          <img
            key={ott.id}
            src={ott.logo_url}
            alt={ott.name}
            title={ott.name}
            className="w-8 h-8 rounded"
          />
        ))}
      </div>
    </div>
  );
};

export default MovieDetailPage;
import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import { useParams } from 'react-router-dom';
import './MovieDetailPage.css';

const MovieDetailPage = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);

  useEffect(() => {
    const fetchMovieDetail = async () => {
      try {
        const response = await axios.get(`/movies/${id}/`);
        setMovie(response.data);
      } catch (error) {
        console.error('영화 정보를 불러오지 못했습니다:', error);
      }
    };

    fetchMovieDetail();
  }, [id]);

  if (!movie) return <div>로딩 중...</div>;

  return (
    <div className="movie-detail-container">
      <h1>{movie.title}</h1>
      <img src={movie.thumbnail_url} alt={movie.title} />
      <p>{movie.description}</p>

      <div className="ott-logos">
        {movie.ott_list.map(ott => (
          <img
            key={ott.id}
            src={ott.logo_url}
            alt={ott.name}
            className="ott-logo"
          />
        ))}
      </div>

      <h2>🎬 리뷰 목록</h2>
      <div className="reviews">
        {movie.reviews.length === 0 ? (
          <p>아직 작성된 리뷰가 없습니다.</p>
        ) : (
          movie.reviews.map((review) => (
            <div key={review.id} className="review-card">
              <p><strong>작성자:</strong> {review.user}</p>
              <p><strong>평점:</strong> {review.rating} / 5</p>
              <p><strong>내용:</strong> {review.comment}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default MovieDetailPage;
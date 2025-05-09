import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import { useParams } from 'react-router-dom';
import './MovieDetailPage.css';

const MovieDetailPage = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [newReview, setNewReview] = useState({ rating: 5, comment: '' });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const fetchMovieDetail = async () => {
    try {
      const response = await axios.get(`/movies/${id}/`);
      setMovie(response.data);
    } catch (error) {
      console.error('영화 정보를 불러오지 못했습니다:', error);
    }
  };

  useEffect(() => {
    fetchMovieDetail();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    try {
      const token = localStorage.getItem('access');
      await axios.post(
        `/reviews/`,
        {
          movie: id,
          rating: newReview.rating,
          comment: newReview.comment,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setNewReview({ rating: 5, comment: '' });
      fetchMovieDetail();
    } catch (error) {
      console.error('리뷰 작성 실패:', error);
    }
    setIsSubmitting(false);
  };

  const handleLike = async (reviewId) => {
    const token = localStorage.getItem('access');
    if (!token) {
      alert('로그인이 필요합니다.');
      return;
    }

    try {
      await axios.post(
        `/reviews/${reviewId}/like/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      fetchMovieDetail();
    } catch (error) {
      console.error('좋아요 실패:', error);
    }
  };

  if (!movie) return <div>로딩 중...</div>;

  const top3Reviews = [...(movie.reviews || [])]
    .sort((a, b) => b.like_count - a.like_count)
    .slice(0, 3);

  const otherReviews = (movie.reviews || []).filter(
    (review) => !top3Reviews.find((top) => top.id === review.id)
  );

  return (
    <div className="movie-detail-container">
      <h1>{movie.title}</h1>
      <img src={movie.thumbnail_url} alt={movie.title} />
      <p>{movie.description}</p>

      <div className="ott-logos">
        {movie.ott_list?.map(ott => (
          <img
            key={ott.id}
            src={ott.logo_url}
            alt={ott.name}
            className="ott-logo"
          />
        ))}
      </div>

      <h2>📝 리뷰 작성</h2>
      <form onSubmit={handleSubmit} className="review-form">
        <label>
          평점:
          <select
            value={newReview.rating}
            onChange={(e) => setNewReview({ ...newReview, rating: e.target.value })}
          >
            {[1, 2, 3, 4, 5].map((num) => (
              <option key={num} value={num}>
                {num}
              </option>
            ))}
          </select>
        </label>
        <label>
          코멘트:
          <textarea
            value={newReview.comment}
            onChange={(e) => setNewReview({ ...newReview, comment: e.target.value })}
          />
        </label>
        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? '작성 중...' : '리뷰 작성'}
        </button>
      </form>

      <h2>🎖️ Top 3 리뷰</h2>
      <div className="reviews">
        {top3Reviews.length === 0 ? (
          <p>아직 추천된 리뷰가 없습니다.</p>
        ) : (
          top3Reviews.map((review) => (
            <div key={review.id} className="review-card top-review">
              <p><strong>작성자:</strong> {review.user}</p>
              <p><strong>평점:</strong> {review.rating} / 5</p>
              <p><strong>내용:</strong> {review.comment}</p>
              <button onClick={() => handleLike(review.id)}>
                👍 {review.like_count}
              </button>
            </div>
          ))
        )}
      </div>

      <h2>📝 다른 리뷰</h2>
      <div className="reviews">
        {otherReviews.length === 0 ? (
          <p>다른 리뷰가 없습니다.</p>
        ) : (
          otherReviews.map((review) => (
            <div key={review.id} className="review-card">
              <p><strong>작성자:</strong> {review.user}</p>
              <p><strong>평점:</strong> {review.rating} / 5</p>
              <p><strong>내용:</strong> {review.comment}</p>
              <button onClick={() => handleLike(review.id)}>
                👍 {review.like_count}
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default MovieDetailPage;
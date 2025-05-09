import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import './MoviesPage.css';

const MoviesPage = () => {
  const [movies, setMovies] = useState([]);
  const [search, setSearch] = useState('');
  const [ott, setOtt] = useState('');
  const [ordering, setOrdering] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    let url = '/movies/search/?';
    if (search) url += `search=${search}&`;
    if (ott) url += `ott_services=${ott}&`;
    if (ordering) url += `ordering=${ordering}`;

    axios.get(url)
      .then(res => setMovies(res.data))
      .catch(err => {
        console.error('영화 목록 불러오기 실패:', err);
        setError('영화 목록을 불러오는 데 실패했습니다.');
      });
  }, [search, ott, ordering]);

  return (
    <div className="movies-page">
      <h2 className="text-2xl font-bold mb-4">🎬 영화 탐색</h2>

      {/* ✅ 검색 및 필터 UI */}
      <div className="filter-bar">
        <input
          type="text"
          placeholder="영화 제목 검색"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <select value={ott} onChange={(e) => setOtt(e.target.value)}>
          <option value="">OTT 전체</option>
          <option value="1">Netflix</option>
          <option value="2">Disney+</option>
          <option value="3">왓챠</option>
          {/* 필요한 만큼 추가 */}
        </select>
        <select value={ordering} onChange={(e) => setOrdering(e.target.value)}>
          <option value="">정렬 없음</option>
          <option value="-release_date">최신순</option>
          <option value="-average_rating">평점 높은순</option>
          <option value="average_rating">평점 낮은순</option>
          <option value="title">제목순</option>
        </select>
      </div>

      {/* ✅ 에러 메시지 */}
      {error && <p className="text-red-500">{error}</p>}

      {/* ✅ 영화 카드 */}
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
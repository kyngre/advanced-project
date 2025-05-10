import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import { useNavigate } from 'react-router-dom';
import './SubscribePage.css';

const SubscribePage = () => {
  const [ottList, setOttList] = useState([]);
  const [selectedOtts, setSelectedOtts] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('/ott/')
      .then(res => setOttList(res.data))
      .catch(err => console.error('OTT 목록 불러오기 실패:', err));
  }, []);

  const toggleOtt = (id) => {
    setSelectedOtts(prev =>
      prev.includes(id) ? prev.filter(ottId => ottId !== id) : [...prev, id]
    );
  };

  const handleSubmit = async () => {
    try {
      await axios.post('/users/subscribe/', { ott_ids: selectedOtts });
      navigate('/');  // 완료 후 메인 페이지로
    } catch (err) {
      alert('구독 설정에 실패했습니다.');
    }
  };

  return (
    <div className="subscribe-page">
      <h2>🎬 구독 중인 OTT를 선택해주세요</h2>
      <p>구독 중인 OTT가 없다면 선택하지 않고 '저장하기'를 눌러도 됩니다.</p>

      <div className="ott-list">
        {ottList.map(ott => (
          <label key={ott.id} className="ott-item">
            <input
              type="checkbox"
              checked={selectedOtts.includes(ott.id)}
              onChange={() => toggleOtt(ott.id)}
            />
            <img src={ott.logo_url} alt={ott.name} />
            <span>{ott.name}</span>
          </label>
        ))}
      </div>

      <button onClick={handleSubmit} className="save-btn">저장하기</button>
    </div>
  );
};

export default SubscribePage;
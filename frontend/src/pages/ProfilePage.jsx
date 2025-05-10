import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import './ProfilePage.css';

const ProfilePage = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [subscribedOtts, setSubscribedOtts] = useState([]);
  const [ottList, setOttList] = useState([]);
  const [message, setMessage] = useState('');

  useEffect(() => {
    // OTT 목록 먼저 가져오기
    axios.get('/ott/').then(res => setOttList(res.data));

    // 사용자 프로필 정보 가져오기
    axios.get('/users/profile/').then(res => {
      setEmail(res.data.email);
      setUsername(res.data.username);
      setSubscribedOtts(res.data.subscribed_ott.map(ott => ott.id));
    });
  }, []);

  const toggleOtt = (id) => {
    setSubscribedOtts(prev =>
      prev.includes(id) ? prev.filter(o => o !== id) : [...prev, id]
    );
  };

  const handleSave = async () => {
    try {
      await axios.put('/users/update/', { username }); // 사용자명 수정
      await axios.post('/users/subscribe/', { ott_ids: subscribedOtts }); // 구독 OTT 수정
      setMessage('저장되었습니다!');
    } catch (err) {
      setMessage('저장에 실패했습니다.');
    }
  };

  return (
    <div className="profile-page">
      <h2>👤 회원정보</h2>
      <p><strong>이메일:</strong> {email}</p>

      <label>닉네임</label>
      <input value={username} onChange={(e) => setUsername(e.target.value)} />

      <label>구독 중인 OTT</label>
      <div className="ott-list">
        {ottList.map(ott => (
          <label key={ott.id} className="ott-item">
            <input
              type="checkbox"
              checked={subscribedOtts.includes(ott.id)}
              onChange={() => toggleOtt(ott.id)}
            />
            <img src={ott.logo_url} alt={ott.name} />
            <span>{ott.name}</span>
          </label>
        ))}
      </div>

      <button onClick={handleSave} className="save-btn">저장하기</button>
      {message && <p className="save-message">{message}</p>}
    </div>
  );
};

export default ProfilePage;
import React, { useEffect, useState } from 'react';
import axios from '../api/axios';
import './ProfilePage.css';
import { ClipLoader } from 'react-spinners';

const ProfilePage = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [subscribedOtts, setSubscribedOtts] = useState([]);
  const [ottList, setOttList] = useState([]);
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(true); // ✅ 로딩 상태

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [ottRes, profileRes] = await Promise.all([
          axios.get('/ott/'),
          axios.get('/users/profile/')
        ]);

        setOttList(ottRes.data);
        setEmail(profileRes.data.email);
        setUsername(profileRes.data.username);
        setSubscribedOtts(profileRes.data.subscribed_ott.map(o => o.id));
        setIsLoading(false); // ✅ 로딩 끝
      } catch (err) {
        console.error('프로필 정보를 불러오지 못했습니다:', err);
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  const toggleOtt = (id) => {
    setSubscribedOtts(prev =>
      prev.includes(id) ? prev.filter(o => o !== id) : [...prev, id]
    );
  };

  const handleSave = async () => {
    try {
      await axios.put('/users/update/', { username });
      await axios.post('/users/subscribe/', { ott_ids: subscribedOtts });
      setMessage('저장되었습니다!');
    } catch {
      setMessage('저장에 실패했습니다.');
    }
  };

  if (isLoading) {
    return (
      <div style={{
        height: '100vh',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#141414',
        flexDirection: 'column',
        color: 'white'
      }}>
        <ClipLoader color="#e50914" size={60} />
        <p style={{ marginTop: '1rem', fontSize: '1.1rem' }}>잠시만 기다려주세요...</p>
      </div>
    );
  }

  return (
    <div className="profile-page">
      <div className="profile-container">
        <h2>회원정보</h2>
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
    </div>
  );
};

export default ProfilePage;
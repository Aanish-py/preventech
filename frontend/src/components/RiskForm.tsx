import { useState } from 'react';
import { apiClient } from '../api/client';

export default function RiskForm({ onResult }: { onResult: (res: any) => void }) {
  const [area, setArea] = useState('AREA001');
  const handleCheck = async () => {
    try {
      const res = await apiClient.post('/api/predict', { area_code: area, disease: 'dengue' });
      onResult(res.data);
    } catch (e) { alert("Error"); }
  };
  return (
    <div className="bg-white p-6 rounded-lg shadow-md mb-6">
      <h2 className="text-xl font-bold mb-4">Check Outbreak Risk</h2>
      <div className="flex gap-4">
        <select value={area} onChange={e => setArea(e.target.value)} className="border p-2 rounded w-full">
            <option value="AREA001">Pune (AREA001)</option>
            <option value="AREA002">Mumbai (AREA002)</option>
        </select>
        <button onClick={handleCheck} className="bg-blue-600 text-white px-4 py-2 rounded">Analyze</button>
      </div>
    </div>
  );
}
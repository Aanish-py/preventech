import { useState } from 'react';
import { useQuery } from 'react-query';
import RiskForm from '../components/RiskForm';
import RiskCharts from '../components/RiskCharts';
import RiskMap from '../components/RiskMap';
import { apiClient } from '../api/client';

export default function Dashboard() {
  const [prediction, setPrediction] = useState<any>(null);
  const { data: stats } = useQuery('liveStats', () => apiClient.get('/api/stats/summary').then(res => res.data), { refetchInterval: 30000 });

  return (
    <div className="p-6 bg-gray-50 min-h-screen">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">PrevenTech Dashboard</h1>
        {stats && <div className="text-sm text-blue-600">Total Cases: {stats.total_cases} | High Risk Areas: {stats.high_risk_areas}</div>}
      </header>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <RiskForm onResult={setPrediction} />
          {prediction && (
            <div className={`p-6 rounded-lg text-white mb-6 ${prediction.risk_label === 'High' ? 'bg-red-500' : prediction.risk_label === 'Moderate' ? 'bg-yellow-500' : 'bg-green-500'}`}>
              <h2 className="text-2xl font-bold">{prediction.risk_label} Risk</h2>
              <p>Score: {Math.round(prediction.risk_score * 100)}%</p>
            </div>
          )}
          <RiskCharts area="AREA001" />
        </div>
        <div>
          <div className="bg-white p-4 rounded-lg shadow-md h-full"><h3 className="font-bold mb-4">Regional Heatmap</h3><RiskMap /></div>
        </div>
      </div>
    </div>
  );
}
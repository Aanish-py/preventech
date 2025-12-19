import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { useQuery } from 'react-query';
import { apiClient } from '../api/client';

export default function RiskCharts({ area }: { area: string }) {
  const { data: trends } = useQuery(['trends', area], () => apiClient.get(`/api/stats/trends?disease=dengue&area_code=${area}`).then(res => res.data));
  if(!trends) return <p>Loading...</p>;
  return (
    <div className="h-64 w-full bg-white p-4 rounded-lg shadow-md">
      <h3 className="text-sm font-bold mb-2">Dengue Trends ({area})</h3>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={trends}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="cases" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
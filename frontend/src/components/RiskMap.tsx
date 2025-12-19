import { MapContainer, TileLayer, CircleMarker, Popup } from 'react-leaflet';
import { useQuery } from 'react-query';
import { apiClient } from '../api/client';

export default function RiskMap() {
  const { data: heatmap } = useQuery('heatmap', () => apiClient.get('/api/stats/heatmap').then(res => res.data));

  return (
    <div className="h-64 w-full rounded-lg overflow-hidden shadow-md border z-0 relative">
      <MapContainer center={[18.5204, 73.8567]} zoom={7} style={{ height: '100%', width: '100%' }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {heatmap?.map((pt: any, idx: number) => (
          <CircleMarker key={idx} center={[pt.lat, pt.lng]} pathOptions={{ color: pt.risk_score > 0.5 ? 'red' : 'green' }} radius={20}>
            <Popup>Risk Score: {pt.risk_score}</Popup>
          </CircleMarker>
        ))}
      </MapContainer>
    </div>
  );
}
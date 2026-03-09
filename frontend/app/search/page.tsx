import { api } from '../../lib/api';

export default async function SearchPage() {
  const data = await api('/beauticians/search?location=');
  return (
    <div>
      <h2 className="mb-4 text-2xl font-semibold">Browse Beauticians</h2>
      <div className="grid gap-4 md:grid-cols-2">
        {data?.map((row: any, idx: number) => (
          <div key={idx} className="rounded border bg-white p-4">
            <p className="font-medium">{row[0].location || 'Location TBD'}</p>
            <p>{row[1].service_name}</p>
            <p>₹{row[1].price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

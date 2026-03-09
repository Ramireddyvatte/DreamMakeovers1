const BASE_URL = process.env.API_URL || 'http://localhost:8000/api/v1';

export async function api(path: string) {
  const res = await fetch(`${BASE_URL}${path}`, { cache: 'no-store' });
  if (!res.ok) return [];
  return res.json();
}

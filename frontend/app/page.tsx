import Link from 'next/link';

export default function HomePage() {
  return (
    <section className="space-y-4">
      <h1 className="text-3xl font-bold">Beauty services at home, by certified pros.</h1>
      <p>Book trusted beauticians, compare prices, and pay securely.</p>
      <Link href="/search" className="rounded bg-pink-600 px-4 py-2 text-white">Find Beauticians</Link>
    </section>
  );
}

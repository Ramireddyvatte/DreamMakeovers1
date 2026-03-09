import './globals.css';
import Link from 'next/link';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="bg-white shadow-sm">
          <nav className="mx-auto flex max-w-6xl gap-6 p-4">
            <Link href="/">DreamMakeovers</Link>
            <Link href="/search">Search</Link>
            <Link href="/dashboard">Dashboard</Link>
          </nav>
        </header>
        <main className="mx-auto max-w-6xl p-4">{children}</main>
      </body>
    </html>
  );
}

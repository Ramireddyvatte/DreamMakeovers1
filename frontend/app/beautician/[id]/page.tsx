export default function BeauticianProfilePage({ params }: { params: { id: string } }) {
  return (
    <div className="space-y-3">
      <h2 className="text-2xl font-semibold">Beautician #{params.id}</h2>
      <p>Portfolio images, certifications, pricing and reviews appear here.</p>
    </div>
  );
}

export default function BookingPage() {
  return (
    <form className="max-w-lg space-y-3 rounded bg-white p-4 shadow">
      <h2 className="text-xl font-semibold">Book Appointment</h2>
      <input className="w-full rounded border p-2" placeholder="Beautician ID" />
      <input className="w-full rounded border p-2" placeholder="Service ID" />
      <input className="w-full rounded border p-2" type="date" />
      <input className="w-full rounded border p-2" type="time" />
      <button className="rounded bg-pink-600 px-4 py-2 text-white" type="submit">Proceed to Payment</button>
    </form>
  );
}

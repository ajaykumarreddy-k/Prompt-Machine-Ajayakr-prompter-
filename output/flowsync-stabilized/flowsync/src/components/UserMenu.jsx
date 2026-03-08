const UserMenu = () => {
  return (
    <section className="bg-zinc-50 rounded-lg border border-zinc-200 shadow-md p-6 flex items-center space-x-4">
      <img src="/user-icon.png" alt="User" className="w-10 h-10 rounded-full" />
      <div>
        <p className="text-sm font-semibold">John Doe</p>
        <button className="secondary-btn">Settings</button>
      </div>
    </section>
  );
};

export default UserMenu;

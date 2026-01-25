const Button = ({ children }: { children: React.ReactNode }) => {
  return (
    <button
      className="
        px-6 py-2.5
        bg-emerald-500 text-white rounded-xl
        duration-150 hover:bg-emerald-400 active:scale-105
        cursor-pointer
      "
    >
      {children}
    </button>
  );
};

export default Button;

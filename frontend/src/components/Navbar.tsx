import Search from "./Search";

interface NavbarProps {
  searchTerm: string;
  setSearchTerm: (value: string) => void;
}

const Navbar = ({ searchTerm, setSearchTerm }: NavbarProps) => {
  return (
    <nav className="bg-violet-600 text-white py-4 shadow-md mb-16">
      <div className="container mx-auto flex flex-col md:flex-row gap-4 justify-between items-center">
        <a href="#">
          <h1 className="text-3xl font-medium font-logo">Welcome MrBeast!</h1>
        </a>
        <div className="flex-1 flex justify-center">
          <Search searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
        </div>
        <a href="#" className="font-medium">
          Login
        </a>
      </div>
    </nav>
  );
};

export default Navbar;

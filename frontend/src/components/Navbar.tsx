import Search from "./Search";

interface NavbarProps {
  searchTerm: string;
  setSearchTerm: (value: string) => void;
  username: string;
}

const Navbar = ({ searchTerm, setSearchTerm, username }: NavbarProps) => {
  return (
    <nav className="bg-violet-600 text-white py-4 shadow-md mb-16">
      <div className="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
        <a href="#" className="justify-self-center md:justify-self-start">
          <h1 className="text-3xl font-medium font-logo">
            Welcome {username}!
          </h1>
        </a>
        <div className="flex justify-center">
          <Search searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
        </div>
        <div className="hidden md:block"></div>
      </div>
    </nav>
  );
};

export default Navbar;

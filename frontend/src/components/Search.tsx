import { BsSearch } from "react-icons/bs";

interface SearchProps {
  searchTerm: string;
  setSearchTerm: (value: string) => void;
}

const Search = ({ searchTerm, setSearchTerm }: SearchProps) => {
  return (
    <div
      className="
        flex items-center px-3 py-2
        w-full max-w-md
        bg-violet-500/50 rounded-xl
        border border-transparent
        transition-all duration-200
        focus-within:bg-violet-500/70 focus-within:border-violet-500
      "
    >
      <span className="text-violet-200">
        <BsSearch />
      </span>
      <input
        type="text"
        placeholder="Search for offers..."
        className="
          flex-1 px-3 py-1 outline-none bg-transparent
          text-base text-white
          placeholder:text-violet-200
        "
        onChange={(e) => setSearchTerm(e.target.value)}
        value={searchTerm}
      />
    </div>
  );
};

export default Search;

import { useState, useEffect } from "react";
import axios from "axios";

const Search = ({ setResult }) => {
  const [plate, setPlate] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (plate.length) {
      axios.get("http://localhost:8000/api/cars/" + plate).then((res) => {
        res.data.length ? setResult(res.data) : setResult("No car found");
      });
    }
    setPlate("");
  };
 
  return ( 
    <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-2">
      <input
        className="p-2 border border-black rounded" 
        type="text"
        placeholder="Plate"
        value={plate}
        onChange={(e) => setPlate(e.target.value)}
      />
      <button
        type="submit"
        className="bg-gray-900 text-white p-2 px-4 rounded hover:bg-white hover:text-gray-900 border border-gray-900"
      >
        Search 
      </button>
    </form>
  );
};

export default Search;

import { useState } from "react";
import Search from "./components/Search";
import Results from "./components/Results";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="grid justify-items-center py-32 font-inter">
      <h1 className="text-3xl text-gray-900 font-black mb-8">
        Search for a car
      </h1>
      <Search setResult={setResult} />
      <Results result={result} />
    </div>
  );
}

export default App;

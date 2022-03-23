import { useEffect } from "react";
import Car from "./Car";

const Results = ({ result }) => {
  useEffect(() => {}, [result]);

  return (
    <div className="mt-16">
      {Array.isArray(result) ? (
        <Car result={result} />
      ) : result === "No car found" ? (
        <p className="text-lg font-light">
          {" "}
          No cars were found. Try with another plate.{" "}
        </p>
      ) : (
        <></>
      )}
    </div>
  );
};

export default Results;

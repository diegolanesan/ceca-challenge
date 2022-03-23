import carIcon from "../assets/car.png";
import plateIcon from "../assets/plate.png";

const Car = ({ result }) => {
  return (
    <div className="grid justify-items-center border border-gray-800 rounded p-4 shadow-lg ">
      <img src={carIcon} className="w-32" alt="car-icon" />
      <h1 className="font-bold mb-2 text-xl">{result[0].name}</h1>
      <div className="flex items-center gap-4">
        <img src={plateIcon} alt="plate-icon" className="w-9" />
        <p>{result[0].plate}</p>
      </div>
    </div>
  ); 
};
 
export default Car;
